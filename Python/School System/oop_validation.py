import re

def length_check(string, min_length):
    return len(string) < min_length
    
def digit_check(string):
    digit_check = True
    for i in ['0','1','2','3','4','5','6','7','8','9']:
        if i in string:
            digit_check = False
    return digit_check
    
def upper_lower_case(string):
    return string.lower() == string or string.upper() == string
    
def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return False
    return True
