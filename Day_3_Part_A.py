import re

def mul(x,y):
    return x * y


# read the input as one big string
with open('Day_3_Input.txt', 'r') as file:
    input = file.read()

# find all the substrings that match the "mul(x,y)" pattern
matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input)

# perform the calculations of these valid substrings
total =0 
for m in matches:
    # get only the numbers. The '4' removes "mul(" and '-1' removes ")" splitting the numbers using delimeter ','
    nums = m[4:-1].split(',')
    result = mul(int(nums[0]), int(nums[1]))
    total += result

print(total)