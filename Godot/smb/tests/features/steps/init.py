from xumes import given


@given("The scene {scene:s}")
def step_impl(context, scene):
    context.engine_driver.set_scene(scene)