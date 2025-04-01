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
        self.score = 0  # Puntuación inicial
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
            self.update(keys, mouse_pressed)  # Pasa las teclas y el ratón al método update
            self.render()
            self.clock.tick(60)

    def update(self, keys, mouse_pressed):
        if not self.ended:
            self.player.update(keys, mouse_pressed)  # Pasa las teclas y el ratón al jugador
            self.opponent.update()
            for shot in self.player_shots:
                shot.update()
            for shot in self.opponent_shots:
                shot.update()
            self.check_collisions()

    def render(self):
        self.screen.fill((0, 0, 0))  # Fondo negro
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lives_text = self.font.render(f'Lives: {self.player.lives}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.player.render()
        self.opponent.render()
        for shot in self.player_shots:
            shot.render()
        for shot in self.opponent_shots:
            shot.render()
        pygame.display.flip()

    def check_collisions(self):
        # Colisión entre jugador y oponente
        if self.player.collide(self.opponent):
            self.player.collide_with_opponent()
        if self.opponent.collide(self.player):
            self.opponent.collide_with_player()

        # Colisiones entre disparos y oponentes
        for shot in self.player_shots:
            if shot.hit_target(self.opponent):
                self.opponent.die()
                self.player_shots.remove(shot)
                self.score += 1  # Incrementa la puntuación
                self.spawn_new_opponent()  # Genera un nuevo oponente

        # Colisiones entre disparos de oponentes y el jugador
        for shot in self.opponent_shots:
            if shot.hit_target(self.player):
                self.player.die()
                self.opponent_shots.remove(shot)

    def spawn_new_opponent(self):
        """
        Genera un nuevo oponente en una posición aleatoria.
        """
        x = random.randint(0, self.width - 50)  # Posición aleatoria dentro de los límites de la pantalla
        y = random.randint(0, self.height // 2)  # Aparece en la mitad superior de la pantalla
        self.opponent = Opponent(self)
        self.opponent.x = x
        self.opponent.y = y
        self.opponent.rect.topleft = (x, y)

    def remove_opponent(self):
        if isinstance(self.opponent, Boss):
            self.end_game(won=True)
        else:
            self.opponent = Boss(self)

    def end_game(self, won=False):
        self.ended = True
        if won:
            game_over_image = pygame.image.load('assets/you_win.png')
        else:
            game_over_image = pygame.image.load('assets/game_over.png')
        self.screen.blit(game_over_image, (self.width // 4, self.height // 4))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.is_running = False