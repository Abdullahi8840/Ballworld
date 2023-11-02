import pygame
from pygame.locals import *
from ball import Ball

'''
changing somewhere else
'''

screen_width = 640
screen_height = 480
frame_rate = 60

def ball_world():
    # Initialize pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Ball")

    # Create Ball instances
    ball_list = []
    for ball in range(0,1):
        b = Ball(screen,screen_width,screen_height)
        ball_list.append(b)
    

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen once per frame
        screen.fill((0, 0, 0))

        for ball in ball_list:
            ball.move()
        for ball in ball_list:
            ball.draw()
        # Draw both balls
       

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    ball_world()


