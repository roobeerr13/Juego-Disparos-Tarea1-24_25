import pygame
import os
from player import Player
from opponent import Opponent

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.player = Player(self)
        self.opponent = Opponent(self)
        self.player_shots = []
        self.opponent_shots = []
        self.score = 0
        self.ended = False
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            keys = pygame.key.get_pressed()
            self.update(keys)
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def update(self, keys):
        self.player.update(keys)
        self.opponent.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Llena la pantalla con negro
        self.player.render()  # Dibuja al jugador
        self.opponent.render()  # Dibuja al oponente
        pygame.display.flip()  # Actualiza la pantalla