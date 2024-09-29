from typing import List

import numpy as np
import pygame
import stable_baselines3
from gymnasium.vector.utils import spaces

from xumes import Agent, Imitable, Imitator, Input, TestStep
from xumes.modules.godot.step.godot_action import GodotEventStep
from xumes.modules.imitation_learning.bc import BC
from xumes.modules.reinforcement_learning.agent import OBST
from xumes import GodotAction, TestStep
from xumes.test_automation.given_script import SequentialStep, DelayStep, CombinedStep


class PlayAgent(Agent, Imitable):

    def __init__(self, model_path: str = None, previous_model_path: str = None, width: int = 40, height: int = 20):
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
            save_path=model_path if model_path is not None else "./tests/integration/models/play",
            previous_model_path=previous_model_path,
            eval_freq=1000,
        )

        self.width = width
        self.height = height
        self._goal_environment = np.zeros((self.width, self.height), dtype=np.uint8)
        self._player_x, self._player_y = self.width // 2, self.height // 2
        self._previous_target_x, self._previous_target_y = 0, 0
        self._previous_player_x, self._previous_player_y = self._player_x, self._player_y

    def observation(self) -> OBST:
        env = self.context.Player.environment

        self.update_environment(env)

        if not env:
            return {
                "cnn": np.zeros((self.width, self.height), dtype=np.uint8),
                "ff": np.zeros(4, dtype=np.float32),
            }
        return {
            "cnn": np.array(env, dtype=np.uint8),
            "ff": np.array(self.context.Player.position + self.context.Player.velocity, dtype=np.float32),
        }

    def update_environment(self, env):
        goal_x, goal_y = self.context.goal
        player_x, player_y = self.context.Player.tilemap_position

        diff_x = goal_x - player_x
        diff_y = goal_y - player_y

        new_target_x = self._player_x + diff_x
        new_target_y = self._player_y + diff_y

        if 0 <= new_target_x < len(env) and 0 <= new_target_y < len(env[0]):
            env[new_target_x][new_target_y] = 2
            self._previous_target_x, self._previous_target_y = new_target_x, new_target_y

    def reward(self) -> float:
        reward = 0

        if self.context.root.in_goal:
            return 1

        if self.context.root.dead:
            return -1

        goal_x, goal_y = self.context.goal
        player_x, player_y = self.context.Player.tilemap_position
        distance_to_goal = np.sqrt((goal_x - player_x) ** 2 + (goal_y - player_y) ** 2)
        previous_distance_to_goal = np.sqrt(
            (goal_x - self._previous_player_x) ** 2 + (goal_y - self._previous_player_y) ** 2)

        if distance_to_goal < previous_distance_to_goal:
            reward += 0.01
        else:
            reward -= 0.01

        self._previous_player_x, self._previous_player_y = player_x, player_y

        if abs(self.context.Player.velocity[0]) > 1:
            reward += 0.005

        return reward

    def terminated(self) -> bool:
        return self.context.root.dead or self.context.root.in_goal

    class MarioAction(TestStep):
        def __init__(self, raw_actions):
            super().__init__()
            self.raw_actions = raw_actions

        def step(self) -> List[Input]:
            steps = []
            if self.raw_actions[0] == 1:
                steps.append(SequentialStep([GodotEventStep(GodotAction("move_left"))]))
            if self.raw_actions[1] == 1:
                steps.append(GodotEventStep(GodotAction("move_right")))
                # actions.append(GodotAction("move_right"))
            if self.raw_actions[2] == 1:
                steps.append(DelayStep(GodotEventStep(GodotAction("jump")), 0))
                # actions.append(GodotAction("jump"))
            if self.raw_actions[3] == 1:
                steps.append(GodotEventStep(GodotAction("run")))
                # actions.append(GodotAction("run"))

            return CombinedStep(steps).step()

        def is_complete(self) -> bool:
            return True

        def reset(self) -> None:
            pass

    def actions(self, raw_actions) -> List[Input] | TestStep:
        return self.MarioAction(raw_actions)

        # actions = []
        # if raw_actions[0] == 1:
        #     actions.append(GodotAction("move_left"))
        # if raw_actions[1] == 1:
        #     actions.append(GodotAction("move_right"))
        # if raw_actions[2] == 1:
        #     actions.append(GodotAction("jump"))
        # if raw_actions[3] == 1:
        #     actions.append(GodotAction("run"))

        # return actions
    def imitator(self) -> Imitator:
        return PlayImitator(algorithm=BC(50),
                            threshold=2,
                            collected_data_path=self._save_path)


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
