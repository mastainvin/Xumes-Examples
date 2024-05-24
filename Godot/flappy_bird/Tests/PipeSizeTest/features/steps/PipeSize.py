import numpy as np
import stable_baselines3
from gymnasium.vector.utils import spaces

from xumes import Agent, given, when, then, config


@config
def config(context):
    context.driver.set_scene("res://Tests/PipeSizeTest/PipeSizeTest.tscn")


@given("first pipe at {i:f} and second pipe at {j:f}")
def step_impl(context, i, j):
    context.driver.set_pipes_position(i, j)


@when("bird flies")
def step_impl(context):
    return Fly()


@then("bird should have passed {i:d} pipes")
def step_impl(context, i):
    context.assert_true(context.score >= i)


class Fly(Agent):

    def __init__(self):
        super().__init__(
            observation_space=spaces.Dict({
                "velocity": spaces.Box(-float('inf'), 300, shape=(2,), dtype=float),
                "X": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
                "Y": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
                "Y1": spaces.Box(-float('inf'), float('inf'), shape=(1,), dtype=float),
            }),
            action_space=spaces.Discrete(2),
            max_episode_length=1000,
            total_timesteps=int(1_000_000),
            algorithm_type="MultiInputPolicy",
            algorithm=stable_baselines3.PPO,
            save_path="./models/fly",
            eval_freq=10000,
            )

        self.points = 0

    def observation(self):
        velocity = self.Game.Bird.velocity
        return {"velocity": np.array(velocity), "X": np.array(self.X), "Y": np.array(self.Y), "Y1": np.array(self.Y1)}

    def reward(self):
        if self.score > self.points:
            self.points = self.score
            if self.points >= 2:
                return 10
            return 1

        if self.dead or self.Game.Bird.position[1] < 0:
            return -1000
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
