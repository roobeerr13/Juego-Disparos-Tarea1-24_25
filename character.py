import pygame
from entity import Entity

class Character(Entity):
    def __init__(self, game, width, height, x, y, speed, image_path, dead_image_path, lives=3):
        super().__init__(game, width, height, x, y, speed, image_path)
        self.dead = False
        self.dead_image = pygame.image.load(dead_image_path)
        self.lives = lives  # Número de vidas
        self.is_alive = True  # Estado de vida del personaje

    def move(self, dx=0, dy=0):
        """
        Mueve al personaje en la dirección especificada.
        """
        if self.is_alive:
            super().move(dx, dy)

    def shoot(self):
        """
        Lógica para disparar un proyectil.
        """
        if self.is_alive:
            from shot import Shot  # Importación aquí para evitar dependencias circulares
            shot = Shot(self.game, self.x + self.width // 2, self.y, -10, "assets/shot1.png")
            self.game.player_shots.append(shot)

    def collide(self, other):
        """
        Verifica si colisiona con otra entidad.
        """
        return self.rect.colliderect(other.rect)

    def collide_with_opponent(self):
        """
        Lógica cuando colisiona con un oponente.
        """
        self.lives -= 1
        if self.lives <= 0:
            self.die()

    def collide_with_player(self):
        """
        Lógica cuando colisiona con el jugador.
        """
        self.dead = True
        pygame.time.set_timer(pygame.USEREVENT, 2000)

    def die(self):
        """
        Marca al personaje como muerto.
        """
        self.dead = True
        self.is_alive = False

    def render(self):
        """
        Dibuja al personaje en la pantalla.
        """
        if self.dead:
            self.game.screen.blit(self.dead_image, (self.x, self.y))
        else:
            super().render()

    def __str__(self):
        return super().__str__() + f' (CHARACTER, Lives: {self.lives})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()