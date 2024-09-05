from xumes import config, given, when, then

from tests.jump.features.steps.play_agent import PlayAgent


@config
def step_impl(context):
    context.driver.set_scene("res://tests/level_1/test_level_1.tscn")

@given("The player starts at {p_x:d} , {p_y:d}")
def step_impl(context, p_x, p_y):
    context.driver.set_mario_position(p_x, p_y)

@given("The goal is at {g_x:d} , {g_y:d}")
def step_impl(context, g_x, g_y):
    context.goal = (g_x , g_y)
    context.driver.set_goal(g_x, g_y)


@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.driver.set_environment(width, height)


@when("I want to reach the goal with model : {model:s}")
def step_impl(context, model):
    return PlayAgent(previous_model_path=model + "/bc_policy", model_path=model, width=35, height=15)


@then("Reach the goal without dying")
def step_impl(context):
    context.assert_true(context.in_goal)
    context.assert_false(context.dead)