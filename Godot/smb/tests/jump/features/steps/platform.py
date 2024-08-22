from xumes import config, given, when, then

from tests.jump.features.steps.play_agent import PlayAgent


@config
def step_impl(context):
    context.driver.set_scene("res://tests/jump/pipe_height.tscn")


@given("A goal platform at position {x:d} , {y:d} of size {size:d}")
def step_impl(context, x, y, size):
    context.driver.set_platform(x, y, size)
    context.goal = (x + size // 2, y - 1)
    context.driver.set_goal(x + size // 2, y-1)

@given("mario at {x:d} , {y:d}")
def step_impl(context, x, y):
    context.driver.set_mario_position(x, y)

@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.driver.set_environment(width, height)


@when("I want to reach the goal")
def step_impl(context):
    return PlayAgent(previous_model_path="./tests/jump/models/play/bc_policy.zip", width=35, height=15)


@then("Reach the goal without dying")
def step_impl(context):
    context.assert_true(context.in_goal)
    context.assert_false(context.dead)