from itertools import pairwise


input_dict = {}
rules = []
# Read the contents of the file. First and second part of input is separated by double '\n' char
with open('Day_5_Input.txt', 'r') as file:
    rules_input, updates = file.read().strip().split("\n\n")

    for line in rules_input.split("\n"):
        x, y = line.split("|")
        rules.append((int(x), int(y)))
    
    # Store the values in the second part of the input as a list of ints for each line
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

# CONVERT THIS INTO A FUNCTION -> IS CALCULATING SOMETHING IT SHOULDNT ????
order = {}
total = 0
test = 0
for u in updates:
    for i, num in enumerate(u):
        order[num] = i
    
    for x, y in rules:
        if (x in order and y in order) and (not order[x] < order[y]):
            test += 1
            # take the sum of all MIDDLE numbers for each valid line
            total += u[len(u) // 2] 


print(total)
# 10813    == TOO HIGH