from xumes import config, given, when, then

from Tests.PipeSizeTest.features_imitation_learning.steps.fly_imitator import Fly


@config
def config(context):
    context.driver.set_scene("res://Tests/PipeSizeTest/PipeSizeTest.tscn")


@given("first pipe at {i:f} and second pipe at {j:f}")
def step_impl(context, i, j):
    context.driver.set_pipes_position(i, j)


@when("bird flies using {path:s} model")
def step_impl(context, path):
    if path == "new":
        return Fly()
    return Fly(previous_model_path=path)


@then("bird should have passed {i:d} pipes")
def step_impl(context, i):
    context.assert_true(context.score >= i)
