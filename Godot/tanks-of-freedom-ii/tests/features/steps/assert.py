from xumes import then

from tests.features.steps.helpers import get_unit_positions


@then("The unit is {is_not:s} at the desired position")
def test_impl(context, is_not):
    unit_positions = get_unit_positions(context.root.units, context.unit_type, context.color)
    if is_not == "":
        context.assert_true(context.destination_pos in unit_positions)
    else:
        context.assert_true(context.origin_pos in unit_positions)
