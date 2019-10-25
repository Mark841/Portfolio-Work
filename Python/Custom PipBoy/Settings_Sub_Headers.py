import time, datetime, calendar
import pygame, sys, random
from pygame.locals import *
from Main_Custom import *
from Titles_Custom import *

def set_Base_Settings_Table(header_Font, footer_Font, box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    WIDTH = 3
    HEIGHT = 300
    # Background
    pygame.draw.rect(SCREEN, FADED_COLOUR, Rect(250, 150, (middle_Box+20), 300))

    # Rows
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 150, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 225, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 300, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 375, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 450, (middle_Box+20), WIDTH))
    # Columns
    pygame.draw.rect(SCREEN, COLOUR, Rect(250, 150, WIDTH, HEIGHT))
    pygame.draw.rect(SCREEN, COLOUR, Rect(557, 150, WIDTH, HEIGHT))
    pygame.draw.rect(SCREEN, COLOUR, Rect(867, 150, WIDTH, HEIGHT))

    SETTINGS = header_Font.render("SETTINGS", True, COLOUR)
    SETTINGS_rect = SETTINGS.get_rect(center=(555, 130))
    SETTING_1 = footer_Font.render("PIPBOY COLOUR", True, COLOUR)
    SETTING_1_rect = SETTING_1.get_rect(center=(370,  190))

    SCREEN.blit(SETTINGS, SETTINGS_rect)
    SCREEN.blit(SETTING_1, SETTING_1_rect)

def select_Colour_Settings(footer_Font, SCREEN, COLOUR):
    pygame.draw.circle(SCREEN, COLOUR, (220, 190), 10)

def set_Green_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, GREEN, FADED_GREEN):
    COLOUR = GREEN
    FADED_COLOUR = FADED_GREEN
    
    SETTINGS = footer_Font.render("GREEN", True, COLOUR)
    SETTINGS_rect = SETTINGS.get_rect(center=(700,  190))

    SCREEN.blit(SETTINGS, SETTINGS_rect)
    return COLOUR, FADED_COLOUR

def set_Red_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, RED, FADED_RED):
    COLOUR = RED
    FADED_COLOUR = FADED_RED
    
    SETTINGS = footer_Font.render("RED", True, COLOUR)
    SETTINGS_rect = SETTINGS.get_rect(center=(700,  190))

    SCREEN.blit(SETTINGS, SETTINGS_rect)
    return COLOUR, FADED_COLOUR

def set_Blue_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE):
    COLOUR = BLUE
    FADED_COLOUR = FADED_BLUE
    
    SETTINGS = footer_Font.render("BLUE", True, COLOUR)
    SETTINGS_rect = SETTINGS.get_rect(center=(700,  190))

    SCREEN.blit(SETTINGS, SETTINGS_rect)
    return COLOUR, FADED_COLOUR
