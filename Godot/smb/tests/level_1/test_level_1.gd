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

func set_environment(width: int, height: int):
	player.set_environment(width, height)
	
func _on_goal_body_entered(body: Node2D) -> void:
	if body == player:
		in_goal = true
		
		
func _on_goal_body_exited(body: Node2D) -> void:
	if body == player:
		in_goal = false

func set_goal(x: int, y: int):
	goal.position = tilemap.map_to_local(Vector2i(x, y))

func _on_death_zone_body_entered(body: Node2D) -> void:
	if body == player:
		dead = true
		
func set_mario_position(x: int, y: int):
	player.position = tilemap.map_to_local(Vector2i(x, y))
