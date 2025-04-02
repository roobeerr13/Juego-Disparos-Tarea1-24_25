import pygame
import random
from player import Player
from opponent import Opponent
from boss import Boss
from shot import Shot

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

    def start(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.USEREVENT and self.player.dead:
                    self.player.image = pygame.image.load('assets/bueno.png')
                    self.player.dead = False

            keys = pygame.key.get_pressed()
            mouse_pressed = pygame.mouse.get_pressed()  # Obtiene el estado de los botones del ratón
            self.update(keys, mouse_pressed) 
            self.render()
            self.clock.tick(60)

    def update(self, keys, mouse_pressed):
        if not self.ended:
            self.player.update(keys, mouse_pressed) 
            self.opponent.update()
            for shot in self.player_shots:
                shot.update()
            for shot in self.opponent_shots:
                shot.update()
            self.check_collisions()

    def render(self):
        self.screen.fill((135, 206, 235))  # Fondo azul claro
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lives_text = self.font.render(f'Lives: {max(self.player.lives, 0)}', True, (255, 255, 255))  # Evita valores negativos
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.player.render_invulnerability_timer()  #