extends BaseStepActionEditor

func fill_step_data(new_step_no, new_step_data):
	super.fill_step_data(new_step_no, new_step_data)
	
	$"what/x".set_text("")
	$"what/y".set_text("")
	$"player_side/side".set_text("")
	
	if self.step_data.has("details"):
		if self.step_data["details"].has("what"):
			$"what/x".set_text(str(self.step_data["details"]["what"][0]))
			$"what/y".set_text(str(self.step_data["details"]["what"][1]))
		if self.step_data["details"].has("side"):
			$"player_side/side".set_text(self.step_data["details"]["side"])

func _compile_step_data():
	self.step_data = super._compile_step_data()
	
	var x = $"what/x".get_text()
	var y = $"what/y".get_text()
	var player_side = $"player_side/side".get_text()

	self.step_data["details"] = {}

	if x != "" and y != "":
		self.step_data["details"]["what"] = [int(x), int(y)]
	if player_side != "":
		self.step_data["details"]["side"] = player_side

	return self.step_data


func _on_picker_button_pressed():
	self.audio.play("menu_click")

	var vip_position = null
	if self.step_data["details"].has("what"):
		vip_position = self.step_data["details"]["what"]

	self.picker_requested.emit({
		"type": "position",
		"position": vip_position,
		"step_no": self.step_no
	})

func _on_side_picker_button_pressed():
	self.audio.play("menu_click")

	self.picker_requested.emit({
		"type": "side",
		"step_no": self.step_no
	})

func _handle_picker_response(response, context):
	super._handle_picker_response(response, context)
	if context["type"] == "position":
		$"what/x".set_text(str(response.x))
		$"what/y".set_text(str(response.y))
	if context["type"] == "side":
		$"player_side/side".set_text(response)
	_emit_updated_signal()
