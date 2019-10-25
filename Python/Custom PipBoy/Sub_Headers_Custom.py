import time, datetime, calendar
#import board
#import busio
#import adafruit_sht31d
#import adafruit_bmp280
import pygame, sys, random
from pygame.locals import *
from Main_Custom import *
from Titles_Custom import *
from Home_Sub_Headers import *
from Holotape_Sub_Headers import *
from Settings_Sub_Headers import *

def output_Sub_Headers(rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, time_Font, footer_Font, header_Font, GREEN, FADED_GREEN, SCREEN_X, SCREEN_Y, SCREEN, rotary_Switch_Position, rotary_Encoder_Position):
    # Home
    if rotary_Switch_Position == 1:
        if rotary_Encoder_Position == 1:
            image_Delay, select_Weather_Animation, image_Pointer = select_Home_Overall(temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, time_Font, SCREEN_Y, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
#        elif rotary_Encoder_Position == 2:
#            pass
        else:
            image_Delay, select_Weather_Animation, image_Pointer = select_Home_Overall(temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, time_Font, SCREEN_Y, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
            
    # Holotape            
    elif rotary_Switch_Position == 2:
        select_Holotape_Overall(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR)
        if hatch_State == True:
            if tape_Detected == True:
                tape = which_Tape_Detect()
                if tape == 1:
                    pass
                elif tape == 2:
                    pass
            else:
                select_Holotape_Overall(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR)
        else:
            show_Close_Message(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR)

    # Custom    
    elif rotary_Switch_Position == 3:
        if rotary_Encoder_Position == 1:
            pass
        elif rotary_Encoder_Position == 2:
            pass
        else:
            pass

    # Settings    
    elif rotary_Switch_Position == 4:
        set_Base_Settings_Table(header_Font, footer_Font, box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
        # Edits the colours of the pipboy
        if rotary_Encoder_Position == 1:
            select_Colour_Settings(footer_Font, SCREEN, COLOUR)
            if rotary_Encoder2_Position == 1:
                COLOUR, FADED_COLOUR = set_Green_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, GREEN, FADED_GREEN)
            elif rotary_Encoder2_Position == 2:
                COLOUR, FADED_COLOUR = set_Red_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, RED, FADED_RED)
            elif rotary_Encoder2_Position == 3:
                COLOUR, FADED_COLOUR = set_Blue_Colour(footer_Font, SCREEN, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE)
        #
        elif rotary_Encoder_Position == 2:
            if rotary_Encoder2_Position == 1:
                pass
            elif rotary_Encoder2_Position == 2:
                pass
            elif rotary_Encoder2_Position == 3:
                pass
        else:
            pass

    return image_Delay, select_Weather_Animation, image_Pointer, COLOUR, FADED_COLOUR
  

### Overall sub-menu screens ###

def select_Home_Overall(temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, time_Font, SCREEN_Y, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    select_Home_Status(header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
    background_Banner_Boxes(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
    bottom_Banner_Home(humidity, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
    select_Home_Menu_Time(middle_Box_Text_Start, time_Font, footer_Font, SCREEN, SCREEN_X, SCREEN_Y, COLOUR, FADED_COLOUR)
    image_Delay, select_Weather_Animation, image_Pointer = select_Home_Menu_Animation(SCREEN, image_Delay, image_Pointer, select_Weather_Animation)
    select_Home_Menu_Table(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)
    select_Home_Menu_Table_Info(temperature, humidity, pressure, altitude, footer_Font, SCREEN, SCREEN_X, SCREEN_Y, COLOUR)
    return image_Delay, select_Weather_Animation, image_Pointer

def select_Holotape_Overall(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR):
    show_Holotape_Empty(header_Font, footer_Font, SCREEN, SCREEN_X, COLOUR)

def select_Settings_Main(header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    pass

### BOTTOM BANNERS ###

def background_Banner_Boxes(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    pygame.draw.rect(SCREEN, FADED_COLOUR, Rect(box_Gap, 670, box_Width, box_Height))
    pygame.draw.rect(SCREEN, FADED_COLOUR, Rect(middle_Box_Start, 670, middle_Box, box_Height))
    pygame.draw.rect(SCREEN, FADED_COLOUR, Rect(end_Box_Start, 670, box_Width, box_Height))



def bottom_Banner_Holotape(footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    background_Banner_Boxes(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)

def bottom_Banner_Custom(footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    pass

def bottom_Banner_Settings(footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    background_Banner_Boxes(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR)




