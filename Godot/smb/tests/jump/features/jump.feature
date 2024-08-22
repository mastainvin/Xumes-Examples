Feature: Jump


  @jump
  Scenario Outline: Vertical jump
    Given A goal platform at position <x1> , <y1> of size <size>
    And mario at <mx> , <my>
    And An environment of size 35 x 15
    When I want to reach the goal
    Then Reach the goal without dying

    Examples:
    | x1 | y1 | size | mx | my |
    | 17 | 2  | 3    | 9  | 7  |
#    | 17 | 3  | 3    | 15 | 7  |
#    | 5  | 2  | 3    | 15 | 7  |
#    | 5  | 3  | 3    | 9  | 7  |
#    | 26 | 7  | 2    | 8  | 7  |
#    | 1  | 7  | 2    | 15 | 7  |
#    | 2  | 4  | 3    | 12 | 7  |
#    | 20 | 4  | 3    | 12 | 7  |
#    | 2  | 10 | 3    | 9 | 7  |
#    | 5  | 10 | 3    | 9 | 7  |
#    | 17 | 10 | 3    | 15 | 7  |
#    | 20 | 10 | 3    | 15 | 7  |
#    | 8  | 7  | 3    | 15 | 7  |
#    | 14 | 7  | 3    | 9  | 7  |