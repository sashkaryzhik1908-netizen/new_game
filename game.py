import time

import pygame, sys

from random import randint

from snake import *

from DEV.my_games.first_project.snake import HeadSnake
from constants import *


pygame.init()


game_over = pygame.font.Font(None, 50)

head = HeadSnake()
ass = AssSnake(head)
apple = Apple(head)



pygame.display.set_caption("THE SNAKE")

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                head.is_moving_left = True

            if event.key == pygame.K_RIGHT:
               head.is_moving_right = True

            if event.key == pygame.K_UP:
                head.is_moving_up = True

            if event.key == pygame.K_DOWN:
                head.is_moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                head.is_moving_left = False

            if event.key == pygame.K_RIGHT:
                head.is_moving_right = False

            if event.key == pygame.K_UP:
                head.is_moving_up = False

            if event.key == pygame.K_DOWN:
                head.is_moving_down = False

    if head.is_moving_left:
        head.x -= SPEED

    if head.is_moving_right:
        head.x += SPEED

    if head.is_moving_up:
        head.y -= SPEED

    if head.is_moving_down:
        head.y += SPEED

    SCREEN.fill(color="White")

    head.spawn()
    head.update()
    ass.spawn()
    ass.update_coordinate(head)
    apple.spawn()


    pygame.display.update()


game_over_text = game_over.render("GAME OVER", True, "white")
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
SCREEN.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()
