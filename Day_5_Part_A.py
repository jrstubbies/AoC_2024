rules = []

# Open the input and separate the two parts of the input using doube '\n'. 
with open("Day_5_Input.txt", 'r') as file:
    rule_input, updates = file.read().strip().split("\n\n")
    
    # Then to get the rules, look at the first part and separate x, y using '|' delimeter.
    for line in rule_input.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))

    # The second part of input is comma separated string of nums
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

# function to check if update line follows the rules, if so return the middle num
def check_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    
    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
        
    return True, update[len(update) // 2]

# Take the sum of all the middle nums for each of the valid input lines
total = 0
for u in updates:
    valid, mid = check_rules(u)
    if valid:
        total += mid

print(total)