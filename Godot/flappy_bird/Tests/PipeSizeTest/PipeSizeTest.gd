extends FeatureNode

var pipes_positions = [1, 0]
var actual_position = 0
var dead = false
var score : int = 0

var pipes = []
var actual_pipe
var next_pipe
var X = 0
var Y = 0 
var Y1 = 0

func _ready():
	GameManager.bird_crashed.connect(_on_bird_crashed)
	GameManager.point_scored.connect(_on_point_scored)
	GameManager.game_started.emit()
	
func _on_bird_crashed():
	dead = true
	
func _on_point_scored():
	score += 1
	
func get_next_position():
	var position = actual_position
	actual_position = (actual_position + 1) % len(pipes_positions)
	return pipes_positions[position]
	
func set_pipes_position(i, j):
	pipes_positions = [i, j]
	$"Game/PipesSpawner"._on_spawn_timer_timeout()
	
func dist(x, y):
	return x - y
	
func _process(delta: float) -> void:
	pipes.clear()
	for child in $Game/PipesSpawner.get_children():
		if child is Pipes:
			pipes.append(child)
			
	if pipes:
		if score < len(pipes):
			actual_pipe = pipes[score]
			if score + 1 < len(pipes):
				next_pipe = pipes[score + 1]
		else:
			actual_pipe = pipes[0]
			next_pipe = pipes[0]
			
		X = dist($Game/Bird.position.x, actual_pipe.position.x)
		Y = dist($Game/Bird.position.y, actual_pipe.position.y)
		Y1 = dist($Game/Bird.position.y, next_pipe.position.y)
			
		
	
