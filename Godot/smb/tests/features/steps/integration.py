from xumes import config, given, when, then

from tests.features.steps.play_agent import PlayAgent


@config
def step_impl(context):
    context.driver.set_scene("res://tests/integration/pipe_height.tscn")


@given("A goal at position {x:d} , {y:d}")
def step_impl(context, x, y):
    context.goal = (x, y)
    context.driver.set_goal(x, y)


@given("Those platforms {platforms:list}")
def step_impl(context, platforms):
    for x, y, size in platforms:
        context.driver.set_platform(x, y, size)


@given("Those pipes {pipes:list}")
def step_impl(context, pipes):
    for x, y, size in pipes:
        context.driver.set_pipe(x, y, size)


@given("mario at {x:d} , {y:d}")
def step_impl(context, x, y):
    context.driver.set_mario_position(x, y)


@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.driver.set_environment(width, height)


@when("I want to reach the goal with model : {model:s}")
def step_impl(context, model):
    return PlayAgent(model_path=model, width=35, height=15)


@then("Reach the goal without dying")
def step_impl(context):
    context.assert_true(context.in_goal)
    context.assert_false(context.dead)
