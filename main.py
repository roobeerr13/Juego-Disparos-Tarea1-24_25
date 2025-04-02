import os
import pygame
from game import Game

def main():
    os.environ["SDL_AUDIODRIVER"] = "dummy"  # Evita problemas de audio en algunos sistemas
    pygame.init()
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(f"Error inesperado: {e}")  # Captura errores y los imprime en la consola
    finally:
        pygame.quit()  # Asegura que pygame se cierre correctamente

if __name__ == "__main__":
    main()