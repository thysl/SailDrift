import pygame
import math
from functions import item_on_screen
from global_vars import WIN_WIDTH, WIN_HEIGHT, speed, heading

class water_tile:

    def __init__(self, x, y):

        self.IMG = pygame.image.load('./assets/images/water_tile.png')
        self.IMG = pygame.transform.scale(self.IMG, (WIN_WIDTH, WIN_HEIGHT))
        self.IMG = self.IMG.convert_alpha()

        self.WIDTH = self.IMG.get_width()
        self.HEIGHT = self.IMG.get_height()

        self.x = x
        self.y = y
    
    def update(self):

        if not item_on_screen((self.x, self.y), (self.WIDTH, self.HEIGHT)):

            exit_left, exit_top, exit_right, exit_bottom = False, False, False, False

            if self.y + self.HEIGHT <= 0: exit_top = True
            if self.x >= WIN_WIDTH: exit_right = True
            if self.y >= WIN_HEIGHT: exit_bottom = True
            if self.x <= 0: exit_left = True

            if exit_left:
                self.x += WIN_WIDTH * 2

            if exit_top:
                self.y += WIN_HEIGHT * 2
            
            if exit_right:
                self.x -= WIN_WIDTH * 2
            
            if exit_bottom:
                self.y -= WIN_HEIGHT * 2

        x_movement = speed * -math.sin(math.radians(heading))
        y_movement = speed * math.cos(math.radians(heading))

        self.x += x_movement
        self.y += y_movement

water_tiles = []

water_tiles.append(water_tile(-(water_tile(0, 0).WIDTH / 2), -(water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile((water_tile(0, 0).WIDTH / 2), (water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile(-(water_tile(0, 0).WIDTH / 2), (water_tile(0, 0).HEIGHT / 2)))
water_tiles.append(water_tile((water_tile(0, 0).WIDTH / 2), -(water_tile(0, 0).HEIGHT / 2)))