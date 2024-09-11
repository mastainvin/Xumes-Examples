extends Player

class_name TestPlayer


@export var tile_coords_to_type := {
	Vector2i(7, 4): 3,
	Vector2i(8, 4): 3,
	Vector2i(7, 5): 3,
	Vector2i(8, 5): 3,
	Vector2i(1, 0): 1,
	Vector2i(0, 0): 2,
}

@export var tilemap: TileMap

var matrix_size: Vector2i 

var environment = []

func set_environment(width: int, height: int):
	matrix_size = Vector2i(width, height)
	for x in range(width):
		environment[x]=[]
		for y in range(height):
			environment[x][y]=0


func _process(delta: float) -> void:
	super._process(delta)
	var player_position = global_position
	environment = get_tile_environment(player_position)
	
func get_tile_environment(player_position: Vector2):
	var player_tile_position = tilemap.local_to_map(player_position)
	
	  # Calculer la moitié de la taille de la matrice
	var half_matrix_size = matrix_size / 2

	# Créer une matrice pour stocker les données des tuiles
	var environment_matrix = []

	# Parcourir les tuiles autour du joueur
	for x in range(matrix_size.x):
		var row = []
		for y in range(matrix_size.y):
			var tile_position = player_tile_position + Vector2i(x - half_matrix_size.x, y - half_matrix_size.y)
			var atlas_coords = tilemap.get_cell_atlas_coords(0, tile_position)
			var tile_type = tile_coords_to_type.get(atlas_coords, 0)
			row.append(tile_type)
		# Ajouter la ligne à la matrice
		environment_matrix.append(row)

	return environment_matrix
