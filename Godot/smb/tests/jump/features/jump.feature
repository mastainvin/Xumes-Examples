Feature: Jump

  @test
  Scenario Outline: Pipe size
    Given A space with a pipe of size <size>
    And An environment of size 10 x 10
    When I want to reach the other side
    Then I should be able to pass the pipe if the pipe is less or equal than 5
    Examples:
        | size |
        | 0    |
        | 2    |
        | 5    |
        | 6    |


  @manual
    Scenario: Pipe size
        Given A space with a pipe of size 3
        And An environment of size 25 x 25
        When I want to reach the other side
        Then I should be able to pass the pipe if the pipe is less or equal than 5

  @collect
  Scenario Outline: Pipe size
    Given A space with a pipe of size <size>
    And An environment of size 10 x 10
    When I want to reach the other side
    Then I should be able to pass the pipe if the pipe is less or equal than 5
    Examples:
        | size |
        | 0    |
        | 2    |
        | 5    |
