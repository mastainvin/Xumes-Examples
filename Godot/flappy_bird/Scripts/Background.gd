extends ParallaxBackground

@export var scroll_speed : float
var speed : float


func _ready():
	speed = scroll_speed
	GameManager.game_started.connect(_on_game_started)
	GameManager.bird_crashed.connect(_on_bird_crashed)


func _process(delta):
	scroll_base_offset.x -= speed * delta
	#scroll_base_offset.x -= speed * delta


func _on_game_started():
	speed = scroll_speed


func _on_bird_crashed():
	speed = 0
