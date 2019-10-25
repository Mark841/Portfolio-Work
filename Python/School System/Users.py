from oop_algorithms import *
from oop_validation import *
from my_pickle import *

class Username:
    def __init__(self, username,password):  
        self.username = username
        self.__password = password
        self.admin = 0
        
    def login(self, password):
        return self.__password == password
            
    def get_username(self):
        return self.username
            
    def get_attributes(self):
        return self.username, self.__password, self.admin
            
    def edit_password(self, new_password):
        self.__password = new_password
            
    def description(self):
        return 'user type'
    
    def get_admin(self):
        return self.admin

class Teacher(Username):  
    def __init__(self, username, password, subject): 
        Username.__init__(self,username,password)
        self.subject = subject
        self.admin = 1
        
    def get_subject(self):
        return self.subject
            
    def description(self):
        return 'Teacher'

class Student(Username):
    def __init__(self, username, password, year_group):
        Username.__init__(self,username,password)
        self.year_group = year_group
            
    def get_year_group(self):
        return self.year_group
            
    def description(self):
        return 'Student'

	
class Users():
    def __init__(self):
        self.usernames = []
        self.no_users = 0
        
    def get_no_users(self):
        return self.no_users
        
    def linear_search_user(self, username):
        return linear_search(self.usernames,username)
        
    def binary_search_user(self, username):
        return binary_search(self.usernames,username)

    def bubble_sort_users(self):
        self.usernames = bubble_sort(self.usernames)
        
    def merge_sort_users(self):
        self.usernames = merge_sort(self.usernames)

    def merge_sort_users(self):
        self.usernames = merge_sort(self.usernames)
        return self.usernames
        
    def delete_user(self,index):
        del self.usernames[index]
        self.no_users -=1
        
    def add_teacher(self, username,password,subject):
        self.usernames.append(Teacher(username,password,subject))
        self.no_users += 1
        
    def add_student(self, username,password,year_group):
        self.usernames.append(Student(username,password,year_group))
        self.no_users += 1
        
    def get_user(self,index):
        return self.usernames[index]

    def output_users(self):
        for i in range(self.get_no_users()):
            print("Username: ", self.get_user(i).get_username(), "  Attributes: ", self.get_user(i).get_attributes())
               
##if __name__ == '__main__':
##    
##    usernames = Users()
##    usernames.add_teacher('dst@me.com', 'Password1', 'Maths')
##    usernames.add_teacher('kln@me.com', 'Password1', 'Science')
##    usernames.add_student('tjt@me.com', 'Password1', '7')
##    usernames.add_student('wbt@me.com', 'Password1', '8')
##    save_object(usernames.usernames)
##    
##    new_usernames = load_object()
##    for row in new_usernames:
##        print(row.username)
##      
##    print()
##    print('Unit Test: User Login')
##    print('=====================')
##    print()
##    
##    while True:
##        username = input('Enter username: ')
##        if not validateEmail(username): 
##            break
##                    
##    index = usernames.linear_search_user(username) 
##    
##    if index != -1:
##        user = usernames.get_user(index)
##        print(user.description()) 
##        
##        while True:
##            password = input('Enter password: ')
##            if length_check(password,6):
##                print('Too short')
##            elif digit_check(password):
##                print('No digit')
##            elif upper_lower_case(password):
##                print('Needs both upper and lower case')
##            else:
##                break
##                
##        if user.login(password): 
##            print("Well done! You must work for MI6. Give my regards to James Bond.")
##        else:
##            print()
##            print("That is not my password.")
##                
##    else:
##        print('user does not exist')
##    
##    print()
##    print('Unit Test: Change Password')
##    print('==========================')
##    print()
##    new_username = input("Enter client's username: ")
##    usernames.merge_sort_users() 
##    index = usernames.binary_search_user(new_username) 
##
##    if index != -1:
##        new_user = usernames.get_user(index)
##        new_password = input('Enter new password: ')
##        
##        if user.get_admin() == 1:
##             new_user.edit_password(new_password)
##             print(new_user.get_attributes())
##        else:
##            print()
##            print(username, "You don't have permission to change passwords")
##                
##    else:
##        print('User doesn\'t exist')
##    
##    print()
##    print('Unit Test: Add New User')
##    print('==========================')
##    print()
##
##    new_username = input("Enter new username: ")
##    index = usernames.linear_search_user(new_username)
##
##    if index == -1:
##        if user.get_admin() == 1:
##            new_password = input('Enter new password: ')
##            user_type = int(input('1 (Teacher) 2 (Student)'))
##            if user_type == 1:
##                new_subject = input('New subject?')
##                usernames.add_teacher(new_username, new_password, new_subject)
##            else:
##                new_year = input('Which year group?')
##                usernames.add_student(new_username, new_password, new_year)
##            print()
##            for i in range(usernames.get_no_users()):
##              print(usernames.get_user(i).get_username())
##        else:
##            print()
##            print(username, "You don't have permission to add new users")
##                    
##    else:
##        print('User already exists')
##    
##    print()
##    print('Unit Test: Delete User')
##    print('==========================')
##    print()
##    new_username = input("Enter client's username: ")
##    usernames.merge_sort_users()
##    index = usernames.binary_search_user(new_username)
##
##    if index != -1:
##        if user.get_admin() == 1:
##            usernames.delete_user(index)
##        else:
##            print()
##            print(username, "You don't have permission to change passwords")
##                    
##    else: 
##        print('User doesn\'t exist')
##
##    for i in range(usernames.get_no_users()):
##        print(usernames.get_user(i).get_username())
##    
##    print()
##    print('Unit Test: Read from File')
##    print('==========================')
##    print()
##    
##    save_object(usernames.usernames)
##    new_usernames = load_object()
##    for row in new_usernames:
##        print(row.username)
##      
