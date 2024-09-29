Feature: End 2 End

  @move
  Scenario: Good move
    Given The scene res://tests/end2end.tscn
    And The map 2p_cityscape
    When The green player moves the TR_M_INF unit from [184,4,104] to [176,4,136]
    Then The unit is  at the desired position

  @move
  Scenario: Too far move
    Given The scene res://tests/end2end.tscn
    And The map 2p_cityscape
    When The green player moves the TR_M_INF unit from [184,4,104] to [160,4,136]
    Then The unit is not at the desired position

  @unit
  Scenario: Create a new unit
    Given The scene res://tests/end2end.tscn
    And The map 2p_cityscape
    When The green player creates a TR_INFANTRY unit at [200,4,104] with the building at [192,4,104]
    Then The unit is  at the desired position


  @combat
  Scenario: Combat
    Given The scene res://tests/end2end.tscn
    And The map 2p_cityscape
    And combat position
    When combat
    Then green TR_M_INF is dead