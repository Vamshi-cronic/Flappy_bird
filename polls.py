import pygame
import random


class Polls:
    def __init__(self):
        self.spacing = 180
        self.center_y = random.randint(150, 650)

        self.x = 800
        self.w = 80

        self.top = self.center_y - self.spacing // 2
        self.bottom = self.center_y + self.spacing // 2

        self.speed = 3

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.w, self.top))

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (self.x, self.bottom, self.w, 800 - self.bottom)
        )

    def offscreen(self):
        return self.x + self.w < 0