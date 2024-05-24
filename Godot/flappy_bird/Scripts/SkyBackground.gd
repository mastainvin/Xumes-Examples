extends TextureRect


func _ready():
	GameManager.bird_crashed.connect(_on_bird_crashed)
	
	material.set_shader_parameter("speed", 0.2)


func _on_bird_crashed():
	material.set_shader_parameter("speed", 0.0)
