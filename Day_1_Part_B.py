# Two arrays to store the 2 column input. Sum to hold value for answer
list_A = []
list_B = []
total = 0

# will use a dictionary with lists as values to store the number looking at (key), count in A, count in B
list_dict = {}


# Open the puzzle input file, read line by line
with open('Day_1_Input_A.txt', 'r') as file:
    for line in file:

        # Use the map function to split the line into two integers.
        col1, col2 = map(int, line.split())
        
        # add the first value to the dictionary as a key if not already there, otherwise increase count 
        if col1 in list_dict:
            list_dict[col1][0] += 1
        else:
            list_dict[col1] = [1, 0]

        list_B.append(col2)

# iterate over all values ib list B to update the count value
for i in list_B:
    if i in list_dict:
        list_dict[i][1] += 1


# go through the dictionary to calculate the total
for x, y in list_dict.items():
    total += ((x * y[1]) * y[0])


# print the answer - the correct answer for my input -   23963899
print(total)