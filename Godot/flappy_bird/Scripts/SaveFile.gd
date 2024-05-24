extends Node

const SAVE_FILE = "user://save_file.save"
var best_score : int


func _ready():
	load_game()


func save_game():
	var file = FileAccess.open(SAVE_FILE, FileAccess.WRITE)
	file.store_var(best_score)
	file.close()


func load_game():
	if FileAccess.file_exists(SAVE_FILE):
		var file = FileAccess.open(SAVE_FILE, FileAccess.READ)
		best_score = file.get_var(best_score)
	else:
		best_score = 0
