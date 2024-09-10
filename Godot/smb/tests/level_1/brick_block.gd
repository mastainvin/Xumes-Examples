extends BrickBlock

var player_ref

var tile_map_position

func _ready():
	player_ref = $"../Player"  # Assurez-vous que le Player est bien dans le chemin spécifié
	connect("visibility_changed", _on_visibility_changed)

	# Vérification manuelle au démarrage
	if is_visible_in_tree():
		player_ref.add_to_env_matrix(self)

func _on_visibility_changed():
	if is_visible_in_tree():
		player_ref.add_to_env_matrix(self)
	else:
		player_ref.remove_from_env_matrix(self)  # Correction du nom de la méthode
