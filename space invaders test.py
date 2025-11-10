import pygame
import sys
#key = pygame.K_LEFT
x = 250
#key = pygame.K_RIGHT
pygame.init()
screen = pygame.display.set_mode((475, 500)) 
pygame.display.set_caption("Space Invaders Test")
clock = pygame.time.Clock()
FPS = 20
running = True
player_x = 225
player_img = pygame.image.load("defender.png") #load in the image
player_img = pygame.transform.scale(player_img, (35, 30)) # change the scale
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
#invaiders

invader_startrow = 100
invader_endrow = 300
invader_startcol = 100
invader_endcol = 300 

move_right = True

invader_img = pygame.image.load("invader1.png")
invader_img = pygame.transform.scale(invader_img, (30, 30))

def draw_invader():
    for row in range(invader_startrow, invader_endrow, 30): # intervals of 30 
        for col in range(invader_startcol, invader_endcol, 30):
            screen.blit(invader_img, (col, row))
    
def move_invaders():
    global invader_startcol, invader_endcol, invader_startrow, invader_endrow, move_right
    # start moving right 
    if move_right == True:
        invader_startcol += 2
        invader_endcol += 2
        edge_hit = False
    else: # otherwise move left
        invader_startcol -= 2
        invader_endcol -= 2
        edge_hit = False
    
    # detect edge of screen
    if invader_endcol > 450 or invader_startcol < 0:
        edge_hit = True
        invader_startrow += 20
        invader_endrow += 20
    
    # immediately reset edge_hit to prevent getting stuck! 
    if edge_hit == True:
        edge_hit == False
        if move_right == True:
            move_right = False
        else:
            move_right = True

fired = False
collide = False

bullet = bullet(player.x, player.y, 10, 20, 10)
bullets = []


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
            elif event.key == pygame.K_SPACE:
                fired = True
                bullet.x = player.x + 15
                bullet.y = player.y
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
    
    screen.fill((0, 0, 0)) # Black background
    
    draw_invader()
    
    move_invaders()

    screen.blit(player_img, (player_x, 450))
    #pygame.draw.circle(screen,(0,0,200), (player_x,450), 25) # Draw player
    pygame.display.flip()

    if fired == True:
        pygame.draw.rect(screen, [0,255,0], bullet.rect)
        bullet.y -= bullet.speed
        bullet.update()
    if bullet.y < 0:
            fired = False # for reset
        
    if bullet.rect.colliderect(invader.rect) and collide == False:
        invaders.remove(invader)
        collide = True
        bullet.x = -10
        bullet.y = -10
    
    clock.tick(FPS)

pygame.quit()
pygame.display.quit()
# This code initializes a Pygame window for testing Space Invaders game mechanics.
# It creates a window of size 800x600 pixels with a black background and runs a basic event loop.
sys.exit(0)