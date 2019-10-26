import pygame, sys, time, random # Imports these
from pygame.locals import * # Retrieves all the local constants from pygame

global PredDirection, ChangePredDirection # Sets these variables to be global variables

# Is the window that appears when the game is lost
def GameOver(RaspLocForReplay, RaspberryCollected, PlaySurface, WHITE, GREY): # Creates the GameOver function
    GameOverFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    GameOverSurf = GameOverFont.render('Game Over', True, GREY) # Draws text on the pygame windows surface
    Statement = ('You collected ', RaspberryCollected, 'raspberrys') # Creates a statement that tells the user their score
    Statement = repr(Statement) # Returns the string of text in a printable format
    RaspCollFont = pygame.font.Font('freesansbold.ttf', 24) # Sets the font and size for the text to display score in the pygame window 
    RaspCollSurf = RaspCollFont.render(Statement, False, WHITE) # Draws text on the pygame windows surface
    RaspCollSurf_rect = RaspCollSurf.get_rect(center=(1080/2, 720/2)) # Sets the location for where the score text will appear on the pygame window to be in the middle of the screen
    GameOverRect = GameOverSurf.get_rect() # Gets the rectangular area of the game over text surface
    GameOverRect.midtop = (1080/2, 10) # Sets the location of the game over text to be in the center and at the top of the screen

    PlaySurface.blit(GameOverSurf, GameOverRect) # Draws the text onto the top of the pygame window
    PlaySurface.blit(RaspCollSurf, RaspCollSurf_rect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

# Is the window that appears when the game is won
def WonGame(RaspLocForReplay, RaspberryCollected, PlaySurface, RED, WHITE): # Creates the WonGame function
    WinFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    WinSurf = WinFont.render('You Win', True, RED) # Draws text on the pygame windows surface
    Statement = ('You collected ', RaspberryCollected, 'raspberrys') # Creates a statement that tells the user their score
    Statement = repr(Statement) # Returns the string of text in a printable format
    RaspCollFont = pygame.font.Font('freesansbold.ttf', 24) # Sets the font and size for the text to display score in the pygame window 
    RaspCollSurf = RaspCollFont.render(Statement, False, WHITE) # Draws text on the pygame windows surface
    RaspCollSurf_rect = RaspCollSurf.get_rect(center=(1080/2, 720/2)) # Sets the location for where the score text will appear on the pygame window to be in the middle of the screen
    WinRect = WinSurf.get_rect() # Gets the rectangular area of the won game text surface
    WinRect.midtop = (1080/2, 10) # Sets the location of the won game text to be in the center and at the top of the screen

    PlaySurface.blit(WinSurf, WinRect) # Draws the text onto the top of the pygame window
    PlaySurface.blit(RaspCollSurf, RaspCollSurf_rect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

# Is the function that sets up all the starting variables for the program to run
def InitialiseVariables(): # Is a function that sets up CONSTANT values or initial values
    global PredDirection, ChangePredDirection # Sets these variables to be global variables
    pygame.init() # Initialises all imported pygame modules 
    fpsClock = pygame.time.Clock() # Limits the frame rate of the game
    PlaySurface = pygame.display.set_mode((1080, 720)) # Sets the size of the pygame window
    pygame.display.set_caption('Snake') # Gives the window a title

    RED = pygame.Color(255, 0, 0) 
    BLACK = pygame.Color(0, 0, 0) 
    WHITE = pygame.Color(255, 255, 255) 
    GREY = pygame.Color(150, 150, 150) 
    GREEN = pygame.Color(0, 255, 0) 

    SnakePosition = [100,100] # Sets the location of the head/front of the snake
    SnakeSegments = [[100,100],[80,100],[60,100]] # Sets the location for each body part of the snake
    RaspberryPosition = [300,300] # Sets the location for the first raspberry
    Direction = 'right' # Sets the initial direction of the snake to right
    ChangeDirection = 'right'
    
    RaspberrySpawned = 1 # Sets that a raspberry has been created and exists on the surface of the window
    RaspberryCollected = 0 # Sets how many points have been collected
    RaspLocForReplay = "" # Is a string that will hold the location of all new raspberrys that are generated, to be used in the replay

    SnakePredatorPosition = [940,680] # Sets the location of the head/front of the computer controlled snake
    SnakePredatorSegments = [[940,680],[960,680],[980,680]] # Sets the location for each body part of the computer controlled snake
    
    PredDirection = 'left' # Sets the initial direction of the computer controlled snake to left
    ChangePredDirection = PredDirection # Sets the ChangePredDirection to the same as the direction of motion of the computer controlled snake so it doesn't instantly change direction
    
    return RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirection, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection
    # Returns these values to be used when the function is called


def PlaceNewRaspberry(RaspLocForReplay, RaspberrySpawned): # Creates a new function that places a raspberry (score) in a random location
    x = random.randrange(1,53) # Gets a random x coordinate from a location on the board
    y = random.randrange(1,35) # Gets a random y coordinate from a location on the board
    RaspberryPosition = [int(x*20),int(y*20)] # Sets the raspberry position to be these coordinates, each coordinate is multiplied by 20 to get the respective coordinates on the screen
    RaspberrySpawned = 1 # Sets this variable to 1 to say that there is a new raspberry on the screen
    RaspLocForReplay += str(x*20) # Makes the x coordinate into a string so it can be saved in the SQL file
    RaspLocForReplay += "," # Adds a , between the two coordinates
    RaspLocForReplay += str(y*20) # Makes the y coordinate into a string so it can be saved in the SQL file
    RaspLocForReplay += "-" # Adds a - between each pair of coordinates
    return RaspberryPosition, RaspLocForReplay, RaspberrySpawned # returns these variables to be used

def AI_Dampener(SnakePosition, SnakePredatorPosition): # Creates a function to 'dumb' down the computer controlled snake
    global PredDirection, ChangePredDirection # Sets these variables to be global variables
    AI_Damp_Choose = random.randint(1,2) # Randomly chooses whether to move in the horizontal or vertical direction
    
    if AI_Damp_Choose == 1: # If the randomly chosen integer is 1 then it runs this
        AI_Dampener_Horizon = random.randint(1,5)
        # Chooses another random number to decide what horizontal box in the grid around the player controlled snake's head to travel towards
        if AI_Dampener_Horizon == 1: # If the chosen number is 1
            if (SnakePosition[0]-40) < SnakePredatorPosition[0]: # Finds if the player contolled snake is to the left of the computer snake
                ChangePredDirection = 'left' # If the snake was found to be to the left, it changes the computer snake's direction to be to the left
            if (SnakePosition[0]-40) > SnakePredatorPosition[0]: # Finds if the player contolled snake is to the right of the computer snake
                ChangePredDirection = 'right' # If the snake was found to be to the right, it changes the computer snake's direction to be to the right
        elif AI_Dampener_Horizon == 2: # If the chosen number is 2
            if (SnakePosition[0]-20) < SnakePredatorPosition[0]: # Finds if the player contolled snake is to the left of the computer snake
                ChangePredDirection = 'left' # If the snake was found to be to the left, it changes the computer snake's direction to be to the left
            if (SnakePosition[0]-20) > SnakePredatorPosition[0]: # Finds if the player contolled snake is to the right of the computer snake
                ChangePredDirection = 'right' # If the snake was found to be to the right, it changes the computer snake's direction to be to the right
        elif AI_Dampener_Horizon == 3: # If the chosen number is 3
            if (SnakePosition[0]) < SnakePredatorPosition[0]: # Finds if the player contolled snake is to the left of the computer snake
                ChangePredDirection = 'left' # If the snake was found to be to the left, it changes the computer snake's direction to be to the left
            if (SnakePosition[0]) > SnakePredatorPosition[0]: # Finds if the player contolled snake is to the right of the computer snake
                ChangePredDirection = 'right' # If the snake was found to be to the right, it changes the computer snake's direction to be to the right
        elif AI_Dampener_Horizon == 4: # If the chosen number is 4
            if (SnakePosition[0]+20) < SnakePredatorPosition[0]: # Finds if the player contolled snake is to the left of the computer snake
                ChangePredDirection = 'left' # If the snake was found to be to the left, it changes the computer snake's direction to be to the left
            if (SnakePosition[0]+20) > SnakePredatorPosition[0]: # Finds if the player contolled snake is to the right of the computer snake
                ChangePredDirection = 'right' # If the snake was found to be to the right, it changes the computer snake's direction to be to the right
        elif AI_Dampener_Horizon == 5: # If the chosen number is 5
            if (SnakePosition[0]+40) < SnakePredatorPosition[0]: # Finds if the player contolled snake is to the left of the computer snake
                ChangePredDirection = 'left' # If the snake was found to be to the left, it changes the computer snake's direction to be to the left
            if (SnakePosition[0]+40) > SnakePredatorPosition[0]: # Finds if the player contolled snake is to the right of the computer snake
                ChangePredDirection = 'right' # If the snake was found to be to the right, it changes the computer snake's direction to be to the right
        if ChangePredDirection == 'right' and not PredDirection == 'left': # Checks if the change in direction would mean the computer snake would go back on itself
            PredDirection = ChangePredDirection # If it wouldn't go directly back on itself, then it commits to the change in direction
        if ChangePredDirection == 'left' and not PredDirection == 'right': # Checks if the change in direction would mean the computer snake would go back on itself
            PredDirection = ChangePredDirection # If it wouldn't go directly back on itself, then it commits to the change in direction
            
    if AI_Damp_Choose == 2:
        AI_Dampener_Vert = random.randint(1,5)
        if AI_Dampener_Vert == 1: # If the chosen number is 1
            if (SnakePosition[1]-40) < SnakePredatorPosition[1]: # Finds if the player contolled snake is above the computer snake
                ChangePredDirection = 'up' # If the snake was found to be above the computer snake, it changes the computer snake's direction to go up
            if (SnakePosition[1]-40) > SnakePredatorPosition[1]: # Finds if the player contolled snake is below the computer snake
                ChangePredDirection = 'down' # If the snake was found to be below the computer snake, it changes the computer snake's direction to go down
        elif AI_Dampener_Vert == 2: # If the chosen number is 2
            if (SnakePosition[1]-20) < SnakePredatorPosition[1]: # Finds if the player contolled snake is above the computer snake
                ChangePredDirection = 'up' # If the snake was found to be above the computer snake, it changes the computer snake's direction to go up
            if (SnakePosition[1]-20) > SnakePredatorPosition[1]: # Finds if the player contolled snake is below the computer snake
                ChangePredDirection = 'down' # If the snake was found to be below the computer snake, it changes the computer snake's direction to go down
        elif AI_Dampener_Vert == 3: # If the chosen number is 3
            if (SnakePosition[1]) < SnakePredatorPosition[1]: # Finds if the player contolled snake is above the computer snake
                ChangePredDirection = 'up' # If the snake was found to be above the computer snake, it changes the computer snake's direction to go up
            if (SnakePosition[1]) > SnakePredatorPosition[1]: # Finds if the player contolled snake is below the computer snake
                ChangePredDirection = 'down' # If the snake was found to be below the computer snake, it changes the computer snake's direction to go down
        elif AI_Dampener_Vert == 4: # If the chosen number is 4
            if (SnakePosition[1]+20) < SnakePredatorPosition[1]: # Finds if the player contolled snake is above the computer snake
                ChangePredDirection = 'up' # If the snake was found to be above the computer snake, it changes the computer snake's direction to go up
            if (SnakePosition[1]+20) > SnakePredatorPosition[1]: # Finds if the player contolled snake is below the computer snake
                ChangePredDirection = 'down' # If the snake was found to be below the computer snake, it changes the computer snake's direction to go down
        elif AI_Dampener_Vert == 5: # If the chosen number is 5
            if (SnakePosition[1]+40) < SnakePredatorPosition[1]: # Finds if the player contolled snake is above the computer snake
                ChangePredDirection = 'up' # If the snake was found to be above the computer snake, it changes the computer snake's direction to go up
            if (SnakePosition[1]+40) > SnakePredatorPosition[1]: # Finds if the player contolled snake is below the computer snake
                ChangePredDirection = 'down' # If the snake was found to be below the computer snake, it changes the computer snake's direction to go down
        if ChangePredDirection == 'up' and not PredDirection == 'down': # Checks if the change in direction would mean the computer snake would go back on itself
            PredDirection = ChangePredDirection # If it wouldn't go directly back on itself, then it commits to the change in direction
        if ChangePredDirection == 'down' and not PredDirection == 'up': # Checks if the change in direction would mean the computer snake would go back on itself
            PredDirection = ChangePredDirection # If it wouldn't go directly back on itself, then it commits to the change in direction

    return PredDirection # Returns the next direction of motion for the computer snake

# Is the function that allows the 'player' snake to find the location of the score
def RaspFinder(ChangeDirection, Direction, SnakePosition, RaspberryPosition): 
    RaspFinder_Choose = random.randint(1,2) 
    if RaspFinder_Choose == 1:
        Direction = RaspFinHorizon(ChangeDirection, Direction, SnakePosition, RaspberryPosition)
    else:
        Direction = RaspFinVert(ChangeDirection, Direction, SnakePosition, RaspberryPosition)
    return Direction

def RaspFinHorizon(ChangeDirection, Direction, SnakePosition, RaspberryPosition):
    if (RaspberryPosition[0]) < SnakePosition[0]:
        ChangeDirection = 'left' 
    if (RaspberryPosition[0]) > SnakePosition[0]: 
        ChangeDirection = 'right'
        
    if ChangeDirection == 'right' and not Direction == 'left':
        Direction = ChangeDirection
    if ChangeDirection == 'left' and not Direction == 'right':
        Direction = ChangeDirection
    return Direction

def RaspFinVert(ChangeDirection, Direction, SnakePosition, RaspberryPosition):
    if (RaspberryPosition[1]) < SnakePosition[1]:
        ChangeDirection = 'up'
    if (RaspberryPosition[1]) > SnakePosition[1]:
        ChangeDirection = 'down'

    if ChangeDirection == 'up' and not Direction == 'down':
        Direction = ChangeDirection
    if ChangeDirection == 'down' and not Direction == 'up':
        Direction = ChangeDirection
    return Direction

# A function that will allow the 'player' snake to avoid the computer snake
def AI_Snake_Avoider(SnakePosition, Direction, PredDirection, SnakePredatorPosition):
    TempChoice = random.randrange(1,2)
    # This if states if the AI snake is somewhere to the left or above
    if (((SnakePosition[0] - SnakePredatorPosition[0]) >= 0) and ((SnakePosition[0] - SnakePredatorPosition[0]) <= 60)) and (((SnakePosition[1] - SnakePredatorPosition[1]) >= 0) and ((SnakePosition[1] - SnakePredatorPosition[1]) <= 60)):
        if Direction == 'left':
            Direction = 'up'
        elif Direction == 'down':
            Direction = 'right'
    # This if states if the AI snake is somewhere to the left or below
    if (((SnakePosition[0] - SnakePredatorPosition[0]) >= 0) and ((SnakePosition[0] - SnakePredatorPosition[0]) <= 60)) and (((SnakePosition[1] - SnakePredatorPosition[1]) >= -60) and ((SnakePosition[1] - SnakePredatorPosition[1]) <= 0)):
        if Direction == 'left':
            Direction = 'down'
        elif Direction == 'up':
            Direction = 'right'
    # This if states if the AI snake is somewhere to the right or above
    if (((SnakePosition[0] - SnakePredatorPosition[0]) >= -60) and ((SnakePosition[0] - SnakePredatorPosition[0]) <= 0)) and (((SnakePosition[1] - SnakePredatorPosition[1]) >= 0) and ((SnakePosition[1] - SnakePredatorPosition[1]) <= 60)):
        if Direction == 'right':
            Direction = 'up'
        else:
            Direction = 'left'
    # This if states if the AI snake is somewhere to the right or below
    if (((SnakePosition[0] - SnakePredatorPosition[0]) >= -60) and ((SnakePosition[0] - SnakePredatorPosition[0]) <= 0)) and (((SnakePosition[1] - SnakePredatorPosition[1]) >= -60) and ((SnakePosition[1] - SnakePredatorPosition[1]) <= 0)):
        if Direction == 'right':
            Direction = 'down'
        else:
            Direction = 'left'
    return Direction

def Avoid_Self(SnakePosition, SnakeSegments, Direction):
    TempChoice = random.randrange(1,2)
    # Goes round 3 times incase the correction leads to another collision such as with a long snake
    for count in range(0,3):
        for SnakeBody in SnakeSegments[1:]:       
            if (((SnakePosition[0]+20 == SnakeBody[0]) and Direction == 'right') or ((SnakePosition[0]-20 == SnakeBody[0])) and Direction == 'left') and (SnakePosition[1] == SnakeBody[1]):
                if TempChoice == 1:
                    Direction = 'up'
                else:
                    Direction = 'down'
            if (((SnakePosition[1]+20 == SnakeBody[1]) and Direction == 'down') or ((SnakePosition[1]-20 == SnakeBody[1])) and Direction == 'up') and (SnakePosition[0] == SnakeBody[0]):
                if TempChoice == 1:
                    Direction = 'left'
                else:
                    Direction = 'right'
    return Direction

def Stay_On_Board(SnakePosition, Direction):
    TempChoice = random.randrange(1,2)
    if (SnakePosition[0] == 20) and (Direction == 'left'):
        if TempChoice == 1:
            Direction = 'up'
        else:
            Direction = 'down'
    if (SnakePosition[0] == 1060) and (Direction == 'right'):
        if TempChoice == 1:
            Direction = 'up'
        else:
            Direction = 'down'
    if (SnakePosition[1] == 20) and (Direction == 'up'):
        if TempChoice == 1:
            Direction = 'left'
        else:
            Direction = 'right'
    if (SnakePosition[1] == 720) and (Direction == 'down'):
        if TempChoice == 1:
            Direction = 'left'
        else:
            Direction = 'right'
            
    if (SnakePosition[0] == 20) and (SnakePosition[1] == 720):
        Direction = 'up'
    if (SnakePosition[0] == 20) and (SnakePosition[1] == 0):
        Direction = 'down'
    if (SnakePosition[0] == 1060) and (SnakePosition[1] == 0):
        Direction = 'down'
    if (SnakePosition[0] == 1060) and (SnakePosition[1] == 720):
        Direction = 'up'
    return Direction

# Is the function that automatically plays the snake game               
def AutomaticSnakeGame():
    RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirection, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection = InitialiseVariables()
    while True:   
        Direction = RaspFinder(ChangeDirection, Direction, SnakePosition, RaspberryPosition) # Gets the new direction for the computer controlled snakes direction of motion
        Direction = AI_Snake_Avoider(SnakePosition, Direction, PredDirection, SnakePredatorPosition) # Gets the new direction to avoid the AI snake
        Direction = Avoid_Self(SnakePosition, SnakeSegments, Direction) 
        Direction = Stay_On_Board(SnakePosition, Direction) # Gets the new direction if the snake wanted to go off the board
        if Direction == 'left': # If the new direction for the computer controlled snake is to move left
            SnakePosition[0] -= 20 # Changes the x coordinate of the computer controlled snakes head to be in the next place on the screen
        elif Direction == 'right': # If the new direction for the computer controlled snake is to move right
            SnakePosition[0] += 20 # Changes the x coordinate of the computer controlled snakes head to be in the next place on the screen
        elif Direction == 'down': # If the new direction for the computer controlled snake is to move down
            SnakePosition[1] += 20 # Changes the y coordinate of the computer controlled snakes head to be in the next place on the screen
        elif Direction == 'up': # If the new direction for the computer controlled snake is to move up
            SnakePosition[1] -= 20 # Changes the y coordinate of the computer controlled snakes head to be in the next place on the screen
            
        SnakeSegments.insert(0,list(SnakePosition)) # Inserts into the list of all components of the snake (SnakeSegments) -in the first index value of the list- where the new head of the snake is located on the screen
        if SnakePosition[0] == RaspberryPosition[0] and SnakePosition[1] == RaspberryPosition[1]: # If the player controlled snake goes over a raspberry/score
            RaspberryCollected += 1 # Adds one to the player's score
            RaspberrySpawned = 0 # Sets the amount of raspberrys/score values on the screen to 0, making it so a new one needs to be placed
        else: # If no raspberrys were collected
            SnakeSegments.pop() # Removes the last value from the list (the tail of the snake) of all the components of the snake (SnakeSegments)
        if RaspberrySpawned == 0: # If there are no raspberrys on the screen
            RaspberryPosition, RaspLocForReplay, RaspberrySpawned = PlaceNewRaspberry(RaspLocForReplay, RaspberrySpawned) # Places a new raspberry on the screen
        PlaySurface.fill(BLACK) # Fills the pygame window to be entirely Black
        for position in SnakeSegments: # For each section of the player controlled snake
            pygame.draw.rect(PlaySurface, WHITE, Rect(position[0], position[1], 20, 20)) # Draw onto the pygame window each of the snakes 'body parts'
            pygame.draw.rect(PlaySurface, RED, Rect(RaspberryPosition[0], RaspberryPosition[1], 20, 20)) # Draw onto the pygame window the new raspberry
        if RaspberryCollected >= 10: # If the player has collected 10 or more raspberrys/score
            for SnakeBody in SnakeSegments[1:]: # For each 'body part' in the player controlled snake
                if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the computer controlled snake
                    pygame.display.flip() # Updates what is displayed on the pygame window
                    WonGame(RaspLocForReplay, RaspberryCollected, PlaySurface, RED, WHITE) # Calls the WonGame function to tell the user they have won
        for SnakeBody in SnakeSegments[1:]: # For each 'body part' in the player controlled snake
            if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with another in the player controlled snake
                pygame.display.flip() # Updates what is displayed on the pygame window
                GameOver(RaspLocForReplay, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        if SnakePosition[0] >= 1080 or SnakePosition[0] <= 0: # Checks if the player controlled snake has gone off the screen in the horizontal direction
            pygame.display.flip() # Updates what is displayed on the pygame window
            GameOver(RaspLocForReplay, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        if SnakePosition[1] >= 720 or SnakePosition[1] <= 0: # Checks if the player controlled snake has gone off the screen in the vertical direction
            pygame.display.flip() # Updates what is displayed on the pygame window
            GameOver(RaspLocForReplay, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        RaspberrySpawned = AutomaticSnakePredator(RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments)
        # Calls the function that controls the SnakePredator (computer controlled snake)
        fpsClock.tick(20) # Computes in milliseconds how long it has been since this was last called and makes it so the frame rate can never go over 20 frames per second
        time.sleep(0.05) # Delays what happens next in the program for 0.05 seconds

# Is the function that controls the computer snake
def AutomaticSnakePredator(RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments):
    # Is the function that controls the computer controlled snake
    global PredDirection # Sets this variable to be a global variable
    PredDirection = AI_Dampener(SnakePosition, SnakePredatorPosition) # Gets the new direction for the computer controlled snakes direction of motion
    if PredDirection == 'left': # If the new direction for the computer controlled snake is to move left
        SnakePredatorPosition[0] -= 20 # Changes the x coordinate of the computer controlled snakes head to be in the next place on the screen
    elif PredDirection == 'right': # If the new direction for the computer controlled snake is to move right
        SnakePredatorPosition[0] += 20 # Changes the x coordinate of the computer controlled snakes head to be in the next place on the screen
    elif PredDirection == 'down': # If the new direction for the computer controlled snake is to move down
        SnakePredatorPosition[1] += 20 # Changes the y coordinate of the computer controlled snakes head to be in the next place on the screen
    elif PredDirection == 'up': # If the new direction for the computer controlled snake is to move up
        SnakePredatorPosition[1] -= 20 # Changes the y coordinate of the computer controlled snakes head to be in the next place on the screen
    SnakePredatorSegments.insert(0,list(SnakePredatorPosition)) # Inserts into the list of all components of the computer snake (SnakePredatorSegments)
    # -in the first index value of the list- where the new head of the snake is located on the screen
    if SnakePredatorPosition[0] == RaspberryPosition[0] and SnakePredatorPosition[1] == RaspberryPosition[1]: # If the computer controlled snake goes over a raspberry/score
        RaspberrySpawned = 0 # Sets the amount of raspberrys/score values on the screen to 0, making it so a new one needs to be placed
    else: # If no raspberrys were collected
        SnakePredatorSegments.pop() # Removes the last value from the list (the tail of the snake) of all the components of the computer snake (SnakePredatorSegments) 
    for position in SnakePredatorSegments: # For each section of the computer controlled snake
        pygame.draw.rect(PlaySurface, GREEN, Rect(position[0], position[1], 20, 20)) # Draw onto the pygame window each of the computer snakes 'body parts'
        pygame.draw.rect(PlaySurface, RED, Rect(RaspberryPosition[0], RaspberryPosition[1], 20, 20)) # Draw onto the pygame window the new raspberry
    pygame.display.flip() # Updates what is displayed on the pygame window
    if RaspberryCollected >= 10: # If the player has collected 10 or more raspberrys/score
        for SnakeBody in SnakePredatorSegments[1:]: # For each 'body part' in the computer controlled snake
            if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the player controlled snake
                WonGame(RaspLocForReplay, RaspberryCollected, PlaySurface, RED, WHITE) # Calls the WonGame function to tell the user they have won
    for SnakeBody in SnakePredatorSegments[1:]: # For each 'body part' in the computer controlled snake
        if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the player controlled snake
            GameOver(RaspLocForReplay, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
    return RaspberrySpawned # Returns the list of all the computer snakes moves and if there are any raspberrys currently on the screen



if __name__ == "__main__":
    AutomaticSnakeGame()

