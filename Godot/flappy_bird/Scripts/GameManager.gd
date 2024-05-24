extends Node

signal game_started
signal point_scored
signal bird_crashed

var is_game_started : bool = false
var is_game_ended : bool = false
var score : int = 0


func _ready():
	game_started.connect(_on_game_started)
	point_scored.connect(_on_point_scored)
	bird_crashed.connect(_on_bird_crashed)


func _on_game_started():
	is_game_started = true
	is_game_ended = false
	
	score = 0


func _on_point_scored():
	score += 1


func _on_bird_crashed():
	is_game_ended = true
	
	if score > SaveFile.best_score:
		SaveFile.best_score = score
		SaveFile.save_game()
		print(SaveFile.best_score)
