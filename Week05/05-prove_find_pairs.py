"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def find_pairs(words):
    """
    The words parameter contains a list of two character 
    words (lower case, no duplicates). Using sets, find an O(n) 
    solution for displaying all symmetric pairs of words.  

    For example, if words was: [am, at, ma, if, fi], we would display:

    am & ma
    if & fi

    The order of the display above does not matter.  'at' would not 
    be displayed because 'ta' is not in the list of words.

    As a special case, if the letters are the same (example: 'aa') then
    it would not match anything else (remember no the assumption above
    that there were no duplicates) and therefore should not be displayed.
    """ 
    rawSet = set()   
    firstSet = set()
    secondSet = set()
    finalSet = set()
    
    for i in words:
        rawSet.add(i)
    for j in rawSet:
        if j not in firstSet and j[::-1] in rawSet and j != j[::-1]:
            firstSet.add(j)
    for k in firstSet:
        if k[::-1] not in secondSet:
            secondSet.add(k)
    for l in secondSet:
        finalSet.add(l + " & " + l[::-1])
    print(finalSet)
        
    pass

find_pairs(["am","at","ma","if","fi"])      # ma & am, fi & if
print("=============")
find_pairs(["ab", "bc", "cd", "de", "ba"])  # ba & ab
print("=============")
find_pairs(["ab","ba","ac","ad","da","ca"]) # ba & ab, da & ad, ca & ac
print("=============")
find_pairs(["ab", "ac"])                    # None
print("=============")
find_pairs(["ab", "aa", "ba"])              # ba & ab
print("=============")
find_pairs(["23","84","49","13","32","46","91","99","94","31","57","14"])
                                            # 32 & 23, 94 & 49, 31 & 13