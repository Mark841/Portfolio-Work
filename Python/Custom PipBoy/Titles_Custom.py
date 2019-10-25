import time, datetime
#import board
#import busio
#import adafruit_sht31d
#import adafruit_bmp280
import pygame, sys, random
from pygame.locals import *

def output_Headers(header_Font, COLOUR, SCREEN_X, SCREEN):
    VERT_OFFSET = 25
    DIVISOR = 8
    
    HOME = header_Font.render('HOME', True, COLOUR)
    HOME_rect = HOME.get_rect(center=((SCREEN_X/DIVISOR)*1, VERT_OFFSET))

    HOLOTAPE = header_Font.render('HOLOTAPE', True, COLOUR)
    HOLOTAPE_rect = HOLOTAPE.get_rect(center=((SCREEN_X/DIVISOR)*2.75, VERT_OFFSET))

    CUSTOM = header_Font.render('CUSTOM', True, COLOUR)
    CUSTOM_rect = CUSTOM.get_rect(center=((SCREEN_X/DIVISOR)*4.7, VERT_OFFSET))

    SETTINGS = header_Font.render('SETTINGS', True, COLOUR)
    SETTINGS_rect = SETTINGS.get_rect(center=((SCREEN_X/DIVISOR)*6.5, VERT_OFFSET))

    SCREEN.blit(HOME, HOME_rect)
    SCREEN.blit(HOLOTAPE, HOLOTAPE_rect)
    SCREEN.blit(CUSTOM, CUSTOM_rect)
    SCREEN.blit(SETTINGS, SETTINGS_rect)

def select_Home(SCREEN, SCREEN_X, COLOUR):
    DIVISOR_1 = 15.5
    DIVISOR_2 = 5.65
    WIDTH = 3
    HEIGHT = 8
    # Left
    pygame.draw.rect(SCREEN, COLOUR, Rect(0, 40, SCREEN_X/DIVISOR_1, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, HEIGHT, WIDTH))
    # Right#
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_2, 25, HEIGHT, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT-WIDTH), 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT), 40, (SCREEN_X-((SCREEN_X/DIVISOR_2)+HEIGHT)), WIDTH))

def select_Holotape(SCREEN, SCREEN_X, COLOUR):
    DIVISOR_1 = 4.15
    DIVISOR_2 = 2.275
    WIDTH = 3
    HEIGHT = 8
    # Left
    pygame.draw.rect(SCREEN, COLOUR, Rect(0, 40, SCREEN_X/DIVISOR_1, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, HEIGHT, WIDTH))
    # Right
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_2, 25, HEIGHT, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT-WIDTH), 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT), 40, (SCREEN_X-((SCREEN_X/DIVISOR_2)+HEIGHT)), WIDTH))

def select_Custom(SCREEN, SCREEN_X, COLOUR):
    DIVISOR_1 = 1.98
    DIVISOR_2 = 1.51
    WIDTH = 3
    HEIGHT = 8
    # Left
    pygame.draw.rect(SCREEN, COLOUR, Rect(0, 40, SCREEN_X/DIVISOR_1, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, HEIGHT, WIDTH))
    # Right
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_2, 25, HEIGHT, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT-WIDTH), 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT), 40, (SCREEN_X-((SCREEN_X/DIVISOR_2)+HEIGHT)), WIDTH))

def select_Settings(SCREEN, SCREEN_X, COLOUR):
    DIVISOR_1 = 1.39
    DIVISOR_2 = 1.11
    WIDTH = 3
    HEIGHT = 8
    # Left
    pygame.draw.rect(SCREEN, COLOUR, Rect(0, 40, SCREEN_X/DIVISOR_1, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_1, 25, HEIGHT, WIDTH))
    # Right
    pygame.draw.rect(SCREEN, COLOUR, Rect(SCREEN_X/DIVISOR_2, 25, HEIGHT, WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT-WIDTH), 25, WIDTH, 18))
    pygame.draw.rect(SCREEN, COLOUR, Rect(((SCREEN_X/DIVISOR_2)+HEIGHT), 40, (SCREEN_X-((SCREEN_X/DIVISOR_2)+HEIGHT)), WIDTH))
