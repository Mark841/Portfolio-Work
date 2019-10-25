import pygame, sys, time, random # Imports these
from pygame.locals import * # Retrieves all the local constants from pygame
from ViewTables import * # Imports the library functions from ViewTables
from Main import * # Imports the functions from the Main file

global PredDirection, ChangePredDirection # Sets these variables to be global variables

def GameOver(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, WHITE, GREY): # Creates the GameOver function
    GameOverFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    GameOverSurf = GameOverFont.render('Game Over', True, GREY) # Draws text on the pygame windows surface
    Statement = ('You collected ', RaspberryCollected, 'raspberrys') # Creates a statement that tells the user their score
    Statement = repr(Statement) # Returns the string of text in a printable format
    RaspCollFont = pygame.font.Font('freesansbold.ttf', 24) # Sets the font and size for the text to display score in the pygame window 
    RaspCollSurf = RaspCollFont.render(Statement, False, WHITE) # Draws text on the pygame windows surface
    RaspCollSurf_rect = RaspCollSurf.get_rect(center=(600/2, 400/2)) # Sets the location for where the score text will appear on the pygame window to be in the middle of the screen
    GameOverRect = GameOverSurf.get_rect() # Gets the rectangular area of the game over text surface
    GameOverRect.midtop = (300, 10) # Sets the location of the game over text to be in the center and at the top of the screen

    Save_Moves_To_SQL(GameID, UserID, Moves, PredMoves, RaspLocForReplay) # Saves all the moves and the raspberry location to the SQL table
    Save_Score_To_SQL(GameID, UserID, RaspberryCollected) # Saves the score to the SQL table
    
    PlaySurface.blit(GameOverSurf, GameOverRect) # Draws the text onto the top of the pygame window
    PlaySurface.blit(RaspCollSurf, RaspCollSurf_rect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    root = menu_window(UserID) # Calls the main menu class
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

def WonGame(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, RED, WHITE): # Creates the WonGame function
    WinFont = pygame.font.Font('freesansbold.ttf', 72) # Sets the font and size for the text to display game over in the pygame window
    WinSurf = WinFont.render('You Win', True, RED) # Draws text on the pygame windows surface
    Statement = ('You collected ', RaspberryCollected, 'raspberrys') # Creates a statement that tells the user their score
    Statement = repr(Statement) # Returns the string of text in a printable format
    RaspCollFont = pygame.font.Font('freesansbold.ttf', 24) # Sets the font and size for the text to display score in the pygame window 
    RaspCollSurf = RaspCollFont.render(Statement, False, WHITE) # Draws text on the pygame windows surface
    RaspCollSurf_rect = RaspCollSurf.get_rect(center=(600/2, 400/2)) # Sets the location for where the score text will appear on the pygame window to be in the middle of the screen
    WinRect = WinSurf.get_rect() # Gets the rectangular area of the won game text surface
    WinRect.midtop = (300, 10) # Sets the location of the won game text to be in the center and at the top of the screen

    Save_Moves_To_SQL(GameID, UserID, Moves, PredMoves, RaspLocForReplay) # Saves all the moves and the raspberry location to the SQL table
    Save_Score_To_SQL(GameID, UserID, RaspberryCollected) # Saves the score to the SQL table
    
    PlaySurface.blit(WinSurf, WinRect) # Draws the text onto the top of the pygame window
    PlaySurface.blit(RaspCollSurf, RaspCollSurf_rect) # Draws the text onto the top of the pygame window
    pygame.display.flip() # Updates what is displayed on the pygame window
    time.sleep(5) # Delays what happens next in the program for 5 seconds
    root = menu_window(UserID) # Calls the main menu class
    pygame.quit() # Closes the pygame window
    sys.exit() # Closes the pygame program

def InitialiseVariables(): # Is a function that sets up CONSTANT values or initial values
    global PredDirection, ChangePredDirection # Sets these variables to be global variables
    pygame.init() # Initialises all imported pygame modules 
    fpsClock = pygame.time.Clock() # Limits the frame rate of the game
    PlaySurface = pygame.display.set_mode((600, 400)) # Sets the size of the pygame window
    pygame.display.set_caption('Snake') # Gives the window a title

    RED = pygame.Color(255, 0, 0) # Sets the red colour
    BLACK = pygame.Color(0, 0, 0) # Sets the black colour
    WHITE = pygame.Color(255, 255, 255) # Sets the white colour
    GREY = pygame.Color(150, 150, 150) # Sets the grey colour
    GREEN = pygame.Color(0, 255, 0) # Sets the green colour

    SnakePosition = [100,100] # Sets the location of the head/front of the snake
    SnakeSegments = [[100,100],[80,100],[60,100]] # Sets the location for each body part of the snake
    RaspberryPosition = [300,300] # Sets the location for the first raspberry
    Direction = 'right' # Sets the initial direction of the snake to right
    ChangeDirectionRight = False # Shows that no input has been entered to change the snakes direction
    ChangeDirectionLeft = False # Shows that no input has been entered to change the snakes direction
    ChangeDirectionUp = False # Shows that no input has been entered to change the snakes direction
    ChangeDirectionDown = False # Shows that no input has been entered to change the snakes direction
    RaspberrySpawned = 1 # Sets that a raspberry has been created and exists on the surface of the window
    RaspberryCollected = 0 # Sets how many points have been collected
    RaspLocForReplay = "" # Is a string that will hold the location of all new raspberrys that are generated, to be used in the replay

    SnakePredatorPosition = [540,300] # Sets the location of the head/front of the computer controlled snake
    SnakePredatorSegments = [[540,300],[560,300],[580,300]] # Sets the location for each body part of the computer controlled snake
    
    PredDirection = 'left' # Sets the initial direction of the computer controlled snake to left
    ChangePredDirection = PredDirection # Sets the ChangePredDirection to the same as the direction of motion of the computer controlled snake so it doesn't instantly change direction
    
    return RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection
    # Returns these values to be used when the function is called

def Check_Events(ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown): # Creates a function that checks whether the user has or hasn't pressed anything on the keyboard or mouse
    for event in pygame.event.get(): # Checks to see if any events have happened (eg. keys pressed or mouse moved) and for each event that has happened it goes in this loop to check what they were
        if event.type == pygame.QUIT: # If the close button is clicked
            sys.exit() # Closes the pygame program
        elif event.type == pygame.KEYDOWN: # If a key is pressed down on the keyboard
            ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown = Check_Keydown_Events(event, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown)
            # Calls the Check_Keydown_Events function to check what key has been pressed down and stores the new direction for the snake in the variables
        elif event.type == pygame.KEYUP: # If a key isn't pressed down on the keyboard
            ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown = Check_Keyup_Events(event, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown)
            # Calls the Check_Keyup_Events function to update all the ChangeDirection variables to False to show that the snake shouldn't change its direction
    return ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown # Returns whether any relevant keys werepressed and therefore whether the player snake should change direction
                    
def Check_Keydown_Events(event, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown): # Creates a function that checks whether the user has pressed any keys down on the keyboard
    if event.key == pygame.K_RIGHT or event.key == ord('d'): # Checks if the d key or the right arrow key has been pressed down
        ChangeDirectionRight = True # If those keys were pressed then the direction of the snake is told to change to right by setting this variable to true
    elif event.key == pygame.K_LEFT or event.key == ord('a'): # Checks if the a key or the left arrow key has been pressed down
        ChangeDirectionLeft = True # If those keys were pressed then the direction of the snake is told to change to left by setting this variable to true
    elif event.key == pygame.K_UP or event.key == ord('w'): # Checks if the w key or the up arrow key has been pressed down
        ChangeDirectionUp = True # If those keys were pressed then the direction of the snake is told to change to up by setting this variable to true
    elif event.key == pygame.K_DOWN or event.key == ord('s'): # Checks if the s key or the down arrow key has been pressed down
        ChangeDirectionDown = True # If those keys were pressed then the direction of the snake is told to change to down by setting this variable to true
    elif event.key == K_ESCAPE: # Check if the escape key was pressed
        pygame.event.post(pygame.event.Event(QUIT)) # If it was then it closes the window and program
    return ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown # returns the all the direction variables to be used to change the direction of the snake
    
def Check_Keyup_Events(event, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown): # Creates a function that checks whether the user hasn't pressed any keys down on the keyboard
    if event.key == pygame.K_RIGHT or event.key == ord('d'): # Checks if the d key or the right arrow key has been released from being pressed down
        ChangeDirectionRight = False # If the key has been released then sets the direction back to false for that direction
    elif event.key == pygame.K_LEFT or event.key == ord('a'): # Checks if the a key or the left arrow key has been released from being pressed down
    	ChangeDirectionLeft = False # If the key has been released then sets the direction back to false for that direction
    elif event.key == pygame.K_UP or event.key == ord('w'): # Checks if the w key or the up arrow key has been released from being pressed down
    	ChangeDirectionUp = False # If the key has been released then sets the direction back to false for that direction
    elif event.key == pygame.K_DOWN or event.key == ord('s'): # Checks if the s key or the down arrow key has been released from being pressed down
    	ChangeDirectionDown = False # If the key has been released then sets the direction back to false for that direction
    return ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown # returns the all the direction variables to be used to change the direction of the snake

def PlaceNewRaspberry(RaspLocForReplay, RaspberrySpawned): # Creates a new function that places a raspberry (score) in a random location
    x = random.randrange(1,30) # Gets a random x coordinate from a location on the board
    y = random.randrange(1,19) # Gets a random y coordinate from a location on the board
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

def SnakeGame(UserID, GameID, RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection):
    # Is the function to play the snake game
    Moves = [] # Creates a list to store all the moves that the user enters, to be used in the replay
    PredMoves = [] # Creates a list to store all the moves that the computer snake takes, to be used in the replay
    while True: # Creates an infinite loop    
        ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown = Check_Events(ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown)
        # Calls the Check_Events function to check if the user has inputted anything
        if ChangeDirectionRight == True and not Direction == 'left': # Checks to see if the new inputted direction wouldn't make the snake go directly back on itself
            Direction = 'right' # If the snake wouldn't go directly back on itself, then change to the new direction of motion
        if ChangeDirectionLeft == True and not Direction == 'right': # Checks to see if the new inputted direction wouldn't make the snake go directly back on itself
            Direction = 'left' # If the snake wouldn't go directly back on itself, then change to the new direction of motion
        if ChangeDirectionUp == True and not Direction == 'down': # Checks to see if the new inputted direction wouldn't make the snake go directly back on itself
            Direction = 'up' # If the snake wouldn't go directly back on itself, then change to the new direction of motion
        if ChangeDirectionDown == True and not Direction == 'up': # Checks to see if the new inputted direction wouldn't make the snake go directly back on itself
            Direction = 'down' # If the snake wouldn't go directly back on itself, then change to the new direction of motion
        else: # If the new direction would make the player controlled snake go directly back on itself
            pass # Tells the program to pass so the direction doesnt change from its current path
        if Direction == 'right': # If the direction of motion for the snake is to the right
            SnakePosition[0] += 20 # Changes the x coordinate of the snakes head to be in the next place on the screen
        if Direction == 'left': # If the direction of motion for the snake is to the left
            SnakePosition[0] -= 20 # Changes the x coordinate of the snakes head to be in the next place on the screen   
        if Direction == 'up': # If the direction of motion for the snake is to go up
            SnakePosition[1] -= 20 # Changes the y coordinate of the snakes head to be in the next place on the screen   
        if Direction == 'down': # If the direction of motion for the snake is to go down
            SnakePosition[1] += 20 # Changes the y coordinate of the snakes head to be in the next place on the screen
        Moves.append(Direction) # Adds the move, that the user entered, to their list of moves
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
                    WonGame(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, RED, WHITE) # Calls the WonGame function to tell the user they have won
        if SnakePosition[0] >= 600 or SnakePosition[0] <= 0: # Checks if the player controlled snake has gone off the screen in the horizontal direction
            pygame.display.flip() # Updates what is displayed on the pygame window
            GameOver(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        if SnakePosition[1] >= 400 or SnakePosition[1] <= 0: # Checks if the player controlled snake has gone off the screen in the vertical direction
            pygame.display.flip() # Updates what is displayed on the pygame window
            GameOver(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        for SnakeBody in SnakeSegments[1:]: # For each 'body part' in the player controlled snake
            if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the computer controlled snake
                pygame.display.flip() # Updates what is displayed on the pygame window
                GameOver(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
        PredMoves, RaspberrySpawned = SnakePredator(RaspLocForReplay, UserID, GameID, PredMoves, Moves, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments)
        # Calls the function that controls the SnakePredator (computer controlled snake)
        fpsClock.tick(20) # Computes in milliseconds how long it has been since this was last called and makes it so the frame rate can never go over 20 frames per second
        time.sleep(0.05) # Delays what happens next in the program for 0.05 seconds
    
def SnakePredator(RaspLocForReplay, UserID, GameID, PredMoves, Moves, RaspberryCollected, fpsClock, PlaySurface, RED, BLACK, WHITE, GREY, GREEN, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments):
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
    PredMoves.append(PredDirection) # Adds the move, that the computer snake is moving in, to its list of moves
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
                WonGame(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, RED, WHITE) # Calls the WonGame function to tell the user they have won
    for SnakeBody in SnakePredatorSegments[1:]: # For each 'body part' in the computer controlled snake
        if SnakePosition[0] == SnakeBody[0] and SnakePosition[1] == SnakeBody[1]: # If that body part collides with the player controlled snake
            GameOver(UserID, GameID, PredMoves, RaspLocForReplay, Moves, RaspberryCollected, PlaySurface, WHITE, GREY) # Calls the GameOver function to tell the user that they have lost the game
    return PredMoves, RaspberrySpawned # Returns the list of all the computer snakes moves and if there are any raspberrys currently on the screen

