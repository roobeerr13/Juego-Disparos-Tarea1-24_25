import pygame
from character import Character

class Player(Character):
    def __init__(self, game):
        width = int(game.width * 0.05)
        height = int(game.height * 0.05)
        x = game.width // 2 - width // 2
        y = game.height - height
        speed = 5
        image_path = 'assets/bueno.png'
        dead_image_path = 'assets/bueno_muerto.png'
        super().__init__(game, width, height, x, y, speed, image_path, dead_image_path)
        self.lives = 3  # Número de vidas
        self.score = 0  # Puntuación inicial

def update(self, keys, mouse_pressed):
    self.move(keys)  # Mueve al jugador según las teclas presionadas
    if keys[pygame.K_SPACE] or mouse_pressed[0]:  # Dispara con barra espaciadora o clic izquierdo
        self.shoot()

def move(self, keys):
    if keys[pygame.K_a] and self.x > 0:  # Mover a la izquierda con 'A'
        self.x -= self.speed
    if keys[pygame.K_d] and self.x < self.game.width - self.width:  # Mover a la derecha con 'D'
        self.x += self.speed
    self.rect.topleft = (self.x, self.y)  # Actualiza el rectángulo de colisión

    def shoot(self):
        from shot import Shot  # Importación aquí para evitar dependencias circulares
        shot = Shot(self.game, self)
        self.game.player_shots.append(shot)

    def die(self):
        self.lives -= 1
        if self.lives == 0:
            self.game.end_game(won=False)
        else:
            self.dead = True
            pygame.time.set_timer(pygame.USEREVENT, 2000)