import time, datetime, calendar
import pygame, sys, random
from pygame.locals import *
from Main_Custom import *
from Titles_Custom import *

def show_Holotape_Empty(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR):    
    EMPTY = header_Font.render('NO HOLOTAPE DETECTED', True, COLOUR)
    EMPTY_rect = EMPTY.get_rect(center=(525, 90))

    INSERT = footer_Font.render('PLEASE INSERT A HOLOTAPE', True, COLOUR)
    INSERT_rect = INSERT.get_rect(center=(530, 550))

    SCREEN.blit(EMPTY, EMPTY_rect)
    SCREEN.blit(INSERT, INSERT_rect)

def show_Close_Message(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR):
    CLOSE_1 = header_Font.render('PLEASE CLOSE THE', True, COLOUR)
    CLOSE_1_rect = CLOSE_1.get_rect(center=(525, 240))
    CLOSE_2 = header_Font.render('HOLOTAPE TRAY', True, COLOUR)
    CLOSE_2_rect = CLOSE_2.get_rect(center=(530, 280))

    SCREEN.blit(CLOSE_1, CLOSE_1_rect)
    SCREEN.blit(CLOSE_2, CLOSE_2_rect)

def which_Tape_Detect():
    pass
