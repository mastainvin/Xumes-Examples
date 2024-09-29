from xumes import given, when, TestContext, GodotJoyAxis, GodotJoyActionStep
from xumes import GodotJoyKey, WaitStep, WaitUntilStep, DelayStep, GodotJoyToDirectionStep, CombinedStep, GodotAction, GodotEventStep

from tests.features.steps.helpers import get_unit_positions
from tests.features.steps.state import MoveToTileState, End2EndScript


@when(
    "The {color:s} player creates a {unit_type:s} unit at {destination_pos:list} with the building at {build_pos:list}")
def test_impl(context, color, unit_type, destination_pos, build_pos):
    context.destination_pos = tuple(destination_pos)
    context.build_pos = tuple(build_pos)
    context.unit_type = unit_type
    context.color = color

    return End2EndScript(states=[
        # Move to building
        MoveToTileState(tile=context.build_pos, threshold=1.0),
        WaitStep(wait_time=10),

        # Select building
        GodotEventStep(GodotAction("ui_accept")),
        WaitStep(wait_time=10),

        # Select unit in menu
        CombinedStep(states=[
            DelayStep(GodotEventStep(GodotAction("ui_accept")), 5),
            GodotJoyToDirectionStep(joy_axis=GodotJoyAxis.LEFT_X, value=1.0, duration=15)
        ]),
        WaitStep(wait_time=10),

        # Move to free tile
        MoveToTileState(tile=context.destination_pos, threshold=1.0),
        WaitStep(wait_time=10),

        # Move unit to that tile
        GodotEventStep(GodotAction("ui_accept")),
        WaitUntilStep(timeout=100,
                       wait_function=lambda: context.destination_pos in get_unit_positions(context.root.units,
                                                                                           context.unit_type,
                                                                                           context.color)),
    ])
