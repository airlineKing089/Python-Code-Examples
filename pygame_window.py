# pygame window example

import pygame

win_width = 500
win_height = 500
win_caption = 'Pygame Window Example'
win_icon = 'icon.ico'

pygame.init()

pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption(win_caption)
pygame.display.set_icon(win_icon)

while True:
  pygame.display.update()
