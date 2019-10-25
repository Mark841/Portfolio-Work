# Search list for a target,returns items index. Function returns -1 if missing.
def linear_search(MY_PASSWORD, username):
    for item in MY_PASSWORD:
        if item.get_username() == username:
            return MY_PASSWORD.index(item)
    return -1
    
    
def bubble_sort(my_list):
    no_swaps = False
    n = len(my_list)-1
    while not(no_swaps):
        no_swaps = True
        for count in range(n):
            if my_list[count].get_username() > my_list[count+1].get_username():
                temp = my_list[count]
                my_list[count] = my_list[count+1]
                my_list[count+1] = temp
                no_swaps = False
        n = n - 1
    return my_list
    
    
def binary_search(my_list, target):

    first = 0
    last = len(my_list)-1
    
    while True:
        midpoint = (first + last)//2
        if my_list[midpoint].get_username() == target:
            return midpoint
        elif first >= last:
            return -1
        elif my_list[midpoint].get_username() > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
                
                
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        left = my_list[:mid]
        right = my_list[mid:]
        
        merge_sort(left)
        merge_sort(right)
        my_list = merge(left, right, my_list)
        return my_list
        
            
def merge(left, right, my_list):
    i = 0
    j = 0
    k = 0
    
    while i < len(left) and j < len(right):
            if left[i].get_username() < right[j].get_username():
                    my_list[k] = left[i]
                    i += 1
            else:
                    my_list[k] = right[j]
                    j += 1
            k += 1
            
    while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
            
    while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
    return my_list
    


