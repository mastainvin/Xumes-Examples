Feature: End 2 End

  Scenario: 1
    Given The map 2p_cityscape
    When The player moves a unit
    Then The unit is at the desired position

