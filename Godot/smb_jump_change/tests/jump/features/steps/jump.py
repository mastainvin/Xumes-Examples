from xumes import config, given, when, then

from tests.jump.features.steps.play_agent import PlayAgent


@config
def step_impl(context):
    context.driver.set_scene("res://tests/jump/pipe_height.tscn")


@given("A space with a pipe of size {size:d}")
def step_impl(context, size):
    context.size = size
    context.driver.set_pipe_size(size)


@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.driver.set_environment(width, height)


@when("I want to reach the other side")
def step_impl(context):
    return PlayAgent(previous_model_path="./tests/jump/models/play/bc_policy.zip", width=10, height=10)


@then("I should be able to pass the pipe if the pipe is less or equal than {max_size:d}")
def step_impl(context, max_size):
    if context.size <= max_size:
        context.assert_greater(context.Player.position[0], 320.0)
    else:
        context.assert_less(context.Player.position[0], 320.0)
