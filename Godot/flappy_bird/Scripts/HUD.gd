extends Control


func _ready():
	GameManager.game_started.connect(_on_game_started)
	GameManager.bird_crashed.connect(_on_bird_crashed)
	GameManager.point_scored.connect(_on_point_scored)
	
	$Score.visible = false


func _on_game_started():
	$Score.visible = true
	$Score.text = "0"


func _on_point_scored():
	$Score.text = str(GameManager.score)


func _on_bird_crashed():
	$Score.visible = false
