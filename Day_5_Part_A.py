import re


input_dict = {}
part_2_lines = []

# Read the contents of the file
with open('Day_5_Input.txt', 'r') as file:
    lines = file.readlines()

# Go over the lines and add keys/values to dict for the first part of input. Store second part input as lists
for line in lines:
    # Deal with the first part of inputs which is in form "X|Y"
    if (re.match(r'[\d]+\|[\d]+', line)):
        x, y = line.split('|')
        
        # if the 'x' value is NOT already a key then add it with its associated 'y' value (done as a list)
        if x not in input_dict:
            input_dict[x] = [int(y.strip())]

        # if the 'x' value IS in the dict already, then need to add the 'y' value to its list of values.
        else:
            input_dict[x].append(int(y.strip()))

# Debug the dictionary to check all items added correctly
for x, y in input_dict.items():
    print(f'X is: {x}    and Y is: {y}')