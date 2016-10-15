import pygame


class Player:
    def __init__(self, system):
        self.system = system
        self.x = system.setting_width / 2
        self.y = system.setting_height / 2
        self.velocity = 0
        self.color = (231, 50, 123)
        self.invincible = False

    def update(self):
        if self.velocity > 0: self.velocity -= 0.1 * self.velocity
        self.y += self.system.setting_gravity - self.velocity
        pygame.draw.circle(self.system.data_screen, self.color, (int(self.x), int(self.y)),
                           self.system.setting_circle_radius)

    def jump(self):
        self.velocity = self.system.setting_velocity

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_invincible(self):
        return self.invincible
