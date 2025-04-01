import pygame
from entity import Entity
from player import Player

class Shot(Entity):
    def __init__(self, game, character):
        width = int(game.width * 0.015)
        height = int(game.height * 0.015)
        x = character.x + character.width // 2 - width // 2
        y = character.y
        speed = 10
        image_path = 'assets/shot1.png' if isinstance(character, Player) else 'assets/shot2.png'
        super().__init__(game, width, height, x, y, speed, image_path)
        self.is_player_shot = isinstance(character, Player)  # Indica si el disparo es del jugador

    def move(self):
        self.y -= self.speed if self.is_player_shot else -self.speed
        self.rect.topleft = (self.x, self.y)  # Actualiza el rectángulo de colisión

        # Elimina el disparo si sale de los límites de la pantalla
        if self.y < 0 or self.y > self.game.height:
            if self.is_player_shot:
                self.game.player_shots.remove(self)
            else:
                self.game.opponent_shots.remove(self)

    def hit_target(self, target):
        return self.rect.colliderect(target.rect)

    def update(self):
        self.move()

    def __str__(self):
        return super().__str__() + ' (SHOT)'