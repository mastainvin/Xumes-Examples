Feature: Test the first level


  Scenario Outline:
    Given The player starts at <p_x> , <p_y>
    And The goal is at <g_x> , <g_y>
    And An environment of size 35 x 15
    When I want to reach the goal with model : ./tests/features/models/backup/level_1_RL
    Then Reach the goal without dying

    Examples:
      | p_x | p_y | g_x | g_y |
      | 5   | 12  | 15  | 12  |
      | 22  | 12  | 29  | 10  |
      | 33  | 12  | 38  | 9   |
      | 38  | 9   | 47  | 8   |
      | 65  | 12  | 73  | 12  |
      | 74  | 12  | 81  | 4   |
      | 81  | 4   | 92  | 4   |
      | 83  | 12  | 91  | 12  |
      | 118 | 8   | 121 | 4   |
      | 122 | 4   | 129 | 4   |
      | 132 | 12  | 137 | 8   |
      | 176 | 12  | 189 | 4   |