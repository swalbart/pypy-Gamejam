# Python stuff

# Pygame stuff

# Local stuff
from game_config import *
import world as world

points = []

def init():
    points = []
    create()

def create():
    if len(points) < 5:
        points.append(world.random_point())

def draw(drawfnc):
    for p in points:
        drawfnc(FOOD_COLOR, (p.x, p.y, PLAYER_SIZE, PLAYER_SIZE))
