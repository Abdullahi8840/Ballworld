import pygame
import random

screen_width = 640
screen_height = 480

class Ball:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.x, self.y = random.randint(0, screen_width), random.randint(0, screen_height)
        self.ball_width, self.ball_height = 20, 20
        self.ball_colour = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        self.x_speed, self.y_speed = random.uniform(0.01, 0.05), random.uniform(0.01, 0.05)
        self.gravity = 0.0000005

    def draw(self):
        pygame.draw.ellipse(self.screen, self.ball_colour, (self.x, self.y, self.ball_width, self.ball_height))

    def move(self):
        self.x += self.x_speed
        self.y_speed += self.gravity
        self.y += self.y_speed

        if self.x > screen_width - self.ball_width or self.x < 0:
                self.x_speed = -self.x_speed

        if self.y > screen_height - self.ball_height or self.y < 0:
                self.y_speed = -self.y_speed
