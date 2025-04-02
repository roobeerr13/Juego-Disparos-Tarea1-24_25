import os
import pygame
from game import Game

def main():
    os.environ["SDL_AUDIODRIVER"] = "dummy" 
    pygame.init()
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(f"Error inesperado: {e}") 
    finally:
        pygame.quit() 

if __name__ == "__main__":
    main()