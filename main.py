import pygame
from bird import Bird
from polls import Polls
import random


POPULATION = 50


def generateBirds(best_bird):
    birds = []

    for _ in range(POPULATION):
        new_bird = Bird(WIDTH // 4, HEIGHT // 2)

        new_bird.brain = best_bird.brain.copy()
        new_bird.brain.mutate(rate=0.2, scale=0.5)

        birds.append(new_bird)

    return birds


pygame.init()

WIDTH = 800
HEIGHT = 800

highest_score = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

best_bird = Bird(WIDTH // 4, HEIGHT // 2)

birds = generateBirds(best_bird)

polls = []
frame_count = 0
score = 0
generation = 1

running = True

while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if frame_count % 120 == 0:
        polls.append(Polls())

    polls = [poll for poll in polls if not poll.offscreen()]

    for poll in polls:
        poll.update()
        poll.draw(screen)

    nearest_pipe = None
    for poll in polls:
        if poll.x + poll.w >= WIDTH // 4:
            nearest_pipe = poll
            break

    if not birds:
        print(f"Generation {generation} | Best Score = {highest_score}")
        birds = generateBirds(best_bird)

        polls = [Polls()]
        frame_count = 0
        score = 0
        generation += 1

    alive_birds = []

    for bird in birds:
        if nearest_pipe:
            bird.think(nearest_pipe)

        bird.update()
        bird.draw(screen)

        bird.score += 1

        if nearest_pipe and bird.hit(nearest_pipe):
            bird.alive = False

        if bird.alive:
            alive_birds.append(bird)

            if bird.score > highest_score:
                highest_score = bird.score
                best_bird = bird

    birds = alive_birds

    pygame.display.update()

pygame.quit()