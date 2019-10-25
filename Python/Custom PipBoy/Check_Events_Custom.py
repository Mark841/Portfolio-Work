import time
#import board
#import busio
#import adafruit_sht31d
#import adafruit_bmp280
import pygame, sys, random
import RPi.GPIO as GPIO
from pygame.locals import *
from Main_Custom import *
from Titles_Custom import *

### A function to check if there are any inputs ###
def Check_Events(counter_1, counter_2, enc_1_A, enc_1_B, enc_2_A, enc_2_B, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position, SCREEN, BLACK):
    for event in pygame.event.get(): 
        rotary_Switch_Position = check_Switch_Events(rotary_Switch_Position)
        counter_1, rotary_Encoder_Position = check_Encoder_Events(rotary_Encoder_Position, counter_1, enc_1_A, enc_1_B)
        counter_2, rotary_Encoder2_Position = check_Encoder2_Events(rotary_Encoder2_Position, counter_2, enc_2_A, enc_2_B)
    SCREEN.fill(BLACK)
    return counter_1, counter_2, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position

### Checks switch inputs ###
def check_Switch_Events(rotary_Switch_Position):
    if GPIO.input(7):
        rotary_Switch_Position = 1
    elif GPIO.input(8):
        rotary_Switch_Position = 2
    elif GPIO.input(9):
        rotary_Switch_Position = 3
    elif GPIO.input(10):
        rotary_Switch_Position = 4
    return rotary_Switch_Position

### Checks encoder inputs ###
def check_Encoder_Events(rotary_Encoder_Position, counter_1, enc_1_A, enc_1_B): 
    Switch_A = GPIO.input(enc_1_A)
    Switch_B = GPIO.input(enc_1_B)

    if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
        counter_1 += 1
        rotary_Encoder_Position += 1
        print ("direction -> ", counter_1)
        # at this point, B may still need to go high, wait for it
        while Switch_B == 0:
            Switch_B = GPIO.input(enc_1_B)
        # now wait for B to drop to end the click cycle
        while Switch_B == 1:
            Switch_B = GPIO.input(enc_1_B)
        return counter_1, rotary_Encoder_Position

    elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
        counter_1 -= 1
        rotary_Encoder_Position -= 1
        print ("direction <- ", counter_1)
         # A is already high, wait for A to drop to end the click cycle
        while Switch_A == 1:
            Switch_A = GPIO.input(enc_1_A)
        return counter_1, rotary_Encoder_Position

    else: # discard all other combinations
        return counter_1, rotary_Encoder_Position

def check_Encoder2_Events(rotary_Encoder2_Position, counter_2, enc_2_A, enc_2_B): 
    Switch_A = GPIO.input(enc_2_A)
    Switch_B = GPIO.input(enc_2_B)

    if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
        counter_2 += 1
        rotary_Encoder2_Position += 1
        print ("direction -> ", counter_2)
        # at this point, B may still need to go high, wait for it
        while Switch_B == 0:
            Switch_B = GPIO.input(enc_2_B)
        # now wait for B to drop to end the click cycle
        while Switch_B == 1:
            Switch_B = GPIO.input(enc_2_B)
        return counter_2, rotary_Encoder2_Position

    elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
        counter_2 -= 1
        rotary_Encoder2_Position -= 1
        print ("direction <- ", counter_2)
         # A is already high, wait for A to drop to end the click cycle
        while Switch_A == 1:
            Switch_A = GPIO.input(enc_2_A)
        return counter_2, rotary_Encoder2_Position

    else: # discard all other combinations
        return counter_2, rotary_Encoder2_Position



def check_Holotape_Inserted():
    pass






'''
### KEYBOARD INPUTS ###
def Check_Events(counter_1, counter_2, enc_1_A, enc_1_B, enc_2_A, enc_2_B, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position, SCREEN, BLACK):
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If the close button is clicked
            sys.exit() 
        elif event.type == pygame.KEYDOWN: # If a key is pressed down on the keyboard
            rotary_Switch_Position, rotary_Encoder_Position = check_Switch_Events(event, rotary_Switch_Position, rotary_Encoder_Position)
            rotary_Encoder_Position = check_Encoder_Events(event, rotary_Encoder_Position, counter_1, enc_1_A, enc_1_B)
            counter, rotary_Encoder2_Position = check_Encoder2_Events(event, rotary_Encoder2_Position, counter_2, enc_2_A, enc_2_B)
    SCREEN.fill(BLACK)
    return counter, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position

def check_Switch_Events(event, old_Rotary_Switch_Position, rotary_Encoder_Position):
    rotary_Switch_Position = old_Rotary_Switch_Position
    if event.key == ord('2'):
        rotary_Switch_Position += 1
    elif event.key == ord('1'):
        rotary_Switch_Position -= 1    
    elif event.key == K_ESCAPE: # Check if the escape key was pressed
        pygame.event.post(pygame.event.Event(QUIT))
        pygame.quit()
    ### Validation ###
    if rotary_Switch_Position >= 4:
        rotary_Switch_Position = 4
    elif rotary_Switch_Position <= 1:
        rotary_Switch_Position = 1
    if old_Rotary_Switch_Position != rotary_Switch_Position:
        rotary_Encoder_Position = 1
    else:
        pass
    return rotary_Switch_Position, rotary_Encoder_Position

def check_Encoder_Events(event, rotary_Encoder_Position): 
    if event.key == ord('6'): 
        rotary_Encoder_Position += 1
    elif event.key == ord('5'): 
        rotary_Encoder_Position -= 1
    ### Validation ###    
    if rotary_Encoder_Position >= 5:
        rotary_Encoder_Position = 5
    elif rotary_Encoder_Position <= 1:
        rotary_Encoder_Position = 1
    return rotary_Encoder_Position

def check_Encoder2_Events(event, rotary_Encoder2_Position): 
    if event.key == ord('9'): 
        rotary_Encoder2_Position += 1
    elif event.key == ord('8'): 
        rotary_Encoder2_Position -= 1
    ### Validation ###    
    if rotary_Encoder2_Position >= 5:
        rotary_Encoder2_Position = 5
    elif rotary_Encoder2_Position <= 1:
        rotary_Encoder2_Position = 1
    return rotary_Encoder2_Position
'''
