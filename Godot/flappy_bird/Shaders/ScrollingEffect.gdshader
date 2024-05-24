shader_type canvas_item;

uniform float speed  = 0.2;

void fragment() {
	vec2 newuv  = UV;
	newuv.x += TIME * speed;
	vec4 c = texture(TEXTURE, newuv);
	COLOR = c;
}
