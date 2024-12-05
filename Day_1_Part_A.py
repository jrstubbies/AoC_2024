# Two arrays to store the 2 column input. Sum to hold value for answer
list_A = []
list_B = []
sum = 0

# Open the puzzle input file, read line by line
with open('Day_1_Input_A.txt', 'r') as file:
    for line in file:

        # Use the map function to split the line into two integers. Then store
        col1, col2 = map(int, line.split())
        list_A.append(col1)
        list_B.append(col2)

# Sort the arrays so that the smallest -> largest numbers for each list align
list_A.sort()
list_B.sort()

# use zip function to combine the two list's numbers. Take the absolute value for the subtraction of these paired values.
for a, b in zip(list_A, list_B):
    sum += abs(a - b)               # total all the absolute values to get the final answer.

# print the answer. Corect answer for my input = 2970687
print(sum)