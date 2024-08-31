Feature: Test the first level


  Scenario Outline:
    Given The player starts at <p_x> , <p_y>
    And The goal is at <g_x> , <g_y>
    And An environment of size 35 x 15
    When I want to reach the goal
    Then Reach the goal without dying

    Examples:
      | p_x | p_y | g_x | g_y |
      | 5   | 12  | 15  | 12  |
      | 22  | 12  | 29  | 10  |
      | 33  | 12  | 29  | 9   |
      | 38  | 9   | 47  | 8   |
      | 65  | 12  | 73  | 12  |
# FAIL Deux étapes
      | 74  | 12  | 81  | 4   |
# Pass
      | 81  | 4   | 92  | 4   |
# Fail
      | 83  | 12  | 91  | 12  |
# Fail
      | 118 | 8   | 124 | 4   |
# Fail
      | 122 | 4   | 138 | 4   |
# Fail
      | 132 | 12  | 137 | 8   |
      | 176 | 12  | 189 | 4   |