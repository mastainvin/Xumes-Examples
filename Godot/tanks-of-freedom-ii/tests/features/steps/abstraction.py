from xumes import GodotJoyKey, WaitStep, WaitUntilStep, SequentialStep, RepeatUntilStep, \
    GodotJoyActionStep, GodotEventStep, GodotAction
from xumes.test_automation.given_script import LogStep

from tests.features.steps.helpers import get_unit_positions
from tests.features.steps.state import MoveToTileState


class MoveUnit(SequentialStep):

    def __init__(self, color, unit_type, origin_pos, destination_pos):
        self._origin_pos = tuple(origin_pos)
        self._destination_pos = tuple(destination_pos)
        super().__init__(states=[
            # Move to unit
            MoveToTileState(tile=self._origin_pos, threshold=1.0),
            WaitStep(wait_time=10),

            # Select unit
            GodotEventStep(GodotAction("ui_accept")),
            WaitStep(wait_time=10),

            # Move to free tile
            MoveToTileState(tile=self._destination_pos, threshold=1.0),
            WaitStep(wait_time=10),

            # Move unit to that tile
            GodotEventStep(GodotAction("ui_accept")),
            WaitUntilStep(timeout=100,
                          wait_function=lambda: self._destination_pos in get_unit_positions(
                              self.context.root.units,
                              unit_type,
                              color)),
            GodotJoyActionStep(action_key=GodotJoyKey.B),
        ])


class FinishTurn(SequentialStep):

    def __init__(self):
        super().__init__(states=[
            RepeatUntilStep(
                step=GodotEventStep(GodotAction("end_turn")),
                wait_function=lambda: self.context.root.current_player_changed,
                timeout=10000
            ),
            WaitStep(10),
            GodotJoyActionStep(action_key=GodotJoyKey.B),
        ])


class Attack(SequentialStep):

    def __init__(self, attack_pos, enemy_pos):
        super().__init__(states=[
            # Select attack position
            MoveToTileState(tile=tuple(attack_pos), threshold=1.0),
            WaitStep(wait_time=10),

            # Select unit
            GodotJoyActionStep(action_key=GodotJoyKey.A),
            WaitStep(wait_time=10),

            # Select enemy pos
            MoveToTileState(tile=tuple(enemy_pos), threshold=1.0),
            WaitStep(wait_time=10),

            # Select unit
            GodotJoyActionStep(action_key=GodotJoyKey.A),
            WaitStep(wait_time=10),
        ])
