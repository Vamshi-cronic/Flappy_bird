import pygame
from neural_network import NeuralNetwork


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vel = 0
        self.gravity = 0.2
        self.jump_force = -5

        self.radius = 15
        self.alive = True

        self.brain = NeuralNetwork([3, 9, 1])

        self.score = 0

    def update(self):
        self.vel += self.gravity
        self.y += self.vel

        if self.y < 0 or self.y > 800:
            self.alive = False

    def jump(self):
        self.vel = self.jump_force

    def think(self, pipe):
        inputs = [
            self.y / 800,
            pipe.top / 800,
            pipe.bottom / 800,
        ]

        output = self.brain.predict(inputs)

        if output > 0.5:
            self.jump()

    def hit(self, poll):
        if not poll:
            return False

        inside_x = poll.x <= self.x + self.radius <= poll.x + poll.w

        hit_top = self.y - self.radius <= poll.top
        hit_bottom = self.y + self.radius >= poll.bottom

        return inside_x and (hit_top or hit_bottom)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(self.x), int(self.y)),
            self.radius
        )