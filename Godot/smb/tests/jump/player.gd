extends Player

class_name TestPlayer

@export var tile_coords_to_type := {
	Vector2i(7, 4): 1,
	Vector2i(8, 4): 1,
	Vector2i(7, 5): 1,
	Vector2i(8, 5): 1,
	Vector2i(1, 0): 1,
	Vector2i(0, 0): 1,
}

@export var tilemap: TileMap

var matrix_size: Vector2i 


var environment = []
var block_env = {}
var tilemap_position = Vector2i(0, 0)

func set_environment(width: int, height: int):
	matrix_size = Vector2i(width, height)
	environment = []
	for x in range(width):
		var column = []
		for y in range(height):
			column.append(0)  # Initialiser avec 0
		environment.append(column)

			


func _process(delta: float) -> void:
	super._process(delta)  # Peut-être pas nécessaire
	get_tile_environment()
	tilemap_position = tilemap.local_to_map(global_position)
	add_block()  # Ajoutez les blocs après avoir mis à jour l'environnement

	
func add_block():
	for block in block_env.keys():
		var relative_position = get_block_relative_position(block.global_position)

		if relative_position.x >= 0 and relative_position.x < matrix_size.x and relative_position.y >= 0 and relative_position.y < matrix_size.y:
			environment[relative_position.x][relative_position.y] = 1

	
func get_tile_environment():
	var player_tile_position = tilemap.local_to_map(global_position)
	
	  # Calculer la moitié de la taille de la matrice
	var half_matrix_size = matrix_size / 2

	# Parcourir les tuiles autour du joueur
	for x in range(matrix_size.x):
		for y in range(matrix_size.y):
			var tile_position = player_tile_position + Vector2i(x - half_matrix_size.x, y - half_matrix_size.y)
			var atlas_coords = tilemap.get_cell_atlas_coords(0, tile_position)
			var tile_type = tile_coords_to_type.get(Vector2i(atlas_coords), 0)
			if tile_type != 0:
				environment[x][y] = 1
			else:
				environment[x][y] = 0

func get_block_relative_position(block_position: Vector2):
	var player_tile_position = tilemap.local_to_map(global_position)

	# La position de la tuile du bloc
	var block_tile_position = tilemap.local_to_map(block_position)

	# Calculer la moitié de la taille de la matrice
	var half_matrix_size = matrix_size / 2

	# Calculer la position relative du bloc par rapport à l'environnement généré autour du joueur
	var relative_position = block_tile_position - player_tile_position + half_matrix_size

	return Vector2i(relative_position.x, relative_position.y)


func add_to_env_matrix(block):
	block_env[block] = null

func remove_from_env_matrix(block):
	if block_env.has(block):
		block_env.erase(block)


