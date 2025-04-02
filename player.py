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
        self.invulnerable = False  # Estado de invulnerabilidad
        self.invulnerability_timer = 0  # Temporizador de invulnerabilidad

    def update(self, keys, mouse_pressed):
        self.move(keys)  # Mueve al jugador según las teclas presionadas
        if keys[pygame.K_SPACE] or mouse_pressed[0]:  # Dispara con barra espaciadora o clic izquierdo
            self.shoot()

        # Verifica si el tiempo de invulnerabilidad ha terminado
        if self.invulnerable:
            current_time = pygame.time.get_ticks()
            if current_time - self.invulnerability_timer > 2000:  # 2 segundos de invulnerabilidad
                self.invulnerable = False

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
        if not self.invulnerable:  # Solo reduce vidas si no es invulnerable
            if self.lives > 0:
                self.lives -= 1
            if self.lives == 0:
                self.game.end_game(won=False)  # Termina el juego si las vidas llegan a 0
            else:
                self.dead = True
                self.invulnerable = True  # Activa la invulnerabilidad
                self.invulnerability_timer = pygame.time.get_ticks()  # Inicia el temporizador

    def render_invulnerability_timer(self):
        # Muestra el temporizador de invulnerabilidad en pantalla
        if self.invulnerable:
            current_time = pygame.time.get_ticks()
            remaining_time = max(0, 2000 - (current_time - self.invulnerability_timer)) // 1000
            font = pygame.font.Font(None, 36)
            timer_text = font.render(f"Invulnerable: {remaining_time}s", True, (255, 255, 255))
            self.game.screen.blit(timer_text, (10, 70))  # Muestra el temporizador debajo de las vidas