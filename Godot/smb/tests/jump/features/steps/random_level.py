import random
from xumes import config, given, when, then
from tests.jump.features.steps.play_agent import PlayAgent
from collections import deque


def random_position(width, height):
    return random.randint(0, width - 1), random.randint(0, height - 1)


def is_reachable(p1, p2, max_jump_distance, max_jump_height):
    """Check if p2 is reachable from p1 within jump constraints."""
    dx = abs(p2[0] - p1[0])
    dy = p2[1] - p1[1]
    return dx <= max_jump_distance and dy <= max_jump_height


def random_platforms(num_platforms, width, height, max_jump_distance, max_jump_height):
    platforms = []
    last_platform = (0, random.randint(0, height - 1))
    platforms.append(last_platform)

    for _ in range(num_platforms - 1):
        while True:
            new_platform = random_position(width, height)
            if is_reachable(last_platform, new_platform, max_jump_distance, max_jump_height):
                platforms.append(new_platform)
                last_platform = new_platform
                break
    return platforms


def validate_path(start, goal, platforms, max_jump_distance, max_jump_height):
    """Use BFS or a simple pathfinding algorithm to validate a path exists."""
    queue = deque([start])
    visited = set()
    while queue:
        current = queue.popleft()
        if current == goal:
            return True
        for platform in platforms:
            if platform not in visited and is_reachable(current, platform, max_jump_distance, max_jump_height):
                visited.add(platform)
                queue.append(platform)
    return False


@config
def step_impl(context):
    context.driver.set_scene("res://tests/random/random.tscn")




@given("An environment of size {width:d} x {height:d}")
def step_impl(context, width, height):
    context.width = width
    context.height = height
    context.driver.set_environment(width, height)

@given("Mario at a random position")
def step_impl(context):
    mario_x, mario_y = random_position(context.width, context.height)
    context.mario_x, context.mario_y = mario_x, mario_y
    context.driver.set_mario_position(mario_x, mario_y)

@given("A random goal")
def step_impl(context):
    goal_x, goal_y = random_position(context.width, context.height)
    context.goal = (goal_x, goal_y)
    context.driver.set_goal(goal_x, goal_y)








@given("Random platforms")
def step_impl(context):
    max_jump_distance = 3  # Example value, adjust as needed
    max_jump_height = 2  # Example value, adjust as needed
    num_platforms = random.randint(3, 10)

    while True:
        platforms = random_platforms(num_platforms, context.width, context.height, max_jump_distance, max_jump_height)
        if validate_path((context.mario_x, context.mario_y), context.goal, platforms, max_jump_distance,
                         max_jump_height):
            break

    for x, y in platforms:
        context.driver.set_platform(x, y, random.randint(1, 5))

@when("I want to reach the goal")
def step_impl(context):
    return PlayAgent(previous_model_path="./tests/jump/models/play/best_model.zip", width=35, height=15)


@then("Reach the goal without dying")
def step_impl(context):
    context.assert_true(context.in_goal)
    context.assert_false(context.dead)
