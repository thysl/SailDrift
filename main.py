import pygame

WIN_WIDTH, WIN_HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

run = True
while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()