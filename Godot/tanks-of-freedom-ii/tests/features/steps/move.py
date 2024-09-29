from xumes import when, GodotJoyKey, WaitStep, WaitUntilStep, GodotJoyActionStep, GodotEventStep, GodotAction

from tests.features.steps.helpers import get_unit_positions
from tests.features.steps.state import MoveToTileState,End2EndScript


@when("The {color:s} player moves the {unit_type:s} unit from {origin_pos:list} to {destination_pos:list}")
def test_impl(context, color, unit_type, origin_pos, destination_pos):
    context.origin_pos = tuple(origin_pos)
    context.destination_pos = tuple(destination_pos)
    context.unit_type = unit_type
    context.color = color

    return End2EndScript(states=[
        # Move to Unit
        MoveToTileState(tile=context.origin_pos, threshold=1.0),
        WaitStep(wait_time=10),

        # Select unit
        GodotEventStep(GodotAction("ui_accept")),
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
