from typing import List

import numpy as np
import pygame
import stable_baselines3
import torch
from gymnasium.vector.utils import spaces
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
import torch as th
from torch import nn

from xumes import Agent, Imitable, Imitator, Input
from xumes.modules.imitation_learning.bc import BC
from xumes.modules.reinforcement_learning.agent import OBST
from xumes import GodotAction


class PlayAgent(Agent, Imitable):

    def __init__(self, model_path: str = None, previous_model_path: str = None, width: int = 25, height: int = 25):
        super().__init__(
            observation_space=spaces.Dict({
                "cnn": spaces.Box(low=0, high=3, shape=(width, height), dtype=np.uint8),
                "ff": spaces.Box(low=-float('inf'), high=float('inf'), shape=(4,), dtype=np.float32),
            }),
            action_space=spaces.MultiDiscrete([2, 2, 2, 2]),
            max_episode_length=100,
            total_timesteps=int(3_000_000),
            algorithm_type="MultiInputPolicy",
            algorithm=stable_baselines3.PPO,
            save_path=model_path if model_path is not None else "./tests/jump/models/play",
            previous_model_path=previous_model_path,
            eval_freq=10000,
            policy_kwargs={"features_extractor_class": CustomCombinedExtractor, "features_extractor_kwargs": {
                "cnn_obs_space": spaces.Box(low=0, high=3, shape=(width, height), dtype=np.uint8),
                "ff_obs_space": spaces.Box(low=-float('inf'), high=float('inf'), shape=(4,), dtype=np.float32),
            }}
        )

        self.width = width
        self.height = height

    def observation(self) -> OBST:

        env = self.context.Player.environment
        if not env:
            return {
                "cnn": np.zeros((self.width, self.height), dtype=np.uint8),
                "ff": np.zeros(4, dtype=np.float32),
            }
        return {
            "cnn": np.array(self.context.Player.environment, dtype=np.uint8),
            "ff": np.array(self.context.Player.position + self.context.Player.velocity, dtype=np.float32),
        }

    def reward(self) -> float:
        if self.context.Player.position[0] > 320:
            return 1
        return 0

    def terminated(self) -> bool:
        return self.context.Player.position[0] > 320

    def actions(self, raws_actions) -> List[Input]:
        actions = []
        if raws_actions[0] == 1:
            actions.append(GodotAction("move_left"))
        if raws_actions[1] == 1:
            actions.append(GodotAction("move_right"))
        if raws_actions[2] == 1:
            actions.append(GodotAction("jump"))
        if raws_actions[3] == 1:
            actions.append(GodotAction("run"))
        return actions

    def imitator(self) -> Imitator:
        return PlayImitator(algorithm=BC(20),
                            threshold=2,
                            collected_data_path="./tests/jump/models/play")


class PlayImitator(Imitator):

    def convert_input(self, keys) -> np.ndarray:
        actions = [0, 0, 0, 0]

        if keys[pygame.K_j]:
            actions[0] = 1
        if keys[pygame.K_l]:
            actions[1] = 1
        if keys[pygame.K_SPACE]:
            actions[2] = 1
        if keys[pygame.K_x]:
            actions[3] = 1
        return np.array(actions)


class CustomCNNExtractor(BaseFeaturesExtractor):
    def __init__(self, observation_space, features_dim=256):
        super(CustomCNNExtractor, self).__init__(observation_space, features_dim)
        n_input_channels = 1
        self.cnn = nn.Sequential(
            nn.Conv2d(n_input_channels, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
        )

        with th.no_grad():
            n_flatten = self.cnn(th.zeros(1, 1, *observation_space.shape)).view(-1).shape[0]

        self.linear = nn.Sequential(
            nn.Linear(n_flatten, features_dim),
            nn.ReLU()
        )

    def forward(self, observations):
        if observations.dim() == 3:
            observations = observations.unsqueeze(1)
        return self.linear(self.cnn(observations).view(observations.size(0), -1))


class CustomFFExtractor(BaseFeaturesExtractor):
    def __init__(self, observation_space, features_dim=128):
        super(CustomFFExtractor, self).__init__(observation_space, features_dim)
        self.linear = nn.Sequential(
            nn.Linear(observation_space.shape[0], features_dim),
            nn.ReLU(),
        )

    def forward(self, observations):
        return self.linear(observations)


class CustomCombinedExtractor(BaseFeaturesExtractor):
    def __init__(self, observation_space, cnn_obs_space, ff_obs_space, features_dim=512):
        super(CustomCombinedExtractor, self).__init__(observation_space, features_dim)

        self.cnn_extractor = CustomCNNExtractor(cnn_obs_space, features_dim=256)
        self.ff_extractor = CustomFFExtractor(ff_obs_space, features_dim=256)

        self.linear = nn.Linear(256 + 256, features_dim)

    def forward(self, observations):
        cnn_obs, ff_obs = observations['cnn'], observations['ff']
        cnn_features = self.cnn_extractor(cnn_obs)
        ff_features = self.ff_extractor(ff_obs)
        combined_features = th.cat((cnn_features, ff_features), dim=1)
        return self.linear(combined_features)
