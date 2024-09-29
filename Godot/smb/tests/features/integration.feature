Feature: Jump

  @all
  Scenario Outline: Vertical jump
    Given The scene res://tests/integration/pipe_height.tscn
    And A goal at position <x1> , <y1>
    And Those platforms <platforms>
    And Those pipes <pipes>
    And The player starts at <mx> , <my>
    And An environment of size 35 x 15
    When I want to reach the goal with model : ./tests/features/models/backup/IL_RL
    Then Reach the goal without dying

    Examples:
      | x1 | y1 | mx | my | platforms                                         | pipes       |
      | 20 | 8  | 17 | 13 | [[19,9,3]]                                        | []          |
      | 8  | 8  | 11 | 13 | [[7,9,3]]                                         | []          |
      | 3  | 12 | 17 | 13 | [[2,13,3]]                                        | []          |
      | 26 | 12 | 11 | 13 | [[25,13,3]]                                       | []          |
      | 5  | 9  | 14 | 13 | [[4,10,3]]                                        | []          |
      | 23 | 9  | 14 | 13 | [[22,10,3]]                                       | []          |
      | 11 | 12 | 17 | 13 | []                                                | []          |
      | 17 | 12 | 11 | 13 | []                                                | []          |
      | 18 | 8  | 14 | 13 | []                                                | [[17,12,4]] |
      | 10 | 8  | 14 | 13 | []                                                | [[10,12,4]] |
      | 20 | 7  | 11 | 13 | [[19,8,3]]                                        | []          |
      | 8  | 7  | 17 | 13 | [[7,8,3]]                                         | []          |
      | 17 | 6  | 11 | 13 | [[13,10,3],[16,7,3]]                              | []          |
      | 11 | 6  | 17 | 13 | [[13,10,3],[10,7,3]]                              | []          |
      | 18 | 7  | 11 | 13 | [[13,12,6],[14,11,5],[15,10,4],[16,9,3],[17,8,2]] | []          |
      | 10 | 7  | 17 | 13 | [[10,12,6],[10,11,5],[10,10,4],[10,9,3],[10,8,2]] | []          |


#  @easy
#  Scenario Outline: Vertical jump Easy
#    Given A goal at position <x1> , <y1>
#    And Those platforms <platforms>
#    And Those pipes <pipes>
#    And mario at <mx> , <my>
#    And An environment of size 35 x 15
#    When I want to reach the goal with model : ./tests/features/models/backup/easy_IL_RL
#    Then Reach the goal without dying
#
#    Examples:
#      | x1 | y1 | mx | my | platforms   | pipes       |
#      | 20 | 8  | 17 | 13 | [[19,9,3]]  | []          |
#      | 8  | 8  | 11 | 13 | [[7,9,3]]   | []          |
#      | 3  | 12 | 17 | 13 | [[2,13,3]]  | []          |
#      | 26 | 12 | 11 | 13 | [[25,13,3]] | []          |
#      | 5  | 9  | 14 | 13 | [[4,10,3]]  | []          |
#      | 23 | 9  | 14 | 13 | [[22,10,3]] | []          |
#      | 11 | 12 | 17 | 13 | []          | []          |
#      | 17 | 12 | 11 | 13 | []          | []          |
#      | 18 | 8  | 14 | 13 | []          | [[17,12,4]] |
#      | 10 | 8  | 14 | 13 | []          | [[10,12,4]] |
#
#  @hard
#  Scenario Outline: Vertical jump Hard
#    Given A goal at position <x1> , <y1>
#    And Those platforms <platforms>
#    And Those pipes <pipes>
#    And mario at <mx> , <my>
#    And An environment of size 35 x 15
#    When I want to reach the goal with model : ./tests/features/models/backup/hard_RL
#    Then Reach the goal without dying
#
#    Examples:
#      | x1 | y1 | mx | my | platforms                                         | pipes |
#      | 20 | 7  | 11 | 13 | [[19,8,3]]                                        | []    |
#      | 8  | 7  | 17 | 13 | [[7,8,3]]                                         | []    |
#      | 17 | 6  | 11 | 13 | [[13,10,3],[16,7,3]]                              | []    |
#      | 11 | 6  | 17 | 13 | [[13,10,3],[10,7,3]]                              | []    |
#      | 18 | 7  | 11 | 13 | [[13,12,6],[14,11,5],[15,10,4],[16,9,3],[17,8,2]] | []    |
#      | 10 | 7  | 17 | 13 | [[10,12,6],[10,11,5],[10,10,4],[10,9,3],[10,8,2]] | []    |
#
## Too hard (1 bad exemple collected (mistake), need to train a special model for this one.
##      | 29 | 12 | 10 | 13 | [[28,13,3]]                                       | []    |

