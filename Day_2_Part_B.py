from itertools import pairwise

# Function to see if there are any duplicate numbers in the input line. Duplicate nums means dont need to look at.
# Function taken from:  https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique
def numsAreUnique(lst):
    seen = set()
    return not any(i in seen or seen.add(i) for i in lst)

# function to check if the list is in ascending order
def isAscend(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)
    )

# function to check if the list is in descending order
def isDescend(lst):
    return all(lst[i] >= lst[i+1] for i in range(len(lst) - 1)
    )

# function to check if the difference between values is between 1 - 3
def validDiff(lst):
    # 'all()' will immediately return FALSE if ANY pair fails this, otherwise all pairs have a difference between 1 - 3
    return all(1 <= abs(x - y) <= 3 for x, y in pairwise(lst))


def removeSingle(lst):
    valid = False

    # Use brute force approach to see if removing one element at a time will lead to a valid line
    for i in range(len(lst)):
        temp = lst[:]      # create a copy of the lst to modify
        temp.pop(i)        # remove the current number

        if not numsAreUnique(temp):
            continue

        if not isAscend(temp) and not isDescend(temp):
            continue 

        if validDiff(temp):
            valid = True
    
    return valid

# --------------------------------------------------- START OF MAIN ---------------------------------------------------

# look at the input line by line.
with open('Day_2_Input.txt', 'r') as file:
    
    total = 0   # holds final answer for valid records

    for line in file:
        report = list(map(int, line.split(' ')))
        
        if removeSingle(report):
            total += 1

# The correct output for my input is:   476
print(total)



