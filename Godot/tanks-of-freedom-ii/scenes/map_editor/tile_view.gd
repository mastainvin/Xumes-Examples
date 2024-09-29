extends Node2D

@export var viewport_size = 20

@export var is_side_tile = false

var tile = null
var final_viewport_size = null

func _ready():
	if self.final_viewport_size == null:
		self.final_viewport_size = self.viewport_size

	$"SubViewport/tile_cam/pivot/arm/lens".set_size(self.final_viewport_size)
	self.refresh()

func refresh():
	var texture = $"SubViewport".get_texture()
	$"screen".texture = texture

func set_tile(new_tile, requested_rotation):
	if self.tile != null:
		self.clear()

	self.tile = new_tile
	$"SubViewport/tile_cam".add_child(new_tile)

	var tile_rotation = Vector3(0, deg_to_rad(requested_rotation), 0)
	new_tile.set_rotation(tile_rotation)
	new_tile.reset_position_for_tile_view()

	if self.is_side_tile:
		self.final_viewport_size = self.viewport_size + new_tile.side_tile_view_cam_modifier
	else:
		self.final_viewport_size = self.viewport_size + new_tile.main_tile_view_cam_modifier

	if new_tile.tile_view_height_cam_modifier != 0:
		var tile_position = new_tile.get_position()
		tile_position.y += new_tile.tile_view_height_cam_modifier
		new_tile.set_position(tile_position)

	$"SubViewport/tile_cam/pivot/arm/lens".set_size(self.final_viewport_size)
	self.refresh()

func clear():
	if self.tile == null:
		return

	self.tile.queue_free()
	self.tile = null

func hide_background():
	$"background".hide()
