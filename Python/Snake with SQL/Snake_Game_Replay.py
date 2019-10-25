import pygame, sys, time, random # Imports these
from pygame.locals import * # Retrieves all the local constants from pygame
from ViewTables import * # Imports the library functions from ViewTables
from Main import * # Imports the functions from the Main file

global PredDirection, ChangePredDirection # Sets these variables to be global variables

def GameOverREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN): # Creates the GameOverREPLAY function
    GameOverFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    GameOverSurf = GameOverFont.render('Replay Over', True, GREY) # Draws text on the pygame windows surface
    GameOverRect = GameOverSurf.get_rect() # Gets the rectangular area of the game over text surface
    GameOverRect.midtop = (300, 10) # Sets the location of the game over text to be in the center and at the top of the screen
    PlaySurface.blit(GameOverSurf, GameOverRect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

def WonGameREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN): # Creates the WonGameREPLAY function
    WinFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    WinSurf = WinFont.render('Replay Over', True, RED) # Draws text on the pygame windows surface
    WinRect = WinSurf.get_rect() # Gets the rectangular area of the won game text surface
    WinRect.midtop = (450, 10) # Sets the location of the won game text to be in the center and at the top of the screen
    PlaySurface.blit(WinSurf, WinRect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

def InitialiseVariablesREPLAY(): # Is a function that sets up CONSTANT values or initial values
    global PredDirection, ChangePredDirection # Sets these variables to be global variables
    pygame.init() # Initialises all imported pygame modules 
    fpsClock = pygame.time.Clock() # Limits the frame rate of the game
    PlaySurface = pygame.display.set_mode((600, 400)) # Sets the size of the pygame window
    pygame.display.set_caption('Last Snake Replay') # Gives the window a title

    RED = pygame.Color(255, 0, 0) # Sets the red colour
    BLACK = pygame.Color(0, 0, 0) # Sets the black colour
    WHITE = pygame.Color(255, 255, 255) # Sets the white colour
    GREY = pygame.Color(150, 150, 150) # Sets the grey colour
    GREEN = pygame.Color(0, 255, 0) # Sets the green colour

    SnakePosition = [100,100] # Sets the location of the head/front of the snake
    SnakeSegments = [[100,100],[80,100],[60,100]] # Sets the location for each body part of the snake
    RaspberryPosition = [300,300] # Sets the location for the first raspberry
    RaspberrySpawned = 1 # Sets that a raspberry has been created and exists on the surface of the window
    RaspberryCollected = 0 # Sets how many points have been collected

    SnakePredatorPosition = [540,300] # Sets the location of the head/front of the computer controlled snake
    SnakePredatorSegments = [[540,300],[560,300],[580,300]] # Sets the location for each body part of the computer controlled snake
    PredDirection = 'left' # Sets the initial direction of the computer controlled snake to left
    ChangePredDirection = PredDirection # Sets the ChangePredDirection to the same as the direction of motion of the computer controlled snake so it doesn't instantly change direction
    
    return RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection
    # Returns these values to be used when the function is called

def SnakeGameREPLAY(UserID, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection):
    # Is a function to play the replay of the game
    MovesTaken = 0 # Is a variable that holds how many of the moves have been replayed

    x, y = GetRaspLocsForReplay() # Gets two lists of all the x and y coordinates for where the raspberrys were located in the previous game
    MovesRepeat = QueueOfReplayMoves() # Calls a class that stores all the player controlled snakes moves from the last game in a queue
    PredMovesRepeat = QueueOfPredReplayMoves() # Calls a class that stores all the computer controlled snakes moves from the last game in a queue
    
    while True: # Creates an infinite loop
        NextMove = MovesRepeat.remove_item() # Gets the next move from the queue of all the player controlled snakes moves
        MovesTaken += 1 # Adds one to the variable that keeps track of how many moves were played
       
        if NextMove == 'right': # If the next move for the player snake is to the right
            SnakePosition[0] += 20 # Changes the x coordinate of the snakes head to be in the next place on the screen
        if NextMove == 'left': # If the next move for the player snake is to the left
            SnakePosition[0] -= 20   # Changes the x coordinate of the snakes head to be in the next place on the screen
        if NextMove == 'up': # If the next move for the player snake is to go up
            SnakePosition[1] -= 20 # Changes the y coordinate of the snakes head to be in the next place on the screen
        if NextMove == 'down': # If the next move for the player snake is to go down
            SnakePosition[1] += 20 # Changes the y coordinate of the snakes head to be in the next place on the screen

        SnakeSegments.insert(0,list(SnakePosition)) # Inserts into the list of all components of the snake (SnakeSegments) -in the first index value of the list- where the new head of the snake is located on the screen
        if SnakePosition[0] == RaspberryPosition[0] and SnakePosition[1] == RaspberryPosition[1]: # If the player controlled snake goes over a raspberry/score
            RaspberryCollected += 1 # Adds one to the player's score
        else: # If no raspberrys were collected
            SnakeSegments.pop() # Removes the last value from the list (the tail of the snake) of all the components of the snake (SnakeSegments)
            
        for count in range(1,30): # Creates a for loop that goes through 30 times for how many score values were collected in the last game
            if RaspberryCollected == count: # If the amount of raspberrys collected is the same as the amount of times gone through the for loop
                x_coord = x[count-1] # Sets the x coordinate (for the next raspberry to be placed) as being that index number -1 in the list of coordinates
                y_coord = y[count-1] # Sets the y coordinate (for the next raspberry to be placed) as being that index number -1 in the list of coordinates
                RaspberryPosition = [int(x_coord),int(y_coord)] # Combines the two coordinates to make a position for the new raspberry to be placed
            
        PlaySurface.fill(BLACK) # Fills the pygame window to be entirely Black
        for position in SnakeSegments: # For each section of the player controlled snake
            pygame.draw.rect(PlaySurface, WHITE, Rect(position[0], position[1], 20, 20)) # Draw onto the pygame window each of the snakes 'body parts'
            pygame.draw.rect(PlaySurface, RED, Rect(RaspberryPosition[0], RaspberryPosition[1], 20, 20)) # Draw onto the pygame window the new raspberry
        if RaspberryCollected >= 10: # If the player has collected 10 or more raspberrys/score
            for SnakeBody in SnakeSegments[1:]: # For each 'body part' in the player controlled snake
                if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the computer controlled snake
                    WonGameREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls the WonGameREPLAY function to end the replay
        if SnakePosition[0] > 600 or SnakePosition[0] < 0: # Checks if the player controlled snake has gone off the screen in the horizontal direction
            GameOverREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls the GameOverREPLAY function to end the replay
        if SnakePosition[1] > 400 or SnakePosition[1] < 0: # Checks if the player controlled snake has gone off the screen in the vertical direction
            GameOverREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls the GameOverREPLAY function to end the replay

        SnakePredatorREPLAY(UserID, PredMovesRepeat, x, y, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments)
        # Calls the function that controls the SnakePredator (computer controlled snake)
        
        if NextMove == "END": # If the next move off the queue is END, the final move in the queue
            GameOverREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls GameOverREPLAY to end the replay

        fpsClock.tick(20) # Computes in milliseconds how long it has been since this was last called and makes it so the frame rate can never go over 20 frames per second

def SnakePredatorREPLAY(UserID, PredMovesRepeat, x, y, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments):
    # Is a function to play the replay of the computer controlled snake
    global PredDirection, ChangePredDirection # Sets these variables to be global variables

    PredNextMove = PredMovesRepeat.remove_item() # Gets the computers next move from the queue of all the computer controlled snakes moves
    
    if PredNextMove == 'right': # If the next move for the computer snake is to the right
        SnakePredatorPosition[0] += 20 # Changes the x coordinate of the snakes head to be in the next place on the screen
    if PredNextMove == 'left': # If the next move for the computer snake is to the left
        SnakePredatorPosition[0] -= 20 # Changes the x coordinate of the snakes head to be in the next place on the screen   
    if PredNextMove == 'up': # If the next move for the computer snake is to go up
        SnakePredatorPosition[1] -= 20 # Changes the y coordinate of the snakes head to be in the next place on the screen  
    if PredNextMove == 'down': # If the next move for the computer snake is to go down
        SnakePredatorPosition[1] += 20 # Changes the y coordinate of the snakes head to be in the next place on the screen
      
    SnakePredatorSegments.insert(0,list(SnakePredatorPosition)) # Inserts into the list of all components of the snake (SnakePredatorSegments) -in the first index value of the list- where the new head of the snake is located on the screen

    if SnakePredatorPosition[0] == RaspberryPosition[0] and SnakePredatorPosition[1] == RaspberryPosition[1]: # If the computer controlled snake goes over a raspberry/score
        RaspberrySpawned = 0 # Sets the amount of raspberrys/score values on the screen to 0, making it so a new one needs to be placed
    else: # If no raspberrys were collected
        SnakePredatorSegments.pop() # Removes the last value from the list (the tail of the snake) of all the components of the computer snake (SnakePredatorSegments) 

    for count in range(1,30): # Creates a for loop that goes through 30 times for how many score values were collected in the last game
        if RaspberryCollected == count: # If the amount of raspberrys collected is the same as the amount of times gone through the for loop
            x_coord = x[count-1] # Sets the x coordinate (for the next raspberry to be placed) as being that index number -1 in the list of coordinates
            y_coord = y[count-1] # Sets the y coordinate (for the next raspberry to be placed) as being that index number -1 in the list of coordinates
            RaspberryPosition = [int(x_coord),int(y_coord)] # Combines the two coordinates to make a position for the new raspberry to be placed

    for position in SnakePredatorSegments: # For each section of the computer controlled snake
        pygame.draw.rect(PlaySurface, GREEN, Rect(position[0], position[1], 20, 20)) # Draw onto the pygame window each of the computer snakes 'body parts'
        pygame.draw.rect(PlaySurface, RED, Rect(RaspberryPosition[0], RaspberryPosition[1], 20, 20)) # Draw onto the pygame window the new raspberry
    pygame.display.flip() # Updates what is displayed on the pygame window
    if RaspberryCollected >= 10: # If the player has collected 10 or more raspberrys/score
        for SnakeBody in SnakePredatorSegments[1:]: # For each 'body part' in the computer controlled snake
            if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the player controlled snake
                WonGameREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls the WonGameREPLAY function to end the replay
    for SnakeBody in SnakePredatorSegments[1:]: # For each 'body part' in the computer controlled snake
        if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the player controlled snake
            GameOverREPLAY(UserID, PlaySurface, RED, BLACK, WHITE, GREY, GREEN) # Calls GameOverREPLAY to end the replay
