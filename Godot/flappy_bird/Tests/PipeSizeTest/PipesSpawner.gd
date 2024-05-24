extends PipesSpawner

func _on_spawn_timer_timeout():
	var y = $"/root/PipeSizeTest".get_next_position()
	var viewport_rect = get_viewport().get_camera_2d().get_viewport_rect()
	spawn_pipes_position(0, get_y_from_percents(y))
	
func remove_pipes():
	for pipe in get_children().filter(func (child): return child is Pipes):
		(pipe as Pipes).queue_free()
