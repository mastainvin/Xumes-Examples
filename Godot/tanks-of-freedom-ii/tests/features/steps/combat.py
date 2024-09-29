from xumes import given, when, then

from tests.features.steps.abstraction import MoveUnit, FinishTurn, Attack
from tests.features.steps.helpers import is_dead
from tests.features.steps.state import End2EndScript


@given("combat position")
def step_impl(context):
    green = "green"
    blue = "blue"
    unit_type = "TR_M_INF"

    context.add_step(MoveUnit(green, unit_type, [184, 4, 104], [160, 4, 128]))
    context.add_step(FinishTurn())
    context.add_step(MoveUnit(blue, unit_type, [104, 4, 184], [128, 4, 160]))
    context.add_step(FinishTurn())
    context.add_step(MoveUnit(green, unit_type, [160, 4, 128], [136, 4, 152]))
    context.add_step(FinishTurn())
    context.add_step(MoveUnit(blue, unit_type, [128, 4, 160], [128, 4, 152]))


@when("combat")
def step_impl(context):
    return End2EndScript(states=[
        Attack([128, 4, 152], [136, 4, 152]),
        FinishTurn(),
        Attack([136, 4, 152], [128, 4, 152]),
    ])

@then("{color:s} {unit_type:s} is dead")
def step_impl(context, color, unit_type):
    context.assert_true(is_dead(context.root.units, color, unit_type))