import pygame 
from global_vars import WIN, heading
import lelievlet

class boat_class:
    
    def __init__(self, type):

        self.orignal_IMG = pygame.image.load(f"./assets/images/{type}.png")
        #self.orignal_IMG = 
        self.IMG = self.orignal_IMG
    
    def image_update(self):

        pass

boat = boat_class("lelievlet")