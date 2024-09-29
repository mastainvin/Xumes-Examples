from xumes import given


@given("The scene {scene:s}")
def step_impl(context, scene):
    context.engine_driver.set_scene(scene)


@given("The map {map_name:s}")
def test_impl(context, map_name):
    context.instance_driver.set_map(map_name)
