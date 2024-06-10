import numpy as np
import stable_baselines3
from gymnasium import spaces
from xumes import Agent


class Fly(Agent):

    def __init__(self):
        super().__init__(
            observation_space=spaces.Dict({
                "velocity": spaces.Box(-float('inf'), float('inf'), shape=(2,), dtype=float),
                "X": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
                "Y": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
                "Y1": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
            }),
            action_space=spaces.Discrete(2),
            max_episode_length=1000,
            total_timesteps=int(3_000_000),
            algorithm_type="MultiInputPolicy",
            algorithm=stable_baselines3.PPO,
            save_path="./Tests/PipeSizeTest/models/fly",
            eval_freq=10000,
            )

        self.points = 0

    def observation(self):
        velocity = self.Game.Bird.velocity
        return {"velocity": np.array(velocity, dtype=float), "X": np.array([self.X], dtype=float), "Y": np.array([self.Y], dtype=float), "Y1": np.array([self.Y1], dtype=float)}

    def reward(self):
        if self.score > self.points:
            self.points = self.score
            return 1

        if self.dead or self.Game.Bird.position[1] < 0:
            return -1
        return 0

    def terminated(self):
        terminated = self.dead != 0 or self.score >= 2 or self.Game.Bird.position[1] < 0
        if terminated:
            self.points = 0
        return terminated

    def actions(self, raw_actions):
        if raw_actions == 1:
            return [{"type": "ACTION_EVENT", "action_name": "jump"}]
        return []
