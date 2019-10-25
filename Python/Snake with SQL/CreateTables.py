import sqlite3 # Imports sqlite3 so the SQL commands will work

def create_user_table(): # Creates a function to create or reset the Users table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("DROP TABLE IF EXISTS Users") # If the table already exists then this will delete the existing table
    c.execute("CREATE TABLE Users(UserID integer primary key autoincrement, Username text unique)") # Creates the table with 2 columns, being: an auto-incrementing integer for the UserID as a primary key, and a Username which is a unique string of text meaning no 2 users can have the same username
    conn.commit() # This commits and saves the changes to the file
    conn.close() # This closes the file

def create_game_table(): # Creates a function to create or reset the Game table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("DROP TABLE IF EXISTS Game") # If the table already exists then this will delete the existing table
    c.execute("CREATE TABLE Game(GameID integer primary key autoincrement, GameName text unique)") # Creates the table with 2 columns, being: an auto-incrementing integer for the GameID as a primary key, and a GameName which is a unique string of text meaning no 2 games can have the same name
    c.execute("INSERT INTO Game VALUES (NULL,'Snake With AI')") # Inserts a game into the next row of the column called "Snake With AI" this will have the first GameID as it is the first data item in the table
    c.execute("INSERT INTO Game VALUES (NULL,'Text Based Adventure')") # Inserts a game into the next row of the column called "Text Based Adventure"
    conn.commit() # This commits and saves the changes to the file
    conn.close() # This closes the file

def create_moves_table(): # Creates a function to create or reset the Moves table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("DROP TABLE IF EXISTS Moves") # If the table already exists then this will delete the existing table
    c.execute("CREATE TABLE Moves(MoveID integer primary key autoincrement, GameID integer, UserID integer, Moves text, PredMoves text, RaspLocation text, \
    FOREIGN KEY(GameID) REFERENCES Game(GameID),FOREIGN KEY(UserID) REFERENCES Users(UserID))") # Creates the table with 6 columns, being: an auto-incrementing integer for the MoveID as a primary key, the GameID which is an integer, the UserID which is an integer, the players Moves which is a string of text, the computer controlled snakes PredMoves which is a string of text, and the RaspLocation which is a string of text
    # It also establishes foreign keys to the other tables as the GameID and UserID are primary keys in the Game and User tables
    conn.commit() # This commits and saves the changes to the file
    conn.close() # This closes the file

def create_scores_table(): # Creates a function to create or reset the Scores table
    conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
    c = conn.cursor() # Sets the cursor value to c 
    c.execute("DROP TABLE IF EXISTS Scores") # If the table already exists then this will delete the existing table
    c.execute("CREATE TABLE Scores(ScoresID integer primary key autoincrement, GameID integer, UserID integer, Score integer, \
    FOREIGN KEY(GameID) REFERENCES Game(GameID),FOREIGN KEY(UserID) REFERENCES Users(UserID))") # Creates the table with 4 columns, being: an auto-incrementing integer for the ScoresID as a primary key, the GameID which is an integer, the UserID which is an integer, and the Score which is an integer
    # It also establishes foreign keys to the other tables as the GameID and UserID are primary keys in the Game and User tables
    conn.commit() # This commits and saves the changes to the file
    conn.close() # This closes the file

def create_or_reset_tables(): # Creates a function that calls all the previous create table functions, so only this function needs to be called instead of calling all 4
    create_user_table() # Calls the create user table function
    create_game_table() # Calls the create game table function
    create_moves_table() # Calls the create moves table function
    create_scores_table() # Calls the create scores table function
