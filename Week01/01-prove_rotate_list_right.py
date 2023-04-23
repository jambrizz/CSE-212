"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def rotate_list_right(data, amount):
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    #empty list to store the result
    result = [] 
    
    #length of the list
    length = len(data)
    #empty list to store the first part of the list
    list1 = []
    #empty list to store the second part of the list
    list2 = []
    
    #position of the index starting at 0, will be changed later to the correct index
    position = 0
    
    #if the amount is equal to the length of the list, the position will be the length of the list
    if amount == length:
        position = amount
    #if the amount is less than the length of the list, the position will be the amount - 1
    else:
        position = amount - 1
    
    #if the position is less than or equal to 0, the position will be the length of the list - 1 to get the last element of the list
    if position <= 0:
        #This is to get the last element of the list when the index is 0
        list1.append(data[position-1])
        
        #This is to get all the indexs before the last element of the list and store it in list2 starting at index 0
        for x in range(0, length-1):
            list2.append(data[x])
        
        result = list1 + list2
    #if the position is equal to the length of the list, the result will be the list itself starting at index 0
    elif position == length:
        for x in range(0, length):
            result.append(data[x])
    #if the position does not meet the conditions above       
    else:
        #This is to get all the indexs after the position and store it in list1 starting at index that is equal to the position and ending at the length of the list
        for x in range(position, length):
            list1.append(data[x])
        #This is to get all the indexs before the position and store it in list2 starting at index 0 and ending at the index that is equal to the position
        for x in range(0, position):
            list2.append(data[x])
        
        result = list1 + list2

    return result

print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

