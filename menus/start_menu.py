import pygame
from menus.menu import Menu
from menus.button import Button

class Start_Menu(Menu):

    def __init__(self):
       pass

    def draw_text(self, text, font, text_col, x, y, screen):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

    def draw_menu(self):
        return 