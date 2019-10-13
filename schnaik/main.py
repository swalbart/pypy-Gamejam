# Python stuff

# Pygame stuff

# Local stuff
import game as game

def main():
    game.init()

    while game.is_running:
        game.update()

    game.close()

if __name__ == '__main__':
    main()
