# Python stuff

# Pygame stuff
import pygame
from pygame.locals import *

# Local stuff
from game_config import *
import player as player
import food as food

is_running = False
window = None
clock = None
player_event = pygame.USEREVENT + 1
food_event = pygame.USEREVENT + 2
player_interval = 250

# Internal Functions
def draw_rect(color, rect):
    global window
    pygame.draw.rect(window, color, rect)

def collision(rect1, rect2):
    return rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0] and rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]

def eating():
    global player_event, player_interval

    for pp in player.points:
        for fp in food.points:
            rect1 = (pp.x, pp.y, PLAYER_SIZE, PLAYER_SIZE)
            rect2 = (fp.x, fp.y, PLAYER_SIZE, PLAYER_SIZE)
            if collision(rect1, rect2):
                food.points.remove(fp)
                player.growing = True

                new_interval = player_interval - max(1, 20//player.score())
                player_interval = max(10, new_interval)
                print(player_interval)
                pygame.time.set_timer(player_event, player_interval)

# Main Functions
def init():
    global window, clock, is_running

    # Pygame stuff
    pygame.init()
    pygame.display.set_caption(WINDOW_CAPTION)
    pygame.time.set_timer(player_event, 200)
    pygame.time.set_timer(food_event, 5000)

    window = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
    clock = pygame.time.Clock()

    player.init()
    food.init()

    is_running = True

def update():
    global player, food, clock, is_running

    clock.tick(60)

    # Keys
    player.press(pygame.key.get_pressed())

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == player_event:
            player.move()
            eating()
        elif event.type == food_event:
            food.create()

    # Draw
    window.fill(BACKGROUND_COLOR)

    player.draw(draw_rect)
    food.draw(draw_rect)

    pygame.display.update()

def close():
    pygame.quit()
