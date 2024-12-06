from itertools import pairwise

# Function to see if there are any duplicate numbers in the input line. Duplicate nums means dont need to look at.
# Function taken from:  https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique
# SETS remove duplicates from a list
# The second line will go through each element of input (line of input). The generator expression will either:
#   - return TRUE if 'i' is already in set, leading to early exit (look no further)
#   - return FALSE if 'i' is NOT in set and add it, will proceed to iterate
# 'any()' will return TRUE if any expression returns true (ie 'i' is in the set already) which is causes the early exit.
# the 'not' is used to invert the output of 'any()'
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

# --------------------------------------------------- START OF MAIN ---------------------------------------------------

# look at the input line by line.
with open('Day_2_Input.txt', 'r') as file:
    
    total = 0   # holds final answer for valid records

    for line in file:
        report = list(map(int, line.split(' ')))
        
        # if any nums are the same then look no further, move to next line
        if not numsAreUnique(report):
            continue
        
        # if the list is neither Asc or Desc, then dont need to look at, move to next line
        if not isAscend(report) and not isDescend(report):
            continue

        if validDiff(report):
            total += 1

# The correct output for my input is:   421
print(total)



