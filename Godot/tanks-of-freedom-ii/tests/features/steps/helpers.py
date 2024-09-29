from typing import List, Dict


def get_unit_positions(units_list: List[Dict], unit_type, player_color):
    positions = []
    for unit in units_list:
        if unit["type"] == unit_type and unit["side"] == player_color:
            positions.append(unit["position"])
    return positions

def is_dead(units_list: List[Dict], unit_type, player_color):
    for unit in units_list:
        if unit["type"] == unit_type and unit["side"] == player_color:
            return False

    return True