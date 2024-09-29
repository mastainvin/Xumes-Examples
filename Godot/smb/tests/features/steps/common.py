from xumes import TestContext, given, when, then

from tests.features.steps.play_agent import PlayAgent


@given("The player starts at {p_x:d} , {p_y:d}")
def step_impl(context: TestContext, p_x, p_y):
    context.instance_driver.set_mario_position(p_x, p_y)

@given("A goal at position {x:d} , {y:d}")
def step_impl(context, x, y):
    context.goal = (x, y)
    context.instance_driver.set_goal(x, y)

@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.instance_driver.set_environment(width, height)

@when("I want to reach the goal with model : {model:s}")
def step_impl(context, model):
    return PlayAgent(model_path=model, width=35, height=15)

@then("Reach the goal without dying")
def step_impl(context):
    context.assert_true(context.root.in_goal)
    context.assert_false(context.root.dead)
