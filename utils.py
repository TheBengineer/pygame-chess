import pygame
from pygame.locals import *
import queue


class Utils:
    @staticmethod
    def get_mouse_event():
        # get coordinates of the mouse
        position = pygame.mouse.get_pos()

        # return left click status and mouse coordinates
        return position

    @staticmethod
    def left_click_event():
        # store mouse buttons
        mouse_btn = pygame.mouse.get_pressed()
        # create flag to check for left click event
        left_click = False

        if mouse_btn[0]:  # and e.button == 1:
            # change left click flag
            left_click = True

        return left_click
