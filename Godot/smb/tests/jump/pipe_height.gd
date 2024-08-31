extends FeatureNode

@onready
var tilemap: TileMap = $TileMap

@onready
var player: TestPlayer = $Player

@onready
var goal: Area2D = $Goal

var in_goal: bool
var dead: bool

func _ready() -> void:
	in_goal = false
	dead = false

func set_pipe(x: int, y: int, size: int):
	if size > 0:
		resize_pipe(Vector2(x, y), size, Vector2(7,4),  Vector2(8,4), Vector2(7,5), Vector2(8,5))
	
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

func _on_goal_body_entered(body: Node2D) -> void:
	if body == player:
		in_goal = true
		
		
func _on_goal_body_exited(body: Node2D) -> void:
	if body == player:
		in_goal = false

func set_platform(x: int, y: int, size: int):
	var source_id = 0 
	var atlas_coords = Vector2i(1, 0)
	
	var position = Vector2i(x, y)
	
	for i in range(size):
		tilemap.set_cell(0, position, source_id, atlas_coords)
		position += Vector2i(1, 0) 
		

func set_goal(x: int, y: int):
	goal.position = tilemap.map_to_local(Vector2i(x, y))

func _on_death_zone_body_entered(body: Node2D) -> void:
	if body == player:
		dead = true
		
func set_mario_position(x: int, y: int):
	player.position = tilemap.map_to_local(Vector2i(x, y))
