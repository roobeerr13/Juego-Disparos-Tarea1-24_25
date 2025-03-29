import os
import pygame
from game import Game

def main():
    print("Directorio de trabajo actual:", os.getcwd())  # Verifica el directorio de trabajo
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()