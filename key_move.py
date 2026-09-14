# import pygame
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 moving_left = True
#
#             if event.key == pygame.K_RIGHT:
#                 moving_right = True
#
#             if event.key == pygame.K_UP:
#                 moving_up = True
#
#             if event.key == pygame.K_DOWN:
#                 moving_down = True
#
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 moving_left = False
#
#             if event.key == pygame.K_RIGHT:
#                 moving_right = False
#
#             if event.key == pygame.K_UP:
#                 moving_up = False
#
#             if event.key == pygame.K_DOWN:
#                 moving_down = False
#
#     if moving_left:
#         x -= STEP
#
#     if moving_right:
#         x += STEP
#
#     if moving_up:
#         y -= STEP
#
#     if moving_down:
#         y += STEP