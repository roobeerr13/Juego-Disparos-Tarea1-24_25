from character import Character
import random

class Opponent(Character):
    def __init__(self, game):
        width = int(game.width * 0.05)
        height = int(game.height * 0.05)
        x = random.randint(0, game.width - width)
        y = 0
        speed = 5
        image_path = 'assets/malo.png'
        dead_image_path = 'assets/malo_muerto.png'
        super().__init__(game, width, height, x, y, speed, image_path, dead_image_path)

    def update(self):
        self.move()  # Mueve al oponente

    def move(self):
        if not self.dead:
            self.y += self.speed
            if self.y > self.game.height:  # Si el oponente sale de la pantalla, reinicia su posición
                self.y = 0
                self.x = random.randint(0, self.game.width - self.width)
            self.rect.topleft = (self.x, self.y)  # Actualiza el rectángulo de colisión

    def die(self):
        super().die()
        self.game.score += 1  # Incrementa la puntuación del jugador