from tkinter import *
from Users import *
from New_Main import *
from oop_algorithms import *
from oop_validation import *
from my_pickle import *

class Login_window:
    # Username: dst@me.com
    # Password: Password1

    def __init__(self):
        self.window = Tk()
        self.createWidgets()

    def createWidgets(self):

        # Creates a title for the window
        self.window.title("Login")

        # Creates a label at the top of the screen with text
        self.information_label = Label(self.window, text = "Please login to the system:")
        self.information_label.grid(row = 0, column = 0)
        
        # The usernames label and entry box
        self.username_label = Label(self.window, text = "Email")
        self.username_label.grid(row = 1, column = 0)
        self.username_entry = Entry(self.window, width = 20)
        self.username_entry.grid(row = 1, column = 1)

        # The passwords label and entry box
        self.password_label = Label(self.window, text = "Password")
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.window, width = 20)
        self.password_entry.grid(row = 2, column = 1)

        # Button to be pressed if the information has been entered
        self.ok_button = Button(self.window, text = "Login", command = self.logging_in)
        self.ok_button.grid(row = 3, column = 1, stick = W)        

    def logging_in(self):

        #Retrieves the username and password
        self.username_get = self.username_entry.get()
        self.password_get = self.password_entry.get()
        print(self.username_get, self.password_get)
              
        index = usernames.linear_search_user(self.username_get)



        if self.password_get == "":
            self.error_label = Label(self.window, text = "Please enter a password")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
        else:
            if index != -1:
                user = usernames.get_user(index)
                print(user.description()) 
                
                if True:
                    if length_check(self.password_get,6):
                        print('Too short')
                        self.error_label = Label(self.window, text = "Incorrect password")
                        self.error_label.grid(row = 0, column = 1)
                        self.createWidgets()
                    elif digit_check(self.password_get):
                        print('No digit')
                        self.error_label = Label(self.window, text = "Incorrect password")
                        self.error_label.grid(row = 0, column = 1)
                        self.createWidgets()
                    elif upper_lower_case(self.password_get):
                        print('Needs both upper and lower case')
                        self.error_label = Label(self.window, text = "Incorrect password")
                        self.error_label.grid(row = 0, column = 1)
                        self.createWidgets()
                    else:
                        print("")
                else:
                    print("")
                        
                if user.login(self.password_get): 
                    self.login()
                else:
                    self.error_label = Label(self.window, text = "Incorrect password")
                    self.error_label.grid(row = 0, column = 1)
                    self.createWidgets()         
            else:
                self.error_label = Label(self.window, text = "User does not exist       ")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets
                    
    def login(self):
        self.window.destroy()
        root = menu_window()

#
#
#

class menu_window:

    def __init__(self):
        self.menu = Tk()
        self.createWidgets()

    def createWidgets(self):

        #Titles the new window and creates a label at the top
        self.menu.title("Menu")
        self.info_menu_label = Label(self.menu, text = "Please select an option")
        self.info_menu_label.grid(row = 0, column = 1)

        # Option 1's button
        self.menu_label = Label(self.menu, text = "1. Add a new teacher")
        self.menu_label.grid(row = 1, column = 1)
        self.menu_button = Button(self.menu, text = "Go", command = self.Teacher)
        self.menu_button.grid(row = 1, column = 2, sticky = W)

        # Option 2's button
        self.menu_label = Label(self.menu, text = "2. Add a new student")
        self.menu_label.grid(row = 2, column = 1)
        self.menu_button = Button(self.menu, text = "Go", command = self.Student)
        self.menu_button.grid(row = 2, column = 2, sticky = W)
        
        # Option 3's button
        self.menu_label2 = Label(self.menu, text = "3. Change an existing user's password")
        self.menu_label2.grid(row = 3, column = 1)
        self.menu_button2 = Button(self.menu, text = "Go", command = self.Pass)
        self.menu_button2.grid(row = 3, column = 2, sticky = W)

        # Option 4's button
        self.menu_label3 = Label(self.menu, text = "4. Delete a user")
        self.menu_label3.grid(row = 4, column = 1)
        self.menu_button3 = Button(self.menu, text = "Go", command = self.Delete)
        self.menu_button3.grid(row = 4, column = 2, sticky = W)

        # Option 5's button
        self.menu_label4 = Label(self.menu, text = "5. Show an alphabetically ordered list of all users")
        self.menu_label4.grid(row = 5, column = 1)
        self.menu_button4 = Button(self.menu, text = "Go", command = self.Alphabetical)
        self.menu_button4.grid(row = 5, column = 2, sticky = W)

    def Teacher(self):
        self.menu.destroy()
        root = Create_Teacher()

    def Student(self):
        self.menu.destroy()
        root = Create_Student()

    def Pass(self):
        self.menu.destroy()
        root = Change_Pass()

    def Delete(self):
        self.menu.destroy()
        root = Delete_User()

    def Alphabetical(self):
        self.menu.destroy()
        root = Sort_User()

#
#
#

class Create_Teacher:

    def __init__(self):
        self.Create = Tk()
        self.createWidgets()
 
    def createWidgets(self):
        # Creates a title for the window
        self.Create.title("New user")

        # Creates a label at the top of the screen with text
        self.information_label = Label(self.Create, text = "Add a new user")
        self.information_label.grid(row = 0, column = 0)
        
        # The usernames label and entry box
        self.email_label = Label(self.Create, text = "Username")
        self.email_label.grid(row = 1, column = 0)
        self.email_entry = Entry(self.Create, width = 20)
        self.email_entry.grid(row = 1, column = 1)

        # The passwords label and entry box
        self.password_label = Label(self.Create, text = "Password")
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.Create, width = 20)
        self.password_entry.grid(row = 2, column = 1)

        # The year group entry box
        self.subject_label = Label(self.Create, text = "Subject")
        self.subject_label.grid(row = 3, column = 0)
        self.subject_entry = Entry(self.Create, width = 20)
        self.subject_entry.grid(row = 3, column = 1)

        # Button to be pressed if the information has been entered
        self.ok_button = Button(self.Create, text = "Create User", command = self.create_user)
        self.ok_button.grid(row = 4, column = 1, stick = W)

        self.back_button = Button(self.Create, text = "Back to Menu", command = self.back_to_menu)
        self.back_button.grid(row = 4, column = 0, stick = W)

    def create_user(self):
        self.username_get = self.email_entry.get()
        self.password_get = self.password_entry.get()
        self.subject_get = self.subject_entry.get()
        print(self.username_get, self.password_get)

        if self.password_get == "":
            self.error_label = Label(self.Create, text = "Please enter a password")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
        if True:
            if length_check(self.password_get,6):
                print('Too short')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif digit_check(self.password_get):
                print('No digit')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif upper_lower_case(self.password_get):
                print('Needs both upper and lower case')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            else:
                print("")
        else:
            print("")

        index = usernames.linear_search_user(self.username_get)

        if index == -1:
            self.error_label = Label(self.Create, text = "User added successfully")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
            usernames.add_teacher(self.username_get, self.password_get, self.subject_get)
            save_object(usernames.usernames)
            new_usernames = load_object()
            for row in new_usernames:
                print(row.username)
        else:
            self.error_label = Label(self.Create, text = "User already exists")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()

    def back_to_menu(self):
        self.Create.destroy()
        root = menu_window()

#
#
#

class Create_Student:

    def __init__(self):
        self.Create = Tk()
        self.createWidgets()
 
    def createWidgets(self):
        # Creates a title for the window
        self.Create.title("New user")

        # Creates a label at the top of the screen with text
        self.information_label = Label(self.Create, text = "Add a new user")
        self.information_label.grid(row = 0, column = 0)
        
        # The usernames label and entry box
        self.email_label = Label(self.Create, text = "Username")
        self.email_label.grid(row = 1, column = 0)
        self.email_entry = Entry(self.Create, width = 20)
        self.email_entry.grid(row = 1, column = 1)

        # The passwords label and entry box
        self.password_label = Label(self.Create, text = "Password")
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.Create, width = 20)
        self.password_entry.grid(row = 2, column = 1)

        # The year group entry box
        self.year_group_label = Label(self.Create, text = "Year Group")
        self.year_group_label.grid(row = 3, column = 0)
        self.year_group_entry = Entry(self.Create, width = 20)
        self.year_group_entry.grid(row = 3, column = 1)

        # Button to be pressed if the information has been entered
        self.ok_button = Button(self.Create, text = "Create User", command = self.create_user)
        self.ok_button.grid(row = 4, column = 1, stick = W)

        self.back_button = Button(self.Create, text = "Back to Menu", command = self.back_to_menu)
        self.back_button.grid(row = 4, column = 0, stick = W)

    def create_user(self):
        self.username_get = self.email_entry.get()
        self.password_get = self.password_entry.get()
        self.year_group_get = self.year_group_entry.get()
        print(self.username_get, self.password_get)

        if self.password_get == "":
            self.error_label = Label(self.Create, text = "Please enter a password")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()

        if True:
            if length_check(self.password_get,6):
                print('Too short')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif digit_check(self.password_get):
                print('No digit')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif upper_lower_case(self.password_get):
                print('Needs both upper and lower case')
                self.error_label = Label(self.Create, text = "Incorrect password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            else:
                print("")
        else:
            print("")

        index = usernames.linear_search_user(self.username_get)

        if index == -1:
            self.error_label = Label(self.Create, text = "User added successfully")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
            usernames.add_student(self.username_get, self.password_get, self.year_group_get)
            save_object(usernames.usernames)
            new_usernames = load_object()
            for row in new_usernames:
                print(row.username)
        else:
            self.error_label = Label(self.Create, text = "User already exists")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()

    def back_to_menu(self):
        self.Create.destroy()
        root = menu_window()

#
#
#

class Change_Pass:
    def __init__(self):
        self.Change = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.Change.title("Change Password")
        # The usernames label and entry box
        self.email_label = Label(self.Change, text = "Email")
        self.email_label.grid(row = 1, column = 0)
        self.email_entry = Entry(self.Change, width = 20)
        self.email_entry.grid(row = 1, column = 1)

        # The old passwords label and entry box
        self.password_label = Label(self.Change, text = "Current Password")
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.Change, width = 20)
        self.password_entry.grid(row = 2, column = 1)

        # The new passwords label and entry box
        self.new_password_label = Label(self.Change, text = "New Password")
        self.new_password_label.grid(row = 3, column = 0)
        self.new_password_entry = Entry(self.Change, width = 20)
        self.new_password_entry.grid(row = 3, column = 1)

        # Button to be pressed if the information has been entered
        self.ok_button = Button(self.Change, text = "Change Password", command = self.change_password)
        self.ok_button.grid(row = 4, column = 1, stick = W)
        self.back_button = Button(self.Change, text = "Back to Menu", command = self.back_to_menu)
        self.back_button.grid(row = 4, column = 0, stick = W)

    def change_password(self):
        self.email_get = self.email_entry.get()
        self.password_get = self.password_entry.get()
        self.new_password_get = self.new_password_entry.get()

        usernames.merge_sort_users() 
        index = usernames.binary_search_user(self.email_get)

        if True:
            if length_check(self.password_get,6):
                print('Too short')
                self.error_label = Label(self.Change, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif digit_check(self.password_get):
                print('No digit')
                self.error_label = Label(self.Change, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif upper_lower_case(self.password_get):
                print('Needs both upper and lower case')
                self.error_label = Label(self.Change, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            else:
                print("")
        else:
            print("")

        if True:
            if length_check(self.new_password_get,6):
                print('Too short')
                self.error_label = Label(self.Change, text = "Invalid new password       ")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif digit_check(self.new_password_get):
                print('No digit')
                self.error_label = Label(self.Change, text = "Invalid new password       ")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif upper_lower_case(self.new_password_get):
                print('Needs both upper and lower case')
                self.error_label = Label(self.Change, text = "Invalid new password       ")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            else:
                print("")
        else:
            print("")

        user = usernames.get_user(index)
        print(user.description()) 

        if index != -1:
            if user.login(self.password_get):
                self.error_label = Label(self.Change, text = "Password changed successfully")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
                new_user = usernames.get_user(index)

                new_user.edit_password(self.new_password_get)
                print(new_user.get_attributes())

            else:
                print ("Password incorrect        ")
                    
        else:
            self.error_label = Label(self.Change, text = "This user does not exist")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()

                
        save_object(usernames.usernames)
        new_usernames = load_object()
        for row in new_usernames:
            print(row.username)
          
    
        if self.password_get == "":
            self.error_label = Label(self.Change, text = "Please enter a password")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
        else:
            print("")
            
        


    def back_to_menu(self):
        self.Change.destroy()
        root = menu_window()

#
#
#

class Delete_User:
    def __init__(self):
        self.Delete = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.Delete.title("Delete A User")
        # The usernames label and entry box
        self.email_label = Label(self.Delete, text = "Email")
        self.email_label.grid(row = 1, column = 0)
        self.email_entry = Entry(self.Delete, width = 20)
        self.email_entry.grid(row = 1, column = 1)

        # The passwords label and entry box
        self.password_label = Label(self.Delete, text = "Password")
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.Delete, width = 20)
        self.password_entry.grid(row = 2, column = 1)

        # Button to be pressed if the information has been entered
        self.ok_button = Button(self.Delete, text = "Delete User", command = self.delete_user)
        self.ok_button.grid(row = 3, column = 1, stick = W)
        self.back_button = Button(self.Delete, text = "Back to Menu", command = self.back_to_menu)
        self.back_button.grid(row = 3, column = 0, stick = W)

    def delete_user(self):
        self.email_get = self.email_entry.get()
        self.password_get = self.password_entry.get()

        usernames.merge_sort_users()
        index = usernames.binary_search_user(self.email_get)

        user = usernames.get_user(index)
        print(user.description()) 

        if True:
            if length_check(self.password_get,6):
                print('Too short')
                self.error_label = Label(self.Delete, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif digit_check(self.password_get):
                print('No digit')
                self.error_label = Label(self.Delete, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            elif upper_lower_case(self.password_get):
                print('Needs both upper and lower case')
                self.error_label = Label(self.Delete, text = "Incorrect current password")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets()
            else:
                print("")
        else:
            print("")

        if self.password_get == "":
            self.error_label = Label(self.Delete, text = "Please enter a password")
            self.error_label.grid(row = 0, column = 1)
            self.createWidgets()
        else:

            if index != -1:
                if user.login(self.password_get):
                    #if user.get_admin() == 1:
                    self.error_label = Label(self.Delete, text = "User deleted successfully  ")
                    self.error_label.grid(row = 0, column = 1)
                    self.createWidgets()
                    usernames.delete_user(index)
                    #else:
                    #    self.error_label = Label(self.Delete, text = "You don't have permission to change passwords")
                    #    self.error_label.grid(row = 0, column = 1)
                    #    self.createWidgets
                            
            else: 
                self.error_label = Label(self.Delete, text = "User does not exist      ")
                self.error_label.grid(row = 0, column = 1)
                self.createWidgets

        #for i in range(usernames.get_no_users()):
        #    print(usernames.get_user(i).get_username())

 
        save_object(usernames.usernames)
        new_usernames = load_object()
        for row in new_usernames:
            print(row.username)

        

    def back_to_menu(self):
        self.Delete.destroy()
        root = menu_window()

#
#
#

class Sort_User:
    def __init__(self):
        self.Sort = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.Sort.title("Sort Users Alphabetically")

        self.list = Listbox(self.Sort, width = 45, height = 15)
        self.list.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 3)
        self.list_btn = Button(self.Sort, text = "Write", command = self.write_list)
        self.list_btn.grid(row = 3, column = 1, sticky = W)

        # Button to be pressed if the information has been entered
        self.back_button = Button(self.Sort, text = "Back to Menu", command = self.back_to_menu)
        self.back_button.grid(row = 3, column = 0, stick = W)

    def write_list(self):
        sorted_users = usernames.merge_sort_users()

        self.list.delete(0, END)
        for item in sorted_users:
            self.list.insert(END, item.get_username())

    def back_to_menu(self):
        self.Sort.destroy()
        root = menu_window()

#
#
#

if __name__ == "__main__":

    usernames = Users()
    usernames.add_teacher('kln@me.com', 'Password1', 'Science')
    usernames.add_student('tjt@me.com', 'Password1', '7')
    usernames.add_teacher('dst@me.com', 'Password1', 'Maths')
    usernames.add_student('wbt@me.com', 'Password1', '8')
    save_object(usernames.usernames)

    root = Login_window()
    mainloop()
