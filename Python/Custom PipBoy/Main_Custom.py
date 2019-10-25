import time, datetime
#import board
#import busio
#import adafruit_sht31d
#import adafruit_bmp280
import pygame, sys, random
import RPi.GPIO as GPIO
from pygame.locals import *
from Titles_Custom import *
from Sub_Headers_Custom import *
from Check_Events_Custom import *

#def Run(i2c, sensor, bmp280):
### Runs the program ###
def Run():
    #rotary_Encoder = int(input("Enter encoder setting: "))
    rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, image_Delay, select_Weather_Animation, image_Pointer, time_Font, temperature, humidity, pressure, altitude, BUFFER, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, buffer_Tracker, y_Coord, frameRate, SCREEN_X, SCREEN_Y, SCREEN, RED, BLACK, WHITE, GREY, GREEN, FADED_GREEN, rotary_Switch_Position, rotary_Encoder_Position, header_Font = setup_Screen()
    counter_1, counter_2, enc_1_A, enc_1_B, enc_2_A, enc_2_B = setup_Encoders()
    
    '''
    ### Runs the opening animation ###
    initialising_Animation = ["Initialising1.png", "Initialising2.png", "Initialising3.png", "Initialising4.png", "Initialising5.png", "Initialising6.png", "Initialising7.png", "Initialising8.png", "Initialising9.png", "Initialising10.png", "Initialising11.png", "Initialising12.png", "Initialising13.png", "Initialising14.png", "Initialising15.png", "Initialising16.png"]
    run_Animation(SCREEN, initialising_Animation, 36, 0.4)
    '''    
    while True:
        for count in range(1,27):
            print(GPIO.input(27))
        
        ### Checks where the dials are set to and opens the corresponding menu for that position ###
        counter_1, counter_2, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position = Check_Events(counter_1, counter_2, enc_1_A, enc_1_B, enc_2_A, enc_2_B, rotary_Switch_Position, rotary_Encoder_Position, rotary_Encoder2_Position, SCREEN, BLACK)
        check_Holotape_Inserted()
        temperature, humidity, pressure, altitude = get_Sensor_Input(i2c, sensor, bmp280)
        output_Headers(header_Font, COLOUR, SCREEN_X, SCREEN)
        if rotary_Switch_Position == 1:
            select_Home(SCREEN, SCREEN_X, COLOUR)
            image_Delay, select_Weather_Animation, image_Pointer, COLOUR, FADED_COLOUR = output_Sub_Headers(rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, time_Font, footer_Font, header_Font, GREEN, FADED_GREEN, SCREEN_X, SCREEN_Y, SCREEN, rotary_Switch_Position, rotary_Encoder_Position)
        elif rotary_Switch_Position == 2:
            select_Holotape(SCREEN, SCREEN_X, COLOUR)
            image_Delay, select_Weather_Animation, image_Pointer, COLOUR, FADED_COLOUR = output_Sub_Headers(rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, time_Font, footer_Font, header_Font, GREEN, FADED_GREEN, SCREEN_X, SCREEN_Y, SCREEN, rotary_Switch_Position, rotary_Encoder_Position)
        elif rotary_Switch_Position == 3:
            select_Custom(SCREEN, SCREEN_X, COLOUR)
            image_Delay, select_Weather_Animation, image_Pointer, COLOUR, FADED_COLOUR = output_Sub_Headers(rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, time_Font, footer_Font, header_Font, GREEN, FADED_GREEN, SCREEN_X, SCREEN_Y, SCREEN, rotary_Switch_Position, rotary_Encoder_Position)
        elif rotary_Switch_Position == 4:
            select_Settings(SCREEN, SCREEN_X, COLOUR)
            image_Delay, select_Weather_Animation, image_Pointer, COLOUR, FADED_COLOUR = output_Sub_Headers(rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, temperature, humidity, pressure, altitude, image_Delay, select_Weather_Animation, image_Pointer, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, time_Font, footer_Font, header_Font, GREEN, FADED_GREEN, SCREEN_X, SCREEN_Y, SCREEN, rotary_Switch_Position, rotary_Encoder_Position)
        else:
            continue
        
        ### Creates the green refresh line that goes vertically down the screen ###
        if BUFFER == True:
            screen_Buffer(y_Coord, SCREEN, GREEN, SCREEN_X)
            if y_Coord > SCREEN_Y:
                y_Coord = 0
            if buffer_Tracker !=2:
                buffer_Tracker += 1
            else:
                y_Coord += 1
                buffer_Tracker = 0
        
        #get_Sensor_Input(i2c, sensor, bmp280)
        update_Screen()

### Variable initialisation ###
def setup_Screen():
    pygame.init()
    BUFFER = False
    buffer_Tracker = 0
    y_Coord = 0
    frameRate = pygame.time.Clock()
    SCREEN_X = 1080
    SCREEN_Y = 720
    SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('PipBoy')

    box_Height = 40
    box_Width = 220
    box_Gap = 10
    middle_Box_Start = box_Width + (2*box_Gap)
    middle_Box = SCREEN_X - (2*box_Width) - (4*box_Gap)
    end_Box_Start = SCREEN_X - box_Width - box_Gap
    
    first_Box_Text_Start = box_Gap + 70
    middle_Box_Text_Start = middle_Box_Start + 70
    end_Box_Text_Start = end_Box_Start + 133

    image_Pointer = 0
    select_Weather_Animation = 0
    image_Delay = 150

    RED = pygame.Color(255, 0, 0)
    FADED_RED = pygame.Color(131, 1, 1) 
    BLACK = pygame.Color(0, 0, 0) 
    WHITE = pygame.Color(255, 255, 255) 
    GREY = pygame.Color(150, 150, 150) 
    GREEN = pygame.Color(0, 255, 0)
    FADED_GREEN = pygame.Color(41, 89, 32)
    BLUE = pygame.Color(0, 230, 255)
    FADED_BLUE = pygame.Color(0, 120, 134)
    COLOUR = GREEN
    FADED_COLOUR = FADED_GREEN

    rotary_Switch_Position = 1
    rotary_Encoder_Position = 1
    rotary_Encoder2_Position = 1

    header_Font = pygame.font.Font('freesansbold.ttf', 36)
    footer_Font = pygame.font.Font('freesansbold.ttf', 24)
    time_Font = pygame.font.Font('freesansbold.ttf', 140)

    temperature = 30
    humidity = 30
    pressure = 30
    altitude = 30

    hatch_State = True
    tape_Detected = True

    #i2c = busio.I2C(board.SCL, board.SDA)
    #sensor = adafruit_sht31d.SHT31D(i2c)
    #bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
    
    return rotary_Encoder2_Position, COLOUR, FADED_COLOUR, BLUE, FADED_BLUE, RED, FADED_RED, hatch_State, tape_Detected, image_Delay, select_Weather_Animation, image_Pointer, time_Font, temperature, humidity, pressure, altitude, BUFFER, footer_Font, first_Box_Text_Start, middle_Box_Text_Start, end_Box_Text_Start, box_Height, box_Width, box_Gap, middle_Box_Start, middle_Box, end_Box_Start, buffer_Tracker, y_Coord, frameRate, SCREEN_X, SCREEN_Y, SCREEN, RED, BLACK, WHITE, GREY, GREEN, FADED_GREEN, rotary_Switch_Position, rotary_Encoder_Position, header_Font

def setup_Encoders():
    enc_1_A = 2 
    enc_1_B = 3
    enc_2_A = 4 
    enc_2_B = 5
    counter_1 = 10
    counter_2 = 10
    
    GPIO.setwarnings(True)

    # Use the Raspberry Pi BCM pins
    GPIO.setmode(GPIO.BCM)

    # define the Encoder switch inputs
    GPIO.setup(enc_1_A, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.setup(enc_1_B, GPIO.IN)
    GPIO.setup(enc_2_A, GPIO.IN) 
    GPIO.setup(enc_2_B, GPIO.IN)

    # setup an event detection thread for the A encoder switch
    GPIO.add_event_detect(enc_1_A, GPIO.RISING, callback=rotation_decode, bouncetime=2) # bouncetime in mSec
    GPIO.add_event_detect(enc_2_A, GPIO.RISING, callback=rotation_decode, bouncetime=2)
    #
    return counter_1, counter_2, enc_1_A, enc_1_B, enc_2_A, enc_2_B

### Runs an animation ###
def run_Animation(SCREEN, animation, y_Offset, frame_delay):
    for count in range(0, len(animation)):
        image = pygame.image.load(animation[count])
        SCREEN.blit(image, (0,y_Offset))
        update_Screen()
        time.sleep(frame_delay)

### Displays an image ###
def display_Image(SCREEN, image, x_Offset, y_Offset):
    IMAGE = pygame.image.load(image)
    SCREEN.blit(IMAGE, (x_Offset,y_Offset))

### Runs a green line down the screen ###
def screen_Buffer(y_Coord, SCREEN, COLOUR, SCREEN_X):
    pygame.draw.rect(SCREEN, COLOUR, Rect(0, y_Coord, SCREEN_X, 3))

### Updates the screen with any changes ###
def update_Screen():
    pygame.display.flip()

### Gets the sensor input from the sensors ###
def get_Sensor_Input(i2c, sensor, bmp280):
    bmp280.sea_level_pressure = 1020.92
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    pressure = bmp280.pressure
    altitude = bmp280.altitude
    
    print("\nTemperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % humidity)
    print("Pressure: %0.1f hPa" % pressure)
    print("Altitude: %0.2f meters" % altitude)

    return temperature, humidity, pressure, altitude

    

if __name__ in "__main__":
    # Create library object using the Bus I2C port
    #i2c = busio.I2C(board.SCL, board.SDA)
    #sensor = adafruit_sht31d.SHT31D(i2c)
    #bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
    #Run(i2c, sensor, bmp280)

    Run()
