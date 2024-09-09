import pygame

WIN_WIDTH, WIN_HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
WIN_WIDTH, WIN_HEIGHT = pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]
FPS = 60