import re

def mul(x,y):
    return x * y

input = ""
# read the input as one big string
with open('Day_3_Input.txt', 'r') as file:
    line = file.readline().strip()
    input += line

total = 0
results = []

# store substrings that start with "do()" (or string start) and ends with "don't()". Only care about the stuff between do and dont
valid_substrings = re.findall(r"(?:^|do\(\)).*?(?:don\'t\(\)|$)", input)
for a in valid_substrings:
    # find list of all the "mul(x,y)" within the current substring.
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', a)
    #print(matches)
    results.extend(matches)
    #print(results)
    #print('-------------------------------------------------------------')

total =0 
for r in results:
    # get only the numbers. The '4' removes "mul(" and '-1' removes ")" splitting the numbers using delimeter ','
    nums = r[4:-1].split(',')
    result = mul(int(nums[0]), int(nums[1]))
    total += result


print(total)
# Should be less than 175015740 (answer for part A)
# 79876130    = TOO LOW
# 13774421    = WRONG