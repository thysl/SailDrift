import pygame

pygame.display.init()

WIN_WIDTH, WIN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_w/16*9
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("SailDrift Simulator")

FPS = 60

speed = 6
heading = 328