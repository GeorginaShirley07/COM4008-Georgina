import pygame
import numpy as np
key = pygame.K_LEFT
x = 250
key = pygame.K_RIGHT
pygame.init()
screen = pygame.display.set_mode((800, 600)) 
#Board = np.full(fill_value= "_", shape=(9,9), dtype=np.str_)
#print(Board)
pygame.display.set_caption("Space Invaders Test")
clock = pygame.time.Clock()
running = True
player_x = 370
Board = np.full(fill_value= "_", shape=(9,9), dtype=np.str_)
print(Board)

while running:
    for event in pygame.event.get():
        # Handle quit event
        if event.type == pygame.QUIT:
            running = False
            # Quit Pygame
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("Left arrow key pressed")
                player_x += 5
    
    screen.fill((0, 0, 0))
    # Limit frame rate to 60 FPS
    #clock.tick(60)
    pygame.draw.circle(screen,(0,0,200), (200,200), 25)
    pygame.display.flip()
        # Handle key press events

pygame.quit()
pygame.display.quit()
# This code initializes a Pygame window for testing Space Invaders game mechanics.
# It creates a window of size 800x600 pixels with a black background and runs a basic event loop.
