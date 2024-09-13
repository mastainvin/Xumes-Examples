extends Node3D

@export var template_name = ""
@export var unit_can_stand = false
@export var unit_can_fly = false
@export var is_invisible = false
@export var can_share_space = false

@export var main_tile_view_cam_modifier = 0
@export var side_tile_view_cam_modifier = 0
@export var tile_view_height_cam_modifier = 0.0

@export var unit_vertical_offset = 0

@export var next_damage_stage_template = ""
@export var base_stage_template = ""

@export var shadow_override = false

var scripting_tags = {}
var current_rotation = 0

func get_dict():
	var tile_rotation = self.get_rotation_degrees()

	var tile_dict = {
		"tile" : self.template_name,
		"rotation" : tile_rotation.y
	}
	if self.scripting_tags.size() > 0:
		tile_dict["tags"] = self.scripting_tags
	return tile_dict

func reset_position_for_tile_view():
	var mesh_position = $"mesh".get_position()
	mesh_position.y = 0

	$"mesh".set_position(mesh_position)

func add_script_tag(tag):
	self.scripting_tags[tag] = true

func has_script_tag(tag):
	return self.scripting_tags.has(tag)

func is_damageable():
	return not self.next_damage_stage_template == ""

func is_restoreable():
	return not self.base_stage_template == ""

func hide_mesh():
	$"mesh".hide()

func disable_shadow():
	self._set_shadow(0)


func enable_shadow():
	self._set_shadow(1)

func _set_shadow(shadow_value):
	$"mesh".cast_shadow = shadow_value
	var reflection = self.get_node_or_null("reflection")
	if reflection != null:
		reflection.cast_shadow = shadow_value

	for child in $"mesh".get_children():
		if child is MeshInstance3D:
			child.cast_shadow = shadow_value

	for child in self.get_children():
		if child is Node3D:
			for next_child in child.get_children():
				if next_child is MeshInstance3D:
					next_child.cast_shadow = shadow_value
					return
