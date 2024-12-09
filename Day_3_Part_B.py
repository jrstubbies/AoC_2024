import re

# the 'mul' function to multiple two numbers
def mul(x,y):
    return x * y

# Open the file. Updated to remove the newline chars as was causing incorrect calcs
file = open('Day_3_Input.txt', 'r')
data = file.read()
clean_data = data.replace('\n', '')
file.close()

total = 0
results = []

# store substrings that start with "do()" (or string start) and ends with "don't()". Only care about the stuff between do and dont
valid_substrings = re.findall(r"(?=^|do\(\)).*?(?=don't\(\)|$)", clean_data)

# find list of all the "mul(x,y)" within the current substring.
for a in valid_substrings:
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', a)
    results.extend(matches)

# Go through all the valid 'mul' statements and run them
for r in results:
    # get only the numbers. The '4' removes "mul(" and '-1' removes ")" splitting the numbers using delimeter ','
    nums = r[4:-1].split(',')
    result = mul(int(nums[0]), int(nums[1]))
    total += result

# correct answer for my input is:    112272912
print(total)
