import pygame
from global_vars import WIN_WIDTH, WIN_HEIGHT

def fhd_to_any(pixels): # only works with the same aspect ratio
    decimal = pixels / 1920
    return WIN_WIDTH * decimal

def item_on_screen(coordinates, dimensions):
    if(
        coordinates[0] > 0 - dimensions[0] and # has entered via left of window
        coordinates[0] < WIN_WIDTH and # has not left via right of window
        coordinates[1] > 0 - dimensions[1] and # has entered via top of window
        coordinates[1] < WIN_WIDTH # had not left via bottom of window
    ):
        return True
    else:
        return False