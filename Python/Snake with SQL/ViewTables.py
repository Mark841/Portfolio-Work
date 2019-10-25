import sqlite3 # Imports sqlite3 so the SQL commands will work
import base64 # imports base64
from CreateTables import * # Imports the library functions from CreateTables
conn = sqlite3.connect('Tables.sqlite') # Connects to the SQL file
c = conn.cursor() # Sets the cursor value to c 

##### USED BY ALL

def view_user_database(filename = 'Tables.sqlite'):
  conn = sqlite3.connect(filename) # Connects to the SQL file
  c = conn.cursor() # Sets the cursor value to c 
  print('Users Data') # Outputs to the user that the following information is for the Users table
  for row in c.execute('SELECT * FROM Users'): # For each row of items in the Users table that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print() # Outputs a blank row to seperate it from the next process to be carried out
  conn.close() # Closes the SQL file

def view_game_database(filename = 'Tables.sqlite'):
  conn = sqlite3.connect(filename) # Connects to the SQL file
  c = conn.cursor() # Sets the cursor value to c 
  print('Games Data') # Outputs to the user that the following information is for the Games table
  for row in c.execute('SELECT * FROM Game'): # For each row of items in the Game table that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print() # Outputs a blank row to seperate it from the next process to be carried out
  conn.close() # Closes the SQL file

def view_moves_database(filename = 'Tables.sqlite'):
  conn = sqlite3.connect(filename) # Connects to the SQL file
  c = conn.cursor() # Sets the cursor value to c 
  print('Moves Data') # Outputs to the user that the following information is for the Moves table
  for row in c.execute('SELECT * FROM Moves'): # For each row of items in the Moves table that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print("Moves Columns") # Outputs to the user to tell them that the next information is about the columns of the Moves table
  for row in c.execute('PRAGMA table_info(Moves)'): # For each row of items (Each tables column information for what column name and data type is stored in them) that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print() # Outputs a blank row to seperate it from the next process to be carried out
  conn.close() # Closes the SQL file

def view_scores_database(filename = 'Tables.sqlite'):
  conn = sqlite3.connect(filename) # Connects to the SQL file
  c = conn.cursor() # Sets the cursor value to c 
  print('Scores Data') # Outputs to the user that the following information is for the Scores table
  for row in c.execute('SELECT * FROM Scores'): # For each row of items in the Scores table that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print("Scores Columns") # Outputs to the user to tell them that the next information is about the columns of the Scores table
  for row in c.execute('PRAGMA table_info(Scores)'): # For each row of items (Each tables column information for what column name and data type is stored in them) that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  print() # Outputs a blank row to seperate it from the next process to be carried out
  conn.close() # Closes the SQL file

def view_database(): # Is a function that views all the table names in the sql file
  for row in c.execute('SELECT name FROM sqlite_master WHERE type="table"'): # For each row of items (tablename) that is returned from the sql statement/query
    print(row) # Prints the table names to the user
  
def view_table_info(tablename): # Is a function that views all the column names and information for a chosen table in the sql file
  print(tablename,"Columns") # Outputs to the user to tell them that the next information is about the columns of the chosen table
  for row in c.execute('PRAGMA table_info("%s")' %tablename): # For each row of items (Each tables column information for what column name and data type is stored in them) that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table
  
def view_table_values(tablename): # Is a function that views all the data for a chosen table in the sql file
  print(tablename,'Data') # Outputs to the user to tell them that the next information is all the data of the chosen table
  for row in c.execute('SELECT * FROM ("%s")' %tablename): # For each row of items (Is all the data items in the table) that is returned from the sql statement/query
    print(row) # Outputs that row of information to the user, so they can see what is in the table

##### USED BY MAIN

def Get_User_IDs(User_Select): # Is a function tries to if a user exists and if they do returns their UserID and if they don't then it returnsa UserID of -1
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    tablename = "Users" # Sets the tablename to be the Users table
    UserIDTemp = -1 # Sets the UserID to -1 to show the user hasnt been found
    for row in c.execute('SELECT * FROM ("%s")' %tablename): # For each row of items (The UserID's and Usernames) that is returned from the sql statement/query
        if row[1] == User_Select: # If the Username is the same as the passed in Username that the user entered
            UserIDTemp = row[0] # Sets the UserID to be the corresponding UserID for that Username in the table
    conn.close() # Closes the SQL file
    return UserIDTemp # Returns the User ID

def Add_User(Username): # Is a function that adds a user to the Users table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("INSERT INTO Users VALUES (NULL,'%s')" %Username) # Inserts into a new row, the new username which is generated the next autoincremented UserID
    conn.commit() # Commits/Saves the changes to the SQL file
    conn.close() # Closes the SQL file

def Get_Game_IDs(Game_Select):
  conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
  c = conn.cursor() # Sets the cursor value to c 
  tablename = "Game" # Sets the tablename to be the Game table
  for row in c.execute('SELECT * FROM ("%s")' %tablename): # For each row of items (GameID's and GameNames) that is returned from the sql statement/query
    if row[1] == Game_Select: # If the GameName (row[1]) is the same as the passed in Game_Select
      return row[0] # Returns the GameID for that game

def Get_Usernames():
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    Users = [] # Creates an empty list to hold the users usernames
    for row in c.execute('SELECT * FROM Users'): # For each row of items in the Users table that is returned from the sql statement/query
        Users.append(row[1]) # Adds the username to the list of users
    return Users # Returns a list of usernames

def Merge_Sort(ScoresList): # Is a function that will merge sort a passed in list
    if len(ScoresList)>1:  # If the length of the original list is greater than 1
        mid = len(ScoresList)//2 # Gets the midpoint of the list
        L1 = ScoresList[:mid] # Splits the original list into two, a left half 
        R1 = ScoresList[mid:] # and a right half

        Merge_Sort(L1) # Recursive call, calls the function again with the left half of the list
        Merge_Sort(R1) # Recursive call, calls the function again with the right half of the list

        i = 0 # Sets these variables, initially to 0
        j = 0 # Sets these variables, initially to 0
        k = 0 # Sets these variables, initially to 0
        while i < len(L1) and j < len(R1): # Goes through a loop continuously while the length of the left half list is bigger than i
        # and the length of the right half list is bigger than j
            if L1[i] > R1[j]: # If the value in the left list at the index of i, is bigger than the value in the right list at the index of j
                ScoresList[k] = L1[i] # Then it changes the value in the original list of scores, in the index of k, to be the value in the left list at the index of i
                i = i + 1 # Autoincrements i by 1, so the same index value isnt used again to compare the same values
            else: # If the value in the left list at index i wasn't bigger than the value in the right list at the index of j
                ScoresList[k] = R1[j] # Then it changes the value in the original list of scores, in the index of k, to be the value in the right list at the index of j
                j = j + 1 # Autoincrements j by 1, so the same index value isnt used again to compare the same values
            k = k + 1 # Autoincrements k by 1, so the same index value isnt used again to compare the same values

        while i < len(L1): # Creates another loop for, if the length of the left list is bigger than the value of i
            ScoresList[k] = L1[i] # Then it changes the value in the original list of scores, in the index of k, to be the value in the left list at the index of i
            i = i + 1 # Autoincrements i by 1, so the same index value isnt used again to compare the same values
            k = k + 1 # Autoincrements k by 1, so the same index value isnt used again to compare the same values

        while j < len(R1): # Creates another loop for, if the length of the right list is bigger than the value of j
            ScoresList[k] = R1[j] # Then it changes the value in the original list of scores, in the index of k, to be the value in the right list at the index of j
            j = j + 1 # Autoincrements j by 1, so the same index value isnt used again to compare the same values
            k = k + 1 # Autoincrements k by 1, so the same index value isnt used again to compare the same values
    return ScoresList # Returns the sorted list of scores

##### USED BY SNAKE GAME

def Save_Moves_To_SQL(GameID, UserID, Moves, PredMoves, RaspLocForReplay): # Is a function that saves the moves to the SQL file
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    StrMoves = MakeMovesIntoString(Moves) # Calls a function which makes it so the list of moves can be added to the SQL file as they need to be in a string format, not a list
    StrPredMoves = MakeMovesIntoString(PredMoves) # Calls a function which makes it so the list of the computer snakes moves can be added to the SQL file as they need to be in a string format, not a list
    c.execute("INSERT OR IGNORE INTO Moves VALUES (NULL,'%d','%d','%s','%s','%s')" %(GameID, UserID, StrMoves, StrPredMoves, RaspLocForReplay)) # Adds the values into a new row in the Moves table
    conn.commit() # Commits/Saves the changes to the SQL file
    conn.close() # Closes the SQL file

def MakeMovesIntoString(Moves): # Is a function that changes a list of moves into a long string of moves
    StrMoves = "" # Sets a vriable to hold the string of moves
    Item = 0 # Sets this variable to 0 which will hold how many items have been added to the string and be used as the index value for the existing moves list
    for count in range(0, len(Moves)): # Creates a for loop which will go through the entire list of moves
        if Item == len(Moves)-1: # If the item is the last item in the list
            if Moves[Item] == "": # If the last item in the list, is one where the user didn't change direction
                StrMoves += "-" # Adds a '-' to the string of mvoes to show no change in direction happened
            else: # If a direction was entered
                StrMoves += Moves[Item] # Adds the direction to the string of moves
        else: # If the item isn't the last in the list of moves
          if Moves[Item] == "": # If the user didn't change direction
              StrMoves += ("-"  + ",") # Adds a '-' to the string of moves to show no change in direction happened, also adds a ',' to split it with the next move
              Item += 1 # Adds one to the Item value, so it doesn't always check the same index value in the moves list
          else: # If the user did change direction
              StrMoves += (Moves[Item] + ",") # Adds the direction to the string of moves, also adds a ',' to split it with the next move
              Item += 1 # Adds one to the Item value, so it doesn't always check the same index value in the moves list
    return StrMoves # Returns the string of all the moves

def Save_Score_To_SQL(GameID, UserID, RaspberryCollected): # Is a function that saves the score to the Scores table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("INSERT OR IGNORE INTO Scores VALUES (NULL,'%d','%d','%d')" %(GameID, UserID, RaspberryCollected)) # Adds the values into a new row in the Scores table
    conn.commit() # Commits/Saves the changes to the SQL file
    conn.close() # Closes the SQL file

##### USED BY SNAKE GAME REPLAY

def GetMovesForReplay(): # Is a function that gets the moves from the SQL table to be used in the replay
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("SELECT *  FROM Moves ORDER BY MoveID DESC LIMIT 1") # Gets the last row from the Moves table
    result = c.fetchone() # holds the result of the SQL statement/query
    Moves = [] # Is a list to hold all the items that were returned from the SQL statement
    Repeat = [] # Is a list that will hold all the moves that need to be repeated
    for item in result: # For each item in the returned SQL statement/query
        Moves.append(item) # Adds each item to the Moves list (MovesID, GameID, UserID, StrMoves, StrPredMoves, RaspLocForReplay)
    for item in Moves[3]: # For each letter in the string of all the moves (Moves[3]) 
        if item == ",": # If the letter is a ','
            pass # Then it passes over it and goes to the next stage
        elif item == "o" or item == "w" or item == "n" or item == "p" or item == "e" or item == "f" or item == "t" or item == "i" or item == "g" or item == "h":
        # If the letter is any of these (not the first letter of the word (up, down, left or right))
            pass # Then it passes over it and goes to the next stage
        elif item == "u": # If the letter is 'u'
            Repeat.append("up") # Adds 'up' to the list of moves to be repeated
        elif item == "d": # If the letter is 'd'
            Repeat.append("down") # Adds 'down' to the list of moves to be repeated
        elif item == "l": # If the letter is 'l'
            Repeat.append("left") # Adds 'left' to the list of moves to be repeated
        elif item == "r": # If the letter is 'r'
            Repeat.append("right") # Adds 'right' to the list of moves to be repeated
        else: # If the letter is none of the above (if it is a '-')
            Repeat.append(item) # Adds the letter to the list of moves to be repeated
    conn.close() # Closes the SQL file
    return Repeat # Returns the list that holds all the moves that are to be repeated

def GetPredMovesForReplay(): # Is a function that gets the computer snakes moves from the SQL table to be used in the replay 
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("SELECT *  FROM Moves ORDER BY MoveID DESC LIMIT 1") # Gets the last row from the Moves table
    result = c.fetchone() # holds the result of the SQL statement/query
    Moves = [] # Is a list to hold all the items that were returned from the SQL statement
    Repeat = [] # Is a list that will hold all the moves that need to be repeated
    for item in result: # For each item in the returned SQL statement/query
        Moves.append(item) # Adds each item to the Moves list (MovesID, GameID, UserID, StrMoves, StrPredMoves, RaspLocForReplay)   
    for item in Moves[4]: # For each letter in the string of all the computer snakes moves (Moves[4]) 
        if item == ",": # If the letter is a ','
            pass # Then it passes over it and goes to the next stage
        elif item == "o" or item == "w" or item == "n" or item == "p" or item == "e" or item == "f" or item == "t" or item == "i" or item == "g" or item == "h":
        # If the letter is any of these (not the first letter of the word (up, down, left or right))
            pass # Then it passes over it and goes to the next stage
        elif item == "u": # If the letter is 'u'
            Repeat.append("up") # Adds 'up' to the list of moves to be repeated
        elif item == "d": # If the letter is 'd'
            Repeat.append("down") # Adds 'down' to the list of moves to be repeated
        elif item == "l": # If the letter is 'l'
            Repeat.append("left") # Adds 'left' to the list of moves to be repeated
        elif item == "r": # If the letter is 'r'
            Repeat.append("right") # Adds 'right' to the list of moves to be repeated
        else: # If the letter is none of the above (if it is a '-')
            Repeat.append(item) # Adds the letter to the list of moves to be repeated
    conn.close() # Closes the SQL file
    return Repeat # Returns the list that holds all the moves that are to be repeated

def GetRaspLocsForReplay(): # Is a function that gets the raspberrys coordinates to be used in the replay
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("SELECT *  FROM Moves ORDER BY MoveID DESC LIMIT 1") # Gets the last row from the Moves table
    result = c.fetchone() # holds the result of the SQL statement/query
    RaspLocs = [] # Creates a list that holds all the coordinates from the SQL query
    x = [] # Creates a list that will hold all the x coordinates for the raspberrys in the replay
    y = [] # Creates a list that will hold all the y coordinates for the raspberrys in the replay
    #RaspNo = 0
    for item in result: # For each item in the returned SQL statement/query
        RaspLocs.append(item) # Adds each item to the RaspLocs list (MovesID, GameID, UserID, StrMoves, StrPredMoves, RaspLocForReplay)

    LOCS = RaspLocs[5] # Sets the variable LOCS to hold the string RaspLocForReplay
    List1 = LOCS.split("-") # Splits the string, where there is a '-' in the string and stores this in a list

    for item in List1: # For each set of coordinates in the list of coordinates
        if item == "": # If there is nothing in the list is nothing 
            break # Breaks the loop as there is nothing in the list
        else: # If there are things in the lsit
            item.strip() # Strips each item so there aren't any spaces left attached to beginning or end of the item 
            a = item.split(",") # Splits the item (coordinates) into two, an x and a y coordinate
            x.append(a[0]) # Adds the x coordinate from the item to the list of all x coordinates
            y.append(a[1]) # Adds the y coordinate from the item to the list of all y coordinates
    conn.close() # Closes the SQL file
    return x, y # Returns the x and y coordinate lists

def QueueOfReplayMoves(): # Is a function that creates a queue of the player controlled snakes moves that will be used in the replay
    Moves = GetMovesForReplay() # Calls the function to import all the moves from the SQL table and stores them in a list
    QueueLength = len(Moves) # Gets the length of the list
    MovesRepeat = queue(QueueLength) # Creates the queue with a fixed size that is the length of the list
    for move in Moves: # For each move in the list of moves
        MovesRepeat.add_item(move) # Adds each move to the queue
    return MovesRepeat # Returns the queue of moves

def QueueOfPredReplayMoves(): # Is a function that creates a queue of the computer controlled snakes moves that will be used in the replay
    Moves = GetPredMovesForReplay() # Calls the function to import all the moves from the SQL table and stores them in a list
    QueueLength = len(Moves) # Gets the length of the list
    MovesRepeat = queue(QueueLength) # Creates the queue with a fixed size that is the length of the list
    for move in Moves: # For each move in the list of moves
        MovesRepeat.add_item(move) # Adds each move to the queue
    return MovesRepeat # Returns the queue of moves

class queue(): # Is a class to store information about a queue
    def __init__ (self, queue_maximum): # Is the constructor for the class
        self.my_list = [] # Creates the queue
        self.next_in = 0 # Sets the next in pointer to 0, so the next item to be put in goes in at this index location
        self.next_out = 0 # Sets the next out pointer to 0, so the first thing to be removed is the first item in the queue
        for i in range(queue_maximum): # Is a for loop that goes through the entire queue
            self.my_list.append('') # Fills the queue with blank spaces so it is set to a size

    def add_item(self, item): # Is a method to add items to the queue
        self.my_list[self.next_in] = item # Puts the item into the queue at the index location of the next in pointer
        self.next_in += 1 # Increments the next in pointer by 1 so the next thing to be added in goes in the next space

    def remove_item(self): # Is a method to remove items to the queue
        if self.next_out == len(self.my_list): # If the next out pointer is at the end of the queue (next out pointer is the length of the list)
          item = "END" # Sets the item to be removed to 'END'
        else: # If it isn't at the end of the queue
          item = self.my_list[self.next_out] # Sets the move that is being removed into the item variable
          self.next_out += 1 # Increments the next out pointer by 1, so the next thing to be removed is the next item in the queue
        return item # Returns the item that has been removed from the queue

    def view_queue(self): # Is a method to view the queue
        for count in range(self.next_out, self.next_in): # Gets every item in the queue between the front of the queue (next out pointer) and the end of the queue (next in pointer)
          print (self.my_list[count]) # Outputs that item to the user in the console
