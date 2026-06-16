import pygame
import sys
from CONSTANTS import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🦆 DuckyDynamics")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 44, 52))
    pygame.display.flip()

pygame.quit()
sys.exit()