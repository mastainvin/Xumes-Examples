import random
from typing import List

import numpy as np

from xumes import Script
from xumes import Input

from xumes import GodotAction

from Tests.root.features_imitation_learning.steps.fly_lambda_imitator import Fly


class FlyScript(Script):

    def __init__(self):
        super().__init__()
        self.model = Fly(model_path="./Tests/PipeSizeTest/models/fly")
        self.model2 = Fly(model_path="./Tests/PipeSizeTest/models/fly")

    def step(self) -> List[Input]:

        # One in ten times, the bird jumps randomly
        if random.random() < 0.1:
            if random.random() < 0.5:
                return [GodotAction("jump")]
            return []
        observation = self.observation()

        # use 2 different models to predict the action
        if self.context.score % 2 == 0:
            action = self.model2.predict(observation)
        else:
            action = self.model.predict(observation)

        # convert the action to the game action
        if action == 1:
            return [GodotAction("jump")]

        return []

    def observation(self):
        # convert the game state to an observation
        velocity = self.context.Bird.velocity
        return {"velocity": np.array(velocity, dtype=float),
                "X": np.array([self.context.root.X], dtype=float),
                "Y": np.array([self.context.root.Y], dtype=float),
                "Y1": np.array([self.context.root.Y1], dtype=float)}

    def terminated(self):
        return self.context.root.dead != 0 or self.context.root.score >= 2 or self.context.Bird.position[1] < 0
