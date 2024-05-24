extends Node2D
class_name Pipes

var speed : float:
	get:
		return speed
	set(value):
		speed = value


func _process(delta):
	position.x -= speed * delta


func _on_point_area_body_exited(body):
	if body is Bird:
		if not GameManager.is_game_ended:
			GameManager.point_scored.emit()


func _on_visible_on_screen_notifier_2d_screen_exited():
	queue_free()


func _on_top_pipe_body_entered(body):
	if body is Bird:
		GameManager.bird_crashed.emit()


func _on_bottom_pipe_body_entered(body):
	if body is Bird:
		GameManager.bird_crashed.emit()
