import math
from typing import List

from xumes import given, when, then, config, Script, Input, GodotJoyMotion, GodotJoyAxis, GodotJoyButton, GodotJoyKey


@config
def test_impl(context):
    context.driver.set_scene("res://tests/end2end.tscn")


@given("The map {map_name:s}")
def test_impl(context, map_name):
    context.driver.set_map(map_name)


@when("The player moves a unit")
def test_impl(context):
    return End2EndScript(states=[
        MoveToGoalState(goal=(184, 4, 104), threshold=1.0),
        WaitState(wait_time=10),
        PerformActionState(action_key=GodotJoyKey.A)
    ])


@then("The unit is at the desired position")
def test_impl(context):
    pass


class State:
    def __init__(self):
        self.script = None

    @property
    def context(self):
        return self.script.context

    def step(self) -> List[Input]:
        raise NotImplementedError()

    def is_complete(self) -> bool:
        return True


class MoveToGoalState(State):
    def __init__(self, goal, threshold=1.0):
        super().__init__()
        self.goal = goal
        self.threshold = threshold

    def step(self) -> List[Input]:
        actions = []

        x_tile_box, _, y_tile_box = self.context.tile_box.position
        x_goal, _, y_goal = self.goal
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
        x_goal, _, y_goal = self.goal
        x_diff = x_goal - x_tile_box
        y_diff = y_goal - y_tile_box
        return abs(x_diff) < self.threshold and abs(y_diff) < self.threshold


class PerformActionState(State):
    def __init__(self, action_key):
        super().__init__()
        self.action_key = action_key
        self.action_performed = False

    def step(self) -> List[Input]:
        actions = []
        if not self.action_performed:
            actions.append(GodotJoyButton(self.action_key))
            self.action_performed = True
        return actions

    def is_complete(self) -> bool:
        return self.action_performed


class WaitState(State):
    def __init__(self, wait_time):
        super().__init__()
        self.wait_time = wait_time
        self.elapsed_time = 0

    def step(self) -> List[Input]:
        self.elapsed_time += 1
        return []

    def is_complete(self) -> bool:
        return self.elapsed_time >= self.wait_time


class End2EndScript(Script):
    def __init__(self, states: List[State]):
        super().__init__()
        self.states = states
        for state in states:
            state.script = self

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
