import numpy as np
import pygame
import stable_baselines3
from gymnasium import spaces

from xumes import Agent, Imitator, LambdaImitator
from xumes import GodotAction
from xumes import Imitable
from xumes.modules.imitation_learning.bc import BC


class Fly(Agent, Imitable):

    def __init__(self, model_path: str = None, previous_model_path: str = None):
        super().__init__(
            observation_space=spaces.Dict({
                "velocity": spaces.Box(low=-float('inf'), high=300, shape=(2,), dtype=np.float32),
                "X": spaces.Box(low=-float('inf'), high=float('inf'), shape=(1,), dtype=np.float32),
                "Y": spaces.Box(low=-float('inf'), high=float('inf'), shape=(1,), dtype=np.float32),
                "Y1": spaces.Box(low=-float('inf'), high=float('inf'), shape=(1,), dtype=np.float32),
            }),
            action_space=spaces.Discrete(2),
            max_episode_length=1000,
            total_timesteps=int(3_000_000),
            algorithm_type="MultiInputPolicy",
            algorithm=stable_baselines3.PPO,
            save_path=model_path if model_path is not None else "./Tests/PipeSizeTest/models/fly",
            previous_model_path=previous_model_path,
            eval_freq=10000,
        )

        self.points = 0

    def observation(self):
        velocity = self.context.Bird.velocity
        return {
            "velocity": np.array(velocity, dtype=np.float32),
            "X": np.array([self.context.root.X], dtype=np.float32),
            "Y": np.array([self.context.root.Y], dtype=np.float32),
            "Y1": np.array([self.context.root.Y1], dtype=np.float32)
        }

    def reward(self):
        if self.context.root.score > self.points:
            self.points = self.context.root.score
            return 1

        if self.context.root.dead or self.context.Bird.position[1] < 0:
            return -1
        return 0

    def terminated(self):
        terminated = self.context.root.dead != 0 or self.context.root.score >= 2 or self.context.Bird.position[1] < 0
        if terminated:
            self.points = 0
        return terminated

    def actions(self, raw_actions):
        if raw_actions == 1:
            return [GodotAction("jump")]
        return []

    def imitator(self) -> Imitator:
        return LambdaImitator(algorithm=BC(20),
                              threshold=2,
                              collected_data_path="./Tests/PipeSizeTest/models/fly",
                              convert_input=lambda keys: np.array([1]) if keys[pygame.K_SPACE] else np.array([0]))

