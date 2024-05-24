extends RayCast2D

var distance: float = 0.0

func _process(delta: float) -> void:
	global_rotation = 0
	distance = global_position.distance_to(get_collision_point())
	
