import time

import pygame, sys

from random import randint

import pygame.time
from pygame.version import PygameVersion

from snake import *

from DEV.my_games.first_project.snake import HeadSnake
from constants import *


pygame.init()

clock = pygame.time.Clock()

game_over = pygame.font.Font(None, 50)

head = HeadSnake()
ass = AssSnake(head)
apple = Apple()

pygame.display.set_caption("THE SNAKE")

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head.direction = "left"
            elif event.key == pygame.K_RIGHT:
                head.direction = "right"
            elif event.key == pygame.K_UP:
                head.direction = "up"
            elif event.key == pygame.K_DOWN:
                head.direction = "down"


    SCREEN.fill(color="White")

    head.move()
    ass.add_ass(head, apple)
    apple.spawn()
    head.spawn()
    ass.spawn(head)


    clock.tick(10)
    pygame.display.update()

    if len(ass.ass_length) > 2:
        game = False

game_over_text = game_over.render("GAME OVER", True, "black")
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
SCREEN.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()
