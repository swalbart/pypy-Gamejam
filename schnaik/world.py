# Python stuff
from dataclasses import dataclass
import random

# Pygame stuff

# Local stuff
from game_config import *

@dataclass
class Point:
    x: int
    y: int

def random_point():
    x = random.randint(0, (WORLD_WIDTH / PLAYER_SIZE) - PLAYER_SIZE) * PLAYER_SIZE
    y = random.randint(0, (WORLD_HEIGHT / PLAYER_SIZE) - PLAYER_SIZE) * PLAYER_SIZE
    return Point(x, y)

def incarcerate(p):
    if p.x > WORLD_WIDTH - PLAYER_SIZE:
        p.x = 0
    elif p.x < 0:
        p.x = WORLD_WIDTH - PLAYER_SIZE

    if p.y > WORLD_HEIGHT - PLAYER_SIZE:
        p.y = 0
    elif p.y < 0:
        p.y = WORLD_HEIGHT - PLAYER_SIZE

    return p
