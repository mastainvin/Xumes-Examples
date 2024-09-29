from typing import List

from xumes import given, GodotEventStep, GodotAction, TestStep, Input
from xumes.test_automation.test_context import TestContext


@given("Those platforms {platforms:list}")
def step_impl(context, platforms):
    for x, y, size in platforms:
        context.instance_driver.set_platform(x, y, size)

class GoCenterStep(TestStep):

    def step(self) -> List[Input]:
        return [GodotAction("move_left"), GodotAction("jump")]

    def is_complete(self):
        return self.context.Player.tilemap_position[0] <= 14

    def reset(self):
        pass


@given("Those pipes {pipes:list}")
def step_impl(context: TestContext, pipes):
    for x, y, size in pipes:
        context.instance_driver.set_pipe(x, y, size)
   #  context.add_step(GoCenterStep())



