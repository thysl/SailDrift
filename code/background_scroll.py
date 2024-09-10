import pygame
from functions import fhd_to_any
from global_vars import WIN_WIDTH, WIN_HEIGHT

class water_tile:

    def __init__(self, x, y):

        self.IMG = pygame.image.load('./assets/images/water_tile.png')
        self.IMG = pygame.transform.scale(self.IMG, (WIN_WIDTH, WIN_HEIGHT))

        self.WIDTH = self.IMG.get_width()
        self.HEIGHT = self.IMG.get_height()

        self.x = x
        self.y = y

water_tiles = []

water_tiles.append(water_tile(-(water_tile(0, 0).WIDTH / 2), -(water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile((water_tile(0, 0).WIDTH / 2), (water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile(-(water_tile(0, 0).WIDTH / 2), (water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile((water_tile(0, 0).WIDTH / 2), -(water_tile(0, 0).HEIGHT / 2)))