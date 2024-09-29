from xumes import when, then
from xumes.test_automation.test_context import TestContext

from tests.features.steps.state import End2EndScript


@when("pass")
def step_impl(context):
    return End2EndScript(states=[])

@when("wait")
def step_impl(context):

    class Wait(End2EndScript):

        def terminated(self):
            return False
    return Wait(states=[])


@then("pass")
def step_impl(context: TestContext):
    context.assert_true(True)