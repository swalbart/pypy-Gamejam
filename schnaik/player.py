# Python stuff
from enum import Enum

# Pygame stuff
import pygame

# Local stuff
from game_config import *
from world import *

class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

current_direction = Direction.NONE
points = []
growing = False

def init():
    global points

    points = []
    points.append(random_point())

def press(keys):
    global current_direction, growing

    if keys[pygame.K_a] and current_direction != Direction.RIGHT:
        current_direction = Direction.LEFT
    elif keys[pygame.K_d] and current_direction != Direction.LEFT:
        current_direction = Direction.RIGHT
    elif keys[pygame.K_s] and current_direction != Direction.UP:
        current_direction = Direction.DOWN
    elif keys[pygame.K_w] and current_direction != Direction.DOWN:
        current_direction = Direction.UP

def draw(drawfnc):
    global positions

    for p in points:
        rect = (p.x, p.y, PLAYER_SIZE, PLAYER_SIZE)
        drawfnc(PLAYER_COLOR, rect)

def move():
    global current_direction, points, growing

    newPoint = Point(points[0].x, points[0].y)

    if current_direction == Direction.NONE:
        return
    elif current_direction == Direction.UP:
        newPoint.y -= PLAYER_SIZE
    elif current_direction == Direction.DOWN:
        newPoint.y += PLAYER_SIZE
    elif current_direction == Direction.LEFT:
        newPoint.x -= PLAYER_SIZE
    elif current_direction == Direction.RIGHT:
        newPoint.x += PLAYER_SIZE

    points.insert(0, incarcerate(newPoint))

    if growing:
        growing = False
    else:
        points.pop()

def score():
    return len(points)
