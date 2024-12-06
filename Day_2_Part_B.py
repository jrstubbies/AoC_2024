from itertools import pairwise

# If one duplicate only then remove and return the list, if more than one then can ignore this input line
def numsAreUnique(lst):
    count = 0
    seen = set()
    temp_list = []

    for i in lst:
        #if more than one duplicate then too many errors, early exit and ignore input line
        if i in seen and count > 1:
            return None
        
        # allow for ONE duplicate to occur
        if i in seen and count <= 1:
            count += 1
        
        if i not in seen:
            seen.add(i)
            temp_list.append(i)
        
    # if reach here then there is at MOST ONE ERROR, which is OK
    return temp_list




# function to check the ascending or descending pattern holds, with ONE ERROR ONLY.
def checkPattern(lst):
    asc_count = 0
    des_count = 0

    # look at each pair. Increment respecive count if the pairs show an increase or decrease
    for x, y in pairwise(lst):
        if x > y:
            des_count += 1
        if y > x:
            asc_count += 1
    
    # If BOTH counts are higher than 1, means there is more than ONE ERROR, and line can be ignored
    if des_count > 1 and asc_count > 1:
        return False
    
    # if reach here then there is only ONE ERROR, which is OK
    print(f"asc count is :    {asc_count}      and desc count is:   {des_count}")
    return True




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
        
        # if more than one duplicate 'None' will be returned, otherwise a set will be returned without the duplicate
        updated_report = numsAreUnique(report)
        print(f"the updated report is: {updated_report}")
        
        if updated_report is None:
            print("more than ONE duplicate. Moving next")
            continue

        if not checkPattern(updated_report):
            print("pattern not valid. moving next")
            continue
        
        # if the list is neither Asc or Desc, then dont need to look at, move to next line
        if not validDiff(updated_report):
            print("diff is too high. moving next")
            continue
        else:
            total += 1
    print("-------------------------------------------------")

# The correct output for my input is:   421
print(total)



