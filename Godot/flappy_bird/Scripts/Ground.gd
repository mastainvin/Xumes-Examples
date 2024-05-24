extends StaticBody2D


func _ready():
	GameManager.bird_crashed.connect(_on_bird_crashed)
	
	$Sprite2D.material.set_shader_parameter("speed", 0.2)


func _on_bird_crashed():
	$Sprite2D.material.set_shader_parameter("speed", 0.0)


func _on_area_2d_body_entered(body):
	if body is Bird:
		GameManager.bird_crashed.emit()
