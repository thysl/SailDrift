import pygame
from global_vars import WIN_WIDTH, WIN_HEIGHT, WIN, FPS
from background_scroll import water_tiles

# init

pygame.init()
    
# init main game loop

clock = pygame.time.Clock()

run = True
while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
    
    # blitting items
    WIN.fill("black")

    for water_tile in water_tiles:
        WIN.blit(water_tile.IMG, (water_tile.x, water_tile.y))
        water_tile.update()

    # other
    pygame.display.update()
    clock.tick(FPS)

    # testing
    print(clock.get_fps())

pygame.quit()