
# Setting up intial variables
Continue = True
import random
import re

# Creating a function to display a menu for users to see
def DisplayMenu():
    print("\nMain Menu\n")
    print ("1. Add a new user ")
    print ("2. Change a users password")
    print ("3. Delete a user")
    print ("4. Show an alphabetically ordered list of all users")

# Creates a function for the menu option and for what each option will do
def GetMenuChoice(Users):
    Choice = int(input("What would you like to do: ")) # Asks the user what they would like to do
    if Choice == 1: #Choice 1 is to add a new user
        new_username = input("Enter new username: ")
        index = usernames.linear_search_user(new_username)

        if index == -1:
            if user.get_admin() == 1:
                new_password = input('Enter new password: ')
                user_type = int(input('1 (Teacher) 2 (Student)'))
                if user_type == 1:
                    new_subject = input('New subject?')
                    usernames.add_teacher(new_username, new_password, new_subject)
                else:
                    new_year = input('Which year group?')
                    usernames.add_student(new_username, new_password, new_year)
                print()
#                for i in range(usernames.get_no_users()):
#                  print(usernames.get_user(i).get_username())
            else:
                print()
                print(username, "You don't have permission to add new users")
        else:
            print('User already exists')

        save_object(usernames.usernames)
        new_usernames = load_object()
        for row in new_usernames:
            print(row.username)
          
        
    elif Choice == 2: #Choice 2 is to change a users password
        new_username = input("Enter client's username: ")
        usernames.merge_sort_users() 
        index = usernames.binary_search_user(new_username) 

        if index != -1:
            new_user = usernames.get_user(index)
            new_password = input('Enter new password: ')
            
            if user.get_admin() == 1:
                 new_user.edit_password(new_password)
                 print(new_user.get_attributes())
            else:
                print()
                print(username, "You don't have permission to change passwords")
                    
        else:
            print('User doesn\'t exist')

                
        save_object(usernames.usernames)
        new_usernames = load_object()
        for row in new_usernames:
            print(row.username)
          
        
    elif Choice == 3: #Choice is to delete a user
        new_username = input("Enter client's username: ")
        usernames.merge_sort_users()
        index = usernames.binary_search_user(new_username)

        if index != -1:
            if user.get_admin() == 1:
                usernames.delete_user(index)
            else:
                print()
                print(username, "You don't have permission to change passwords")
                        
        else: 
            print('User doesn\'t exist')

        for i in range(usernames.get_no_users()):
            print(usernames.get_user(i).get_username())

        save_object(usernames.usernames)
        new_usernames = load_object()
        for row in new_usernames:
            print(row.username)
            
    elif Choice == 4: #Choice 4 sorts the users alphabetically
        usernames.merge_sort_users()
        usernames.output_users()

if __name__ == '__main__':

    from oop_validation import *
    from oop_algorithms import *
    from my_pickle import *
    from Users import *

    
    usernames = Users()
    usernames.add_teacher('dst@me.com', 'Password1', 'Maths')
    usernames.add_teacher('kln@me.com', 'Password1', 'Science')
    usernames.add_student('tjt@me.com', 'Password1', '7')
    usernames.add_student('wbt@me.com', 'Password1', '8')
    save_object(usernames.usernames)
    
    new_usernames = load_object()
    for row in new_usernames:
        print(row.username)
      

#    while True:
    username = input('Enter email: ')
#    if not validateEmail(username): 
#        break
                    
    index = usernames.linear_search_user(username)
    
    if index != -1:
        user = usernames.get_user(index)
        print(user.description()) 
        
        while True:
            password = input('Enter password: ')
            if length_check(password,6):
                print('Too short')
            elif digit_check(password):
                print('No digit')
            elif upper_lower_case(password):
                print('Needs both upper and lower case')
            else:
                break
                
        if user.login(password): 
            print("Login Successful") 
            DisplayMenu() 
            GetMenuChoice(Users) 
        else:
            print("That is an incorrect password.")         
    else:
        print('user does not exist')
