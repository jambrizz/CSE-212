"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 1 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""
def unique_letters(text):
    """
    This is the new function for the teach assignment.
    """
    # Since we are using a set, it has the property that all elements are unique.
    # This avoids the comparing all letters to all other letters like the function below.
    newSet = set()
    for letter in text:
        if letter in newSet:
            return False
        newSet.add(letter)
    return True


def unique_letters1(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    """

    # Compare all letters to all other letters
    for i in range(len(text)):  
        for j in range(len(text)):
            if i != j:  # Don't want to compare to yourself ... that will 
                        # always result in a match.
                if text[i] == text[j]:
                    return False
    return True

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string