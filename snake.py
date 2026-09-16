from random import randint, choice

from constants import *

import pygame


class Snake:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = SIZE
        self.height = SIZE
        self.color = choice(COLORS)




class HeadSnake(Snake):
    def __init__(self):
        super().__init__()
        self.x = randint(0, GREED_WIDTH) * GREED_SIZE
        self.y = randint(0, GREED_HEIGHT) * GREED_SIZE
        self.speed = SPEED
        self.direction = "up"
        self.position =[(self.x, self.y )]

    def spawn(self):
        pygame.draw.rect(SCREEN, self.color,(self.x,self.y, SIZE, SIZE))



    def move(self):
        if self.direction == "left":
            self.x -= SPEED
        elif self.direction == "right":
            self.x += SPEED
        elif self.direction == "up":
            self.y -= SPEED
        elif self.direction == "down":
            self.y += SPEED

        self.update_position()

    def update_position(self):
        if self.x >= SCREEN_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = SCREEN_WIDTH - GREED_SIZE
        if self.y >= SCREEN_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = SCREEN_HEIGHT - GREED_SIZE

        self.position.insert(0, (self.x, self.y))




class AssSnake(Snake):
    def __init__(self, head):
        super().__init__()
        self. ass_length = []



    def add_ass(self, head,apple):
        if apple.x == head.x and apple.y == head.y:
            apple.x = randint(0, GREED_WIDTH) * GREED_SIZE
            apple.y = randint(0, GREED_HEIGHT) * GREED_SIZE

            new_segment = Snake()
            self.ass_length.append(new_segment)

    def spawn(self,head):
        max_length = len(self.ass_length) + 1
        if len(head.position) > max_length:
            head.position.pop()



        for index, segment in enumerate(self.ass_length):
            # Индекс + 1, так как на 0-й позиции всегда сама голова
            if index + 1 < len(head.position):
                segment.x, segment.y = head.position[index + 1]
                pygame.draw.rect(SCREEN, segment.color, (segment.x, segment.y, SIZE, SIZE))




class Apple(Snake):
    def __init__(self):
        super().__init__()
        self.x = randint(0, GREED_WIDTH) * GREED_SIZE
        self.y = randint(0, GREED_HEIGHT) * GREED_SIZE


    def spawn(self):
        pygame.draw.rect(SCREEN, self.color,(self.x,self.y, SIZE, SIZE))


