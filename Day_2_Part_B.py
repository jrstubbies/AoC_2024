from itertools import pairwise

# NEED TO MODIFY THIS SO THAT IS NOT 'ANY' BUT RATHER A COUNT AT 0 OR 1 (ANYMORE THAN 1 THEN IS A FAIL)
def numsAreUnique(lst):
    seen = set()
    return not any(i in seen or seen.add(i) for i in lst)

#######################################################################################################################
# NEED TO MODIFY THESE SO THAT IS NOT 'ALL' BUT RATHER A COUNT. IF COUNT IS GREATER THAN 1 THEN IS A FAIL. (IE ONE NUMBER
# CAN BE OUT OF PLACE)
# function to check if the list is in ascending order
def isAscend(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)
    )

# function to check if the list is in descending order
def isDescend(lst):
    return all(lst[i] >= lst[i+1] for i in range(len(lst) - 1)
    )


#######################################################################################################################


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
        print(f"the current line is:  {report}")
        
        # if any nums are the same then look no further, move to next line
        if not numsAreUnique(report):
            print("   and the nums are NOT UNIQUE. Moving to next")
            continue
        
        # if the list is neither Asc or Desc, then dont need to look at, move to next line
        if not isAscend(report) and not isDescend(report):
            print("   and the input is not a gradual inc/decr. moving to next")
            continue

        if validDiff(report):
            total += 1
            print(f"the diff between nums is valid, and total is now: {total}")

# The correct output for my input is:   421
print(total)



