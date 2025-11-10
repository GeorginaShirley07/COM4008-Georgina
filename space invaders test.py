import pygame
import sys
#key = pygame.K_LEFT
x = 250
#key = pygame.K_RIGHT
pygame.init()
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Space Invaders Test")
clock = pygame.time.Clock()
running = True
player_x = 370
player_img = pygame.image.load("defender.png") #load in the image
player_img = pygame.transform.scale(player_img, (35, 30)) # change the scale


while running:
    for event in pygame.event.get():
        # Handle quit event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            pygame.display.quit()
            sys.exit()
            # Quit Pygame
        # Handle key press events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
                player_x += 5
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
    
    screen.fill((0, 0, 0)) # Black background
    pygame.draw.circle(screen,(0,0,200), (player_x,450), 25) # Draw player
    pygame.display.flip()
        
pygame.quit()
pygame.display.quit()
# This code initializes a Pygame window for testing Space Invaders game mechanics.
# It creates a window of size 800x600 pixels with a black background and runs a basic event loop.
sys.exit(0)