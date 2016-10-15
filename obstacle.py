import pygame
from random import randint


class Obstacle:
    def __init__(self, system):
        self.system = system
        self.x = system.setting_width
        self.width = 50
        choice = randint(0, 3)

        if choice == 0:
            self.color = (231, 50, 123)
            self.height = 300
            self.align = self.system.setting_height - self.height

        elif choice == 1:
            self.color = (130, 200, 30)
            self.height = 400
            self.align = 0

        elif choice == 2:
            self.color = (43, 20, 10)
            self.height = 500
            self.align = 0

        elif choice == 3:
            self.color = (180, 20, 10)
            self.height = 500
            self.align = self.system.setting_height - self.height

        self.shape = pygame.draw.rect(self.system.data_screen, self.color,
                                      (self.x, self.align, self.width, self.height))

    def update(self):
        self.x -= self.system.setting_obstacle_speed
        self.shape = pygame.draw.rect(self.system.data_screen, self.color,
                                      (self.x, self.align, self.width, self.height))

    def has_collided(self, player):
        return self.shape.collidepoint(player.get_x(), player.get_y()) and not player.is_invincible()
