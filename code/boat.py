import pygame 
from global_vars import WIN, heading
from boat_types.lelievlet import lelievlet
from functions import percent

class boat_class:
    
    def __init__(self, type):

        self.orignal_IMG = pygame.image.load(f"./assets/images/{type}.png")
        self.orignal_IMG = self.orignal_IMG.convert_alpha()
        self.orignal_IMG = pygame.transform.scale(self.orignal_IMG, (percent(10), percent(20)))
        self.IMG = self.orignal_IMG
    
    def image_update(self):

        pass

boat = boat_class("lelievlet")