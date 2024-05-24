extends Control

@export var bronze : Texture
@export var platinum : Texture
@export var gold : Texture

@onready var last_best_score = SaveFile.best_score


func _ready():
	GameManager.game_started.connect(_on_game_started)
	GameManager.bird_crashed.connect(_on_bird_crashed)
	
	$Countdown/GetReady.visible = false
	$GameOver.visible = false


func _on_game_started():
	$Title.visible = false
	$Countdown/Instructions.visible = false
	$Countdown/GetReady.visible = true
	$Countdown/CountdownTimer.start()


func _on_bird_crashed():
	$Countdown.visible = false
	$GameOver.visible = true
	
	$GameOver/Panel/Score.text = str(GameManager.score)
	$GameOver/Panel/BestScore.text = str(SaveFile.best_score)
	
	show_medal()


func _on_countdown_timer_timeout():
	$Countdown.visible = false


func _on_play_button_pressed():
	get_tree().reload_current_scene()
	GameManager.is_game_started = false


func show_medal():
	if GameManager.score > last_best_score:
		$GameOver/Panel/Medal.texture = gold
	elif GameManager.score == SaveFile.best_score:
		$GameOver/Panel/Medal.texture = platinum
	elif GameManager.score < SaveFile.best_score:
		$GameOver/Panel/Medal.texture = bronze
