Feature: Random Level Generation for Mario Game

  Scenario: Generate a random level with a goal, platforms, and Mario's position
    Given An environment of size 35 x 15
    And Mario at a random position
    And A random goal
    And Random platforms
    When I want to reach the goal
    Then Reach the goal without dying