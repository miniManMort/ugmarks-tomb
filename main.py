import pygame
from level import Level
from hero import Hero

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

dungeon_level = Level(10,10,screen)
dungeon_level.draw()

hero = Hero(100,100,screen)
hero.draw()



# Game loop
running = True
xmove=0
ymove=0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:  
                xmove=  -1
            elif event.key == pygame.K_RIGHT:  
                xmove = 1  # object moves 0.3 towards x axis
            elif event.key == pygame.K_UP: 
                ymove = -1  # object moves -0.3 towards y axis
            elif event.key == pygame.K_DOWN: 
                ymove = 1  # object moves 0.3 towards y axis

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  
                xmove=  0
            elif event.key == pygame.K_RIGHT:  
                xmove = 0  # object moves 0.3 towards x axis
            elif event.key == pygame.K_UP: 
                ymove = 0  # object moves -0.3 towards y axis
            elif event.key == pygame.K_DOWN: 
                ymove = 0  # object moves 0.3 towards y axis

    hero.move(xmove, ymove)
    dungeon_level.draw()
    hero.draw()


    pygame.display.flip()


# Quit Pygame
pygame.quit()