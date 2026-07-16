import pygame
import sys
from CONSTANTS import *
from physics import *

# ---- Object Arrays ---- #
balls = []
squares = []

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🦆 DuckyDynamics")

ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
square = Square(SCREEN_WIDTH, SCREEN_HEIGHT)
squares.append(square)
balls.append(ball)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos

    screen.fill((40, 44, 52))

    pygame.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), ball.radius)
    pygame.draw.rect(screen, square.color, (int(square.x), int(square.y), square.radius, square.radius))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()