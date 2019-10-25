import time, datetime, calendar
import pygame, sys, random
from pygame.locals import *
from Main_Custom import *
from Main_Custom import display_Image
from Titles_Custom import *

def select_Home_Status(header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    VERT_OFFSET = 70
    DIVISOR = 8
    
    STATUS = header_Font.render('STATUS', True, COLOUR)
    STATUS_rect = STATUS.get_rect(center=((SCREEN_X/DIVISOR)*1, VERT_OFFSET))

    SCREEN.blit(STATUS, STATUS_rect)

def select_Home_Menu_Time(middle_Box_Text_Start, time_Font, footer_Font, SCREEN, SCREEN_X, SCREEN_Y, COLOUR, FADED_COLOUR):
    TIME = time_Font.render((datetime.datetime.now().strftime('%H:%M:%S')), True, COLOUR)
    TIME_rect = TIME.get_rect(center=((SCREEN_X/1.4), (SCREEN_Y/3.4)))

    string = (datetime.datetime.today().strftime('%A') + " ")
    string += datetime.datetime.now().strftime('%d-%b-%Y')
    
    DATE = footer_Font.render(string, True, COLOUR)
    DATE_rect = DATE.get_rect(center=(550, 690))

    SCREEN.blit(TIME, TIME_rect)
    SCREEN.blit(DATE, DATE_rect)

def select_Home_Menu_Table(box_Gap, box_Width, box_Height, middle_Box_Start, middle_Box, end_Box_Start, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):
    WIDTH = 3
    HEIGHT = 300
    # Background
    pygame.draw.rect(SCREEN, FADED_COLOUR, Rect(450, 350, (middle_Box+20), 300))

    # Rows
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 350, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 425, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 500, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 575, (middle_Box+20), WIDTH))
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 650, (middle_Box+20), WIDTH))
    # Columns
    pygame.draw.rect(SCREEN, COLOUR, Rect(450, 350, WIDTH, HEIGHT))
    pygame.draw.rect(SCREEN, COLOUR, Rect(850, 350, WIDTH, HEIGHT))
    pygame.draw.rect(SCREEN, COLOUR, Rect(1067, 350, WIDTH, HEIGHT))

def select_Home_Menu_Table_Info(temperature, humidity, pressure, altitude, footer_Font, SCREEN, SCREEN_X, SCREEN_Y, COLOUR):
    left_Box_X = 550
    right_Box_X = 900
    TEMPERATURE = footer_Font.render("Temperature:", True, COLOUR)
    TEMPERATURE_rect = TEMPERATURE.get_rect(center=(left_Box_X, 390))
    TEMP_2 = footer_Font.render(str(temperature), True, COLOUR)
    TEMP_2_rect = TEMP_2.get_rect(center=(right_Box_X, 390))

    HUMIDITY = footer_Font.render("Humidity:", True, COLOUR)
    HUMIDITY_rect = HUMIDITY.get_rect(center=(left_Box_X-23, 465))
    HUMIDITY_2 = footer_Font.render(str(humidity), True, COLOUR)
    HUMIDITY_2_rect = HUMIDITY.get_rect(center=((right_Box_X+43), 465))

    PRESSURE = footer_Font.render("Pressure:", True, COLOUR)
    PRESSURE_rect = PRESSURE.get_rect(center=((left_Box_X-24), 540))
    PRESSURE_2 = footer_Font.render(str(pressure), True, COLOUR)
    PRESSURE_2_rect = PRESSURE.get_rect(center=((right_Box_X+41), 540))

    ALTITUDE = footer_Font.render("Altitude:", True, COLOUR)
    ALTITUDE_rect = ALTITUDE.get_rect(center=((left_Box_X-24), 615))
    ALTITUDE_2 = footer_Font.render(str(altitude), True, COLOUR)
    ALTITUDE_2_rect = ALTITUDE.get_rect(center=((right_Box_X+41), 615))

    SCREEN.blit(TEMPERATURE, TEMPERATURE_rect)
    SCREEN.blit(TEMP_2, TEMP_2_rect)
    SCREEN.blit(HUMIDITY, HUMIDITY_rect)
    SCREEN.blit(HUMIDITY_2, HUMIDITY_2_rect)
    SCREEN.blit(PRESSURE, PRESSURE_rect)
    SCREEN.blit(PRESSURE_2, PRESSURE_2_rect)
    SCREEN.blit(ALTITUDE, ALTITUDE_rect)
    SCREEN.blit(ALTITUDE_2, ALTITUDE_2_rect)

def bottom_Banner_Home(humidity, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, header_Font, SCREEN, SCREEN_X, COLOUR, FADED_COLOUR):   
    string = "HUMIDITY: " + str(humidity)
    WEATHER = footer_Font.render(string, True, COLOUR)
    WEATHER_rect = WEATHER.get_rect(center=(first_Box_Text_Start+20, 690))

    LOCATION = footer_Font.render('SPOFFORTH', True, COLOUR)
    LOCATION_rect = LOCATION.get_rect(center=(end_Box_Text_Start, 690))

    SCREEN.blit(WEATHER, WEATHER_rect)
    SCREEN.blit(LOCATION, LOCATION_rect)

def select_Home_Menu_Animation(SCREEN, image_Delay, image_Pointer, select_Weather_Animation):
    lightning_Animation = ["Lightning0.png", "Lightning1.png", "Lightning2.png", "Lightning3.png"]
    cloudy_Animation = ["Cloudy0.png", "Cloudy1.png"]
    raining_Animation = ["Raining0.png", "Raining1.png", "Raining2.png"]
    sunny_Animation = ["Sunny0.png", "Sunny1.png", "Sunny2.png", "Sunny3.png", "Sunny4.png", "Sunny5.png", "Sunny6.png", "Sunny7.png", "Sunny8.png"]
    night_Animation = ["Night0.png"]
    snowing_Animation = ["Snowing0.png", "Snowing1.png", "Snowing2.png"]
    windy_Animation = ["Windy0.png", "Windy1.png"]
    fog_Animation = ["Fog0.png", "Fog1.png"]
    snowAndRain_Animation = ["SnowAndRain0.png"]

    x_Offset = 100
    y_Offset = 200
    speed = 150
    if select_Weather_Animation != 0:
        pass
    else:
        select_Weather_Animation = random.randint(1,10)
    
    if select_Weather_Animation == 1:
        image = lightning_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 3:
                image_Pointer = 0
        
    elif select_Weather_Animation == 2:
        image = cloudy_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 1:
                image_Pointer = 0
            
    elif select_Weather_Animation == 3:
        image = raining_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 2:
                image_Pointer = 0
            
    elif select_Weather_Animation == 4:
        image = sunny_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 8:
                image_Pointer = 0
            
    elif select_Weather_Animation == 5:
        image = night_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 0:
                image_Pointer = 0
            
    elif select_Weather_Animation == 6:
        image = snowing_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 2:
                image_Pointer = 0
            
    elif select_Weather_Animation == 7:
        image = windy_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 1:
                image_Pointer = 0
            
    elif select_Weather_Animation == 8:
        image = fog_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 1:
                image_Pointer = 0
            
    elif select_Weather_Animation == 9:
        image = snowAndRain_Animation[image_Pointer]
        display_Image(SCREEN, image, x_Offset, y_Offset)
        if image_Delay == speed:
            image_Pointer += 1
            if image_Pointer > 0:
                image_Pointer = 0

    image_Delay -= 1
    if image_Delay == 0:
        image_Delay = speed
    return image_Delay, select_Weather_Animation, image_Pointer

