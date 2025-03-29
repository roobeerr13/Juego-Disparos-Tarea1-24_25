import pygame

class Game:
    def __init__(self):
        self.running = True  # Asegúrate de definir este atributo
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Juego de Disparos")

    def run(self):
        while self.running:  # Usa el atributo definido
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))  # Pinta la pantalla de negro
            pygame.display.flip()
        pygame.quit()

    def update(self, keys):
        self.player.update(keys)
        self.opponent.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Llena la pantalla con negro
        self.player.render()  # Dibuja al jugador
        self.opponent.render()  # Dibuja al oponente
        pygame.display.flip()  # Actualiza la pantalla