from xumes import config, given, when, then

from Tests.PipeSizeTest.features_script.steps.fly_script import FlyScript


@config
def config(context):
    context.driver.set_scene("res://Tests/PipeSizeTest/PipeSizeTest.tscn")


@given("first pipe at {i:f} and second pipe at {j:f}")
def step_impl(context, i, j):
    context.driver.set_pipes_position(i, j)


@when("bird flies")
def step_impl(context):
    return FlyScript()


@then("bird should have passed {i:d} pipes")
def step_impl(context, i):
    context.assert_true(context.root.score >= i)
