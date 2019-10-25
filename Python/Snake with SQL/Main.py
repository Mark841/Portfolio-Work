import sqlite3 # Imports sqlite3 so the SQL commands will work
from tkinter import * # imports tkinter so the GUI can be created
from Snake_Game import * # imports all from the Snake_Game library file to use all the functions inside it
from ViewTables import * # imports all from the ViewTables library file to use all the functions inside it
from CreateTables import * # imports all from the CreateTables library file to use all the functions inside it
from Snake_Game_Replay import * # imports all from the Snake_Game_Replay library file to use all the functions inside it

class Enter_Username: # Creates a class to store all the information in the enter username window
    def __init__(self): # Is the constructor for the class
        self.window = Tk() # Initialises the window
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.createWidgets() # Calls the createWidgets method

    def createWidgets(self): # Sets up the createWidgets method to create the layout of the window
        self.window.title("Username Entry") # Sets the title of the window to Username Entry
        self.information_label = Label(self.window, text = "Please create a username to play a game:", bg = "light blue") # Creates a label in the window with text on it and sets the background colour of the label to light blue
        self.information_label.grid(row = 0, column = 0) # Sets the location of this label to be in row 0, column 0 of the window
        
        self.username_label = Label(self.window, text = "Username", bg = "light blue") # Creates a label in the window with text on it and sets the background colour of the label to light blue
        self.username_label.grid(row = 1, column = 0) # Sets the location of this label to be in row 1, column 0 of the window
        self.username_entry = Entry(self.window, width = 20) # Creates an entry box in the window and sets the width of the box to 20
        self.username_entry.grid(row = 1, column = 1) # Sets the location of this entry box to be in row 1, column 1 of the window

        self.ok_button = Button(self.window, text = "Create", command = self.CheckingUsername, bg = "light green", borderwidth = 3) # Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the CheckingUsername method
        self.ok_button.grid(row = 3, column = 1, stick = W) # Sets the location of this button to be in row 3, column 1 of the window       

    def CheckingUsername(self): # Sets up the CheckingUsername method to check the entered username
        conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
        c = conn.cursor() # Sets the cursor value to c 
        
        self.username_get = self.username_entry.get() # Gets what the user has inputted into the entry box
        User_Select = self.username_get # Sets the retrieved username into variable
        global UserID # Sets the UserID to a global variable
        UserID = Get_User_IDs(User_Select) # Retrieves the UserID by calling the Get_User_IDs function and passes in the entered username to search if it is in the database
        if UserID == -1: # Checks to see if the returned value for the UserID is -1 and if it is then the user doesnt exist
            Add_User(self.username_get) # Calls the Add_User functino to add a new user to the database with the entered username
            UserID = Get_User_IDs(User_Select) # # Retrieves the UserID for the new user by calling the Get_User_IDs function
            self.login() # Calls the login method
        else: # If the user already existed then
            self.login() # Calls the login method
         
    def login(self): # Sets up the login method to go to the main menu
        conn.close() # Closes the SQL file
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

class menu_window: # Creates a class to store all the information in the main menu window
    def __init__ (self, UserID): # Is the constructor for the class
        self.UserID = UserID
        self.window = Tk() # Initialises the window
        self.window.title("Menu") # Sets the title of the window to Menu
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.lst = Listbox(self.window, width=45, height=15) # Creates a listbox on the window and chooses its size
        self.lst.bind('<<ListboxSelect>>',self.on_select) # Makes it so if an item in the list box is clicked then it calls the on_select method
        self.lst.grid(row=0, column=0, columnspan=2, padx=10, pady=3) # Sets the location of where the listbox appear in the window
        self.write_lst() # Calls the write_lst method
        
    def write_lst(self): # Sets up the write_lst method to write text inside the listbox
        self.lst.delete(0, END) # Deletes any existing text in the listbox
        self.lst.insert(END,'0. Play Snake') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'1. Replay Last Game') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'2. View All Routes Taken') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'3. View Scores Leaderboard') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'4. View Scores For A Particular User') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'5. View Average Score For User') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'6. Clear Entire Database') # Inserts this line of text into the listbox after the end of the previous item
        self.lst.insert(END,'7. Exit') # Inserts this line of text into the listbox after the end of the previous item

    def on_select(self, event): # Sets up the on_select method so if an item is clicked on in the listbox then it runs this to see what item was clicked
        selection = self.lst.curselection()[0] # Sets the selection variable (the users choice) equal to the row that was clicked on in the listbox
        if selection == 0: # If the selection variable is 0
            self.window.destroy() # Closes the current window
            self.Snake_Game() # Calls the Snake_Game method
        elif selection == 1: # If the selection variable is 1
            self.window.destroy() # Closes the current window
            self.Snake_Game_Replay() # Calls the Snake_Game_Replay method
        elif selection == 2: # If the selection variable is 2
            self.window.destroy() # Closes the current window
            root = Routes_Taken() # Calls the Routes_Taken class
        elif selection == 3: # If the selection variable is 3
            self.window.destroy() # Closes the current window
            root = Scores_Leaderboard() # Calls the Scores_Leaderboard class
        elif selection == 4: # If the selection variable is 4
            self.window.destroy() # Closes the current window
            root = Scores_By_User() # Calls the Scores_By_User class
        elif selection == 5: # If the selection variable is 5
            self.window.destroy() # Closes the current window
            root = Average_Score_For_User() # Calls the Average_Score_For_User class
        elif selection == 6: # If the selection variable is 6
            self.window.destroy() # Closes the current window
            root = Reset_Database() # Calls the Reset_Database class
        elif selection == 7: # If the selection variable is 7
            self.window.destroy() # Closes the current window

    def Snake_Game(self):  # Sets up the Snake_Game method
        Game_Select = "Snake With AI" # Tells the code what game has been selected
        GameID = Get_Game_IDs(Game_Select) # Finds the GameID of the selected game, which can be used later to save the scores and moves for this game

        RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RedColour, BlackColour, WhiteColour, GreyColour, GreenColour, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection = InitialiseVariables()
        # Initialises all the variables that will be needed for the game, calls the function from the Snake_Game file
        SnakeGame(self.UserID, GameID, RaspLocForReplay, RaspberryCollected, fpsClock, PlaySurface, RedColour, BlackColour, WhiteColour, GreyColour, GreenColour, SnakePosition, SnakeSegments, RaspberryPosition, Direction, ChangeDirectionRight, ChangeDirectionLeft, ChangeDirectionUp, ChangeDirectionDown, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection)
        # Calls the function to run the game, from the Snake_Game file

    def Snake_Game_Replay(self): # Sets up the Snake_Game_Replay method
        RaspberryCollected, fpsClock, PlaySurface, RedColour, BlackColour, WhiteColour, GreyColour, GreenColour, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection = InitialiseVariablesREPLAY()
        # Initialises all the variables for the replay of the game, calls the function from the Snake_Game_Replay file
        SnakeGameREPLAY(self.UserID, RaspberryCollected, fpsClock, PlaySurface, RedColour, BlackColour, WhiteColour, GreyColour, GreenColour, SnakePosition, SnakeSegments, RaspberryPosition, RaspberrySpawned, SnakePredatorPosition, SnakePredatorSegments, PredDirection, ChangePredDirection)
        # Calls the function to replay the game, from the Snake_Game_Replay file

class Routes_Taken: # Creates a class to store all the information in the routes taken window
    def __init__(self): # Is the constructor for the class
        self.window = Tk() # Initialises the window
        self.window.wm_protocol("WM_DELETE_WINDOW", self.close) # Is a protocol so if the red X or close button in the top right of the window is clicked then it runs the close method
        self.window.title("Routes Taken") # Sets the title of the window to Routes Taken
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.Routes_lst = Listbox(self.window, width=100, height=15) # Creates a listbox on the window and chooses its size
        self.Routes_lst.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=3) # Sets the location of where the listbox appear in the window

        self.menu_button = Button(self.window, text='Back to Menu', command = self.GoBack, bg = "light green", borderwidth = 3) # Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the GoBack method
        self.menu_button.grid(row=2,column = 1,sticky =E) # Sets the location of this button to be in row 2, column 1 of the window    

        self.write_lst() # Calls the write_lst method

    def write_lst(self): # Sets up the write_lst method to write text inside the listbox
        self.Routes_lst.delete(0, END) # Deletes any existing text in the listbox
        conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
        c = conn.cursor() # Sets the cursor value to c 
        sql = "SELECT Username, Moves" # Starts an SQL statement that selects all the Username's and Moves
        sql += " FROM Users, Moves" # Adds onto the SQL statement by telling it to find the information in the Users and Moves tables
        sql += " WHERE Users.UserID = Moves.UserID" # Adds onto the SQL statement by saying that the UserId in the Users table,
        # is the same as the UserID in the Moves table, creating the relationship between them allowing data to be shared in the query
        for row in c.execute(sql): # For each row of items that is returned from the sql statement/query (the Username and Moves) 
            self.Routes_lst.insert(END, row) # Inserts into the listbox each row of data that was returned from the query
        conn.close()  # Closes the SQL file

    def close(self): # Sets up the close method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

    def GoBack(self): # Sets up the GoBack method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

class Scores_Leaderboard: # Creates a class to store all the information in the scores leaderboard window
    def __init__(self): # Is the constructor for the class
        self.window = Tk() # Initialises the window
        self.window.wm_protocol("WM_DELETE_WINDOW", self.close) # Is a protocol so if the red X or close button in the top right of the window is clicked then it runs the close method
        self.window.title("Scores Leaderboard") # Sets the title of the window to Scores Leaderboard
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.ScoresBox_lst = Listbox(self.window, width=50, height=15) # Creates a listbox on the window and chooses its size
        self.ScoresBox_lst.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=3) # Sets the location of where the listbox appear in the window
        self.write_lst() # Calls the write_lst method

        self.ok_button = Button(self.window, text='Back to Menu', command = self.GoBack, bg = "light green", borderwidth = 3)# Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the GoBack method
        self.ok_button.grid(row=2,column = 1,sticky =E) # Sets the location of this button to be in row 2, column 1 of the window

    def write_lst(self):  # Sets up the write_lst method to write text inside the listbox
        ScoresList = [] # Creates a list that will hold all the scores and usernames
        self.ScoresBox_lst.delete(0, END) # Deletes any existing text in the listbox
        conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
        c = conn.cursor() # Sets the cursor value to c 
        sql = "SELECT Score, Username" # Starts an SQL statement that selects the Scores and Usernames
        sql += " FROM Scores, Users" # Adds onto the SQL statement by telling it to find the information in the Scores and Users tables
        sql += " WHERE Scores.UserID = Users.UserID" # Adds onto the SQL statement by saying that the UserID in the Users table,
        # is the same as the UserID in the Scores table, creating the relationship between them allowing data to be shared in the query
        for row in c.execute(sql): # For each row that is returned from the SQL statement/query (the Scores and Usernames) 
            ScoresList.append(row) # Appends each row,  so the Score and Username to the list of scores
        ScoresList = Merge_Sort(ScoresList) # Calls the merge sort algorithm from the library program, to sort the scores in the list of scores
        for item in ScoresList: # For each item in the list of scores
            self.ScoresBox_lst.insert(END, item) # Inserts into the listbox each item of data that was returned from the merge sorted list of scores
        conn.close() # Closes the SQL file

    def close(self): # Sets up the close method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

    def GoBack(self): # Sets up the GoBack method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

class Scores_By_User: # Creates a class to store all the information in the scores by particular user window
    def __init__(self): # Is the constructor for the class
        self.window = Tk() # Initialises the window
        self.window.wm_protocol("WM_DELETE_WINDOW", self.close) # Is a protocol so if the red X or close button in the top right of the window is clicked then it runs the close method
        self.window.title("Scores For A Particular User") # Sets the title of the window to Scores For A Particular User
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.ScoresBox_lst = Listbox(self.window, width=50, height=15) # Creates a listbox on the window and chooses its size
        self.ScoresBox_lst.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=3) # Sets the location of where the listbox appear in the window

        self.Users_lbl = Label(self.window, text='Username', bg = "light blue", borderwidth = 3) # Creates a label in the window with text on it and sets the background colour of the label to light blue
        self.Users_lbl.grid(row=5, column=0) # Sets the location of where the label appears in the window
        options = [] # Creates a list to hold all the options (Users) for the dropdown menu
        Users = Get_Usernames() # Calls the Get_Usernames library function to retrieve all the usernames which is stored in a list called Users
        for Username in Users: # For each username in the Users list
            options.append(Username) # Adds each username to the list of options in the dropdown menu
        self.option_var = StringVar() # Creates a tkinter variable that holds a string, where the default value is an empty string ""
        self.option_var.trace("w", lambda name, index, mode: self.write_lst()) # Calls the write_lst method to write in the list box, when a User is selected in the dropdown menu 
        self.option_menu = OptionMenu(self.window, self.option_var, *options) # Sets the default option that appears on the dropdown menu to be nothing,
        # so when the window is first opened, the user must select a user otherwise nothing will be shown
        self.option_menu.configure(width=9) # Sets the width of the dropdown menu box
        self.option_menu.grid(row=5, column=1) # Sets the location of where the dropdown menu appears in the window
        self.write_lst() # Calls the write_lst method

        self.return_button = Button(self.window, text='Back to Menu', command = self.GoBack, bg = "light green", borderwidth = 3)
        # Creates a button in the window with text on it and sets the background of it to light green, it also creates a border around the button.
        # If the button is pressed, it calls the GoBack method
        self.return_button.grid(row=6,column = 1,sticky =E) # Sets the location of this button to be in row 6, column 1 of the window

    def write_lst(self):  # Sets up the write_lst method to write text inside the listbox
        conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
        c = conn.cursor() # Sets the cursor value to c 
        sql = 'SELECT Score' # Starts an SQL statement that selects all the Scores
        sql += ' FROM Users, Scores' # Adds onto the SQL statement by telling it to find the information in the Users and Scores tables
        sql += ' WHERE Users.UserID = Scores.UserID' # Adds onto the SQL statement by saying that the UserID in the Users table,
        # is the same as the UserID in the Scores table, creating the relationship between them allowing data to be shared in the query
        sql += ' AND Users.Username = "%s"' %self.option_var.get() # Adds onto the SQL statement by making it search for all the scores
        # for the user with the selected username that was selected in the dropdown menu
        self.ScoresBox_lst.delete(0, END) # Deletes any existing text in the listbox
        for row in c.execute(sql): # For each row that is returned from the SQL statement/query (the Score) 
            self.ScoresBox_lst.insert(END, row) # Inserts into the listbox each row of data that was returned from the query
        conn.close() # Closes the SQL file

    def close(self): # Sets up the close method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

    def GoBack(self):# Sets up the GoBack method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

class Average_Score_For_User: # Creates a class to store all the information in the average score for users window
    def __init__(self): # Is the constructor for the class
        self.window = Tk() # Initialises the window
        self.window.wm_protocol("WM_DELETE_WINDOW", self.close) # Is a protocol so if the red X or close button in the top right of the window is clicked then it runs the close method
        self.window.title("Average Score For Each User")# Sets the title of the window to Average Score For Each User
        self.window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.ScoresBox_lst = Listbox(self.window, width=50, height=15) # Creates a listbox on the window and chooses its size
        self.ScoresBox_lst.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=3) # Sets the location of where the listbox appear in the window
        self.write_lst() # Calls the write_lst method

        self.return_button = Button(self.window, text='Back to Menu', command = self.GoBack, bg = "light green", borderwidth = 3) # Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the GoBack method
        self.return_button.grid(row=2,column = 1,sticky =E) # Sets the location of this button to be in row 2, column 1 of the window

    def write_lst(self):  # Sets up the write_lst method to write text inside the listbox
        ScoresList = [] # Creates a list to hold all the Scores and Usernames
        conn = sqlite3.connect("Tables.sqlite") # Connects to the SQL file
        c = conn.cursor() # Sets the cursor value to c 
        sql = 'SELECT AVG(Score), Username' # Starts an SQL statement that gets the Average Scores for each Username
        sql += ' FROM Scores, Users' # Adds onto the SQL statement by telling it to find the information in the Scores and Users tables
        sql += ' WHERE Scores.UserID = Users.UserID' # Adds onto the SQL statement by saying that the UserID in the Scores table,
        # is the same as the UserID in the Users table, creating the relationship between them, allowing data to be shared in the query
        sql += ' GROUP BY Users.UserID' # Groups all the data by a users UserID
        self.ScoresBox_lst.delete(0, END) # Deletes any existing text in the listbox
        for row in c.execute(sql): # For each row that is returned from the SQL statement/query (the Average Score and Username) 
            ScoresList.append(row) # Appends each row, so the Average Score and Username to the list of scores
        ScoresList = Merge_Sort(ScoresList) # Calls the merge sort algorithm from the library program, to sort the scores in the list of scores
        for item in ScoresList: # For each item in the list of scores
            self.ScoresBox_lst.insert(END, item) # Inserts each item from the list of scores into the listbox that was returned from the query
        conn.close() # Closes the SQL file

    def close(self):  # Sets up the close method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

    def GoBack(self):  # Sets up the GoBack method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

class Reset_Database(): # Creates a class to store all the information in the reset database window
    def __init__(self): # Is the constructor for the class
        self.Reset_window = Tk() # Initialises the window
        self.Reset_window.wm_protocol("WM_DELETE_WINDOW", self.close) # Is a protocol so if the red X or close button in the top right of the window is clicked then it runs the close method
        self.Reset_window.configure(background = "light blue") # Sets the windows background colour to light blue
        self.createWidgets() # Calls the createWidgets method

    def createWidgets(self):  # Sets up the createWidgets method
        self.Reset_window.title("Reset Database") # Sets the title of the window to Reset Database
        self.information_label = Label(self.Reset_window, text = "Are you sure you would like to reset the entire database?\n(This will take you back to the username entry window)", bg = "light blue")
        # Creates a label in the window with text on it and sets the background colour of the label to light blue
        self.information_label.grid(row = 0, column = 0) # Sets the location of where the label appears in the window

        self.yes_button = Button(self.Reset_window, text = "YES", command = self.resetting_database, bg = "light green", borderwidth = 3) # Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the resetting_database method
        self.yes_button.grid(row = 2, column = 0, stick = W) # Sets the location of this button to be in row 2, column 0 of the window   

        self.no_button = Button(self.Reset_window, text = "NO", command = self.go_back, bg = "light green", borderwidth = 3) # Creates a button in the window with text on it and sets the background of
        # it to light green, it also creates a border around the button. If the button is pressed it calls the go_back method
        self.no_button.grid(row = 2, column = 1, stick = W) # Sets the location of this button to be in row 2, column 1 of the window     

    def resetting_database(self):  # Sets up the resetting_database method
        create_or_reset_tables() # Calls the create_tables function in the CreateTables file which will delete and recreate all the tables in the SQL file
        self.Reset_window.destroy() # Closes the current window
        root = Enter_Username() # Calls the Enter_Username class

    def close(self):  # Sets up the close method
        self.window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class

    def go_back(self):  # Sets up the go_back method
        self.Reset_window.destroy() # Closes the current window
        root = menu_window(UserID) # Calls the menu_window class
               
        

if __name__ == "__main__": # Is the main of the program so starts to run the items that are in here
    root = Enter_Username() # Calls the first class for the GUI - Enter_Username
    mainloop() # Is an infinite loop, that constantly runs the code to check for anything that changes (events)
