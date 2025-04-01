import os
import pygame
from game import Game

def main():
    os.environ["SDL_AUDIODRIVER"] = "dummy"  # Deshabilita el audio
    pygame.init()
    game = Game()
    game.start() 

if __name__ == "__main__":
    main()