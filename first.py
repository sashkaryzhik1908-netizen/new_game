import time

import pygame, sys

from random import randint


pygame.init()


game_over = pygame.font.Font(None, 50)

screen_width, screen_height = 1280, 720

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("first game")

# все что касается дороги и разметки
ROAD_WIDTH, ROAD_HEIGH = screen_width/3, screen_height
road_x, road_y = screen_width - ROAD_WIDTH * 2, 0
right_marking_side_width, right_marking_side_heigh = 8,screen_height
right_marking_side_x, right_marking_side_y = screen_width - screen_width / 3 - 20, 0
left_marking_side_width, left_marking_side_heigh = right_marking_side_width, right_marking_side_heigh
left_marking_side_x, left_marking_side_y = screen_width - screen_width / 3 * 2 + 10, 0

# пока тупо, но я это понимаю
marking_center_width, marking_center_heigh = 10, 50
marking_center_x, marking_center_y = road_x + ROAD_WIDTH/2, 0

marking_1_center_y = 100

marking_2_center_y = 200

marking_3_center_y = 300

marking_4_center_y = 400

marking_5_center_y = 500

marking_6_center_y = 600

marking_7_center_y = 700

#Реализация авто игрока
STEP = 2
car_image = pygame.image.load("car.png")
car_width, car_heigh = car_image.get_size()
car_x = road_x * 2 - car_width * 2
car_y = screen_height - car_heigh
car_moving_left = False
car_moving_right = False

#реализация встречных авто

car_1_image = pygame.image.load("car_1.png")
car_1_width, car_1_heigh = car_1_image.get_size()
car_1_x = road_x + car_1_width
car_1_y = 0 - car_1_heigh * (randint(1,4))
car_1_speed = randint(1,2)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_moving_left = True

            if event.key == pygame.K_RIGHT:
                car_moving_right = True
                car_x += STEP


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car_moving_left = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car_moving_right = False



    if car_moving_left and car_x >= STEP + left_marking_side_x:
        car_x -= STEP

    if car_moving_right and car_x <= right_marking_side_x - car_width :
        car_x += STEP


    car_1_y += car_1_speed
    if car_1_y >= screen_height + 1:
        car_1_y = 0 - car_1_heigh * (randint(1,4))
        car_1_speed = randint(1, 2)

    # marking_center_y += car_1_speed
    # marking_1_center_y += car_1_speed
    # marking_2_center_y += car_1_speed
    # marking_3_center_y += car_1_speed
    # marking_4_center_y += car_1_speed
    # marking_5_center_y += car_1_speed
    # marking_6_center_y += car_1_speed
    # marking_7_center_y += car_1_speed
    # if marking_center_y >= screen_height + 1:
    #     marking_center_y = 0
    # if marking_1_center_y >= screen_height + 1 + 100:
    #     marking_1_center_y = marking_center_y - 100
    # if marking_2_center_y >= screen_height + 1 + 200:
    #     marking_2_center_y = marking_center_y - 200
    # if marking_3_center_y >= screen_height + 1 + 300:
    #     marking_3_center_y = marking_center_y - 300
    # if marking_4_center_y >= screen_height + 1 + 400:
    #     marking_4_center_y = marking_center_y - 400
    # if marking_5_center_y >= screen_height + 1 + 500:
    #     marking_5_center_y = marking_center_y - 500
    # if marking_6_center_y >= screen_height + 1 + 600:
    #     marking_6_center_y = marking_center_y - 600
    # if marking_7_center_y >= screen_height + 1 + 700:
    #     marking_7_center_y = marking_center_y - 700

    screen.fill(color="LightGreen")



    pygame.draw.rect(screen, "gray", (road_x, road_y,ROAD_WIDTH, ROAD_HEIGH))
    pygame.draw.rect(screen, "white", (right_marking_side_x, right_marking_side_y, right_marking_side_width, right_marking_side_heigh))
    pygame.draw.rect(screen, "white",
                     (left_marking_side_x, left_marking_side_y, left_marking_side_width, left_marking_side_heigh))



    pygame.draw.rect(screen, "white", (marking_center_x,marking_center_y, marking_center_width, marking_center_heigh ))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_1_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_2_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_3_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_4_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_5_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_6_center_y, marking_center_width, marking_center_heigh))
    pygame.draw.rect(screen, "white", (marking_center_x, marking_7_center_y, marking_center_width, marking_center_heigh))





    screen.blit(car_image,(car_x, car_y))
    screen.blit(car_1_image, (car_1_x, car_1_y))
    pygame.display.update()

    car_rect = pygame.Rect(car_x, car_y, car_image.get_width(), car_image.get_height())
    car_1_rect = pygame.Rect(car_1_x, car_1_y, car_1_image.get_width(), car_1_image.get_height())

    if car_rect.colliderect(car_1_rect):
        car_1_y = -car_1_heigh
        run = False

game_over_text = game_over.render("GAME OVER", True, "white")
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (640,360)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()




