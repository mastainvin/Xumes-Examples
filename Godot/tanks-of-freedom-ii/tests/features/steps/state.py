import math
from typing import List

from xumes import Input, GodotJoyMotion, GodotJoyAxis, Script
from xumes import TestStep

JOY_LEFT = "left"
JOY_RIGHT = "right"


class MoveToTileState(TestStep):
    def __init__(self, tile, threshold=1.0):
        super().__init__()
        self.goal_tile = tile
        self.threshold = threshold

    def step(self) -> List[Input]:
        actions = []
        x_tile_box, _, y_tile_box = self.context.tile_box.position
        x_goal, _, y_goal = self.goal_tile
        x_diff = x_goal - x_tile_box
        y_diff = y_goal - y_tile_box

        norm = math.sqrt(x_diff ** 2 + y_diff ** 2)

        if norm != 0:
            x_diff_norm = x_diff / norm
            y_diff_norm = y_diff / norm
        else:
            x_diff_norm = 0
            y_diff_norm = 0

        cos_45 = math.cos(math.radians(45))
        sin_45 = math.sin(math.radians(45))

        x_iso = x_diff_norm * cos_45 - y_diff_norm * sin_45
        y_iso = x_diff_norm * sin_45 + y_diff_norm * cos_45

        if x_iso != 0:
            actions.append(GodotJoyMotion(GodotJoyAxis.LEFT_X, x_iso))

        if y_iso != 0:
            actions.append(GodotJoyMotion(GodotJoyAxis.LEFT_Y, y_iso))

        return actions

    def is_complete(self) -> bool:
        x_tile_box, _, y_tile_box = self.context.tile_box.position
        x_goal, _, y_goal = self.goal_tile
        x_diff = x_goal - x_tile_box
        y_diff = y_goal - y_tile_box
        return abs(x_diff) < self.threshold and abs(y_diff) < self.threshold

    def reset(self):
        pass

class End2EndScript(Script):
    def __init__(self, states: List[TestStep]):
        super().__init__()
        self.states = states
        for state in states:
            state.set_has_context(self)

        self.current_state_index = 0

    def step(self) -> List[Input]:
        if self.current_state_index >= len(self.states):
            return []

        current_state = self.states[self.current_state_index]
        actions = current_state.step()

        if current_state.is_complete():
            self.current_state_index += 1

        return actions

    def terminated(self) -> bool:
        return self.current_state_index >= len(self.states)
