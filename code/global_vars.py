import pygame

pygame.display.init()

if pygame.display.Info().current_w / pygame.display.Info().current_h < 1920/1080:
    WIN_WIDTH, WIN_HEIGHT = pygame.display.Info().current_w*0.9, pygame.display.Info().current_w*0.9/16*9

elif pygame.display.Info().current_w / pygame.display.Info().current_h > 1920/1080:
    WIN_WIDTH, WIN_HEIGHT = pygame.display.Info().current_h*0.9/9*16, pygame.display.Info().current_h*0.9

else:
    WIN_WIDTH, WIN_HEIGHT = pygame.display.Info().current_w*0.9, pygame.display.Info().current_h*0.9


WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.SCALED, vsync=1)
pygame.display.set_caption("SailDrift Simulator")

FPS = 60

speed = 5
heading = 60