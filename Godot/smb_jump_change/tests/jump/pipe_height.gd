extends FeatureNode

@onready
var tilemap: TileMap = $TileMap

@onready
var player: TestPlayer = $Player

func set_pipe_size(size: int):
	if size > 0:
		resize_pipe(Vector2(12, 12), size, Vector2(7,4),  Vector2(8,4), Vector2(7,5), Vector2(8,5))
	
func set_environment(width: int, height: int):
	player.set_environment(width, height)
	
func resize_pipe(base_coords: Vector2, height: int,
				 top_left_atlas_coords: Vector2i, top_right_atlas_coords: Vector2i,
				 bottom_left_atlas_coords: Vector2i, bottom_right_atlas_coords: Vector2i):
	var source_id = 0  

	# Base
	for i in range(height - 1):
		var current_pos = base_coords - Vector2(0, i)
		tilemap.set_cell(0, current_pos, source_id, bottom_left_atlas_coords)
		tilemap.set_cell(0, current_pos + Vector2(1, 0), source_id, bottom_right_atlas_coords)

	# Summit
	var top_pos = base_coords - Vector2(0, height - 1)
	tilemap.set_cell(0, top_pos, source_id, top_left_atlas_coords)
	tilemap.set_cell(0, top_pos + Vector2(1, 0), source_id, top_right_atlas_coords)

