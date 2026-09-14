from random import randint, choice

from constants import *

import pygame

class Snake:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.color = choice(["black", "grey", "blue", "red", "Purple "] )
        self.speed = SPEED
        self.is_moving_left, self.is_moving_right, self.is_moving_up, self.is_moving_down = False, False, False, False

    def spawn(self):
        pass


class HeadSnake(Snake):

    def __init__(self):
        super().__init__()
        self.x = randint(0, SCREEN_WIDTH)
        self.y = randint(0, SCREEN_HEIGHT)
        self.need_coordinates = []


    def spawn(self):
        pygame.draw.rect(SCREEN,self.color, (self.x, self.y, self.width, self.height))
        # self.x += SPEED

    def move_left(self):
        self.is_moving_left = True


    def move_right(self):
        self.is_moving_right = True

    def move_up(self):
            self.is_moving_up = True

    def move_down(self):
        self.is_moving_down = True

    def update(self):
        self.need_coordinates.append((self.x + 20, self.y))
        if len(self.need_coordinates) > 100:
            self.need_coordinates.pop(0)


class AssSnake(Snake):
    def __init__(self, head):
        super().__init__()
        self.need_coordinates = []
        self.x, self.y = head.x, head.y


    def spawn(self):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height))

    def update_coordinate(self, head):
        if head.need_coordinates:
            self.x, self.y = head.need_coordinates[0]



class Apple(Snake):
    def __init__(self, head):
        super().__init__()
        self.speed = 0
        self.x = randint(0, SCREEN_WIDTH)
        self.y = randint(0, SCREEN_HEIGHT)
        self.head_x = head.x
        self.head_y = head.y

    def spawn(self):
        if self.x == self.head_x and self.y == self.head_y:
            self.x = randint(0, SCREEN_WIDTH)
            self.y = randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), RADIUS)

    def add_piece_ass(self, head):
        if self.x + RADIUS == head.x or head.x + RADIUS == head.y:
            AssSnake(head)

