# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1280
HEIGHT = 950
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player =  [50, 25, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 =  [100, 275, 200, 25]
wall2 =  [100, 350, 25, 200]
wall3 =  [100, 25, 25, 200]
wall4 =  [0, 0, 1280, 25]
wall5 =  [0, 925, 1280, 25]
wall6 =  [0, 0, 25, 950]
wall7 =  [1255, 0, 25, 950]
wall8 =  [0, 550, 440, 25]
wall9 =  [100, 450, 200, 25]
wall10 = [980, 275, 200, 25]
wall11 = [1155, 350, 25, 200]
wall12 = [1155, 25, 25, 200]
wall13 = [930, 550, 300, 25]
wall14 = [980, 450, 200, 25]
wall15 = [100, 350, 200, 25]
wall16 = [325, 350, 25, 200]
wall17 = [980, 350, 200, 25]
wall18 = [930, 350, 25, 200]
wall19 = [415, 275, 185, 25]
wall20 = [655, 275, 200, 25]
wall21 = [415, 275, 25, 500]
wall22 = [575, 275, 25, 450]
wall23 = [495, 775, 800, 25]
wall24 = [655, 775, 200, 25]
wall25 = [655, 300, 25, 425]
wall26 = [830, 275, 25, 500]
wall27 = [495, 325, 25, 475]
wall28 = [340, 775, 100, 25]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,
         wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17,
         wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25,
         wall26, wall27, wall28]

# Make coins
coin1 = [150, 500, 25, 25]
coin2 = [200, 400, 25, 25]
coin3 = [50, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
case = 1
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_w]
    down = pressed[pygame.K_s]
    left = pressed[pygame.K_a]
    right = pressed[pygame.K_d]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0
        
    if left:
        player_vx = -player_speed
    elif right:
        player_vx = player_speed
    else:
        player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''
    top = player[1]
    bottom = player[1] + player[3]
    left = player[0]
    right = player[0] + player[2]
    if case == 1:
        ''' if the block is moved out of the window, nudge it back on. '''
        if top < 0:
            player[1] = 0
        elif bottom > HEIGHT:
            player[1] = HEIGHT - player[3]

        if left < 0:
            player[0] = 0
        elif right > WIDTH:
            player[0] = WIDTH - player[2]




    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [565, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
