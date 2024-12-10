# MY CODE

def checkLeftRight(lines, linelength, i, j):
    total = 0
    # Check to the RIGHT of the same line
    if (j + 3 < linelen) and (lines[i][j+1] == 'M') and (lines[i][j+2] == 'A') and (lines[i][j+3] == 'S'):
        total += 1
    
    # Check to the LEFT of the same line
    if (j - 3 >= 0) and (lines[i][j-1] == 'M') and (lines[i][j-2] == 'A') and (lines[i][j-3] == 'S'):
        total += 1  
    
    return total


def checkUpDown(lines, linelength, i, j):
    total = 0
    # Check vertical UP
    if (i - 3 >= 0) and (lines[i-1][j] == 'M') and (lines[i-2][j] == 'A') and (lines[i-3][j] == 'S'):
        total += 1

    # Check vertical DOWN
    if (i + 3 < len(lines)) and (lines[i+1][j] == 'M') and (lines[i+2][j] == 'A') and (lines[i+3][j] == 'S'):
        total += 1
    
    return total


def checkDiagonals(lines, linelength, i, j):
    total = 0
    # Check Diagonal Up and Left
    if (i - 3 >= 0) and (j - 3 >= 0) and (lines[i-1][j-1] == 'M') and (lines[i-2][j-2] == 'A') and (lines[i-3][j-3] == 'S'):
        total += 1
    
    # Check Diagonal Up and Right
    if (i - 3 >= 0) and (j + 3 < linelen) and (lines[i-1][j+1] == 'M') and (lines[i-2][j+2] == 'A') and (lines[i-3][j+3] == 'S'):
        total += 1
    
    # Check Diagonal Down and Left
    if (i + 3 < len(lines)) and (j - 3 >= 0) and (lines[i+1][j-1] == 'M') and (lines[i+2][j-2] == 'A') and (lines[i+3][j-3] == 'S'):
        total += 1
    
    # Check Diagonal Down and Right
    if (i + 3 < len(lines)) and (j + 3 < linelen) and (lines[i+1][j+1] == 'M') and (lines[i+2][j+2] == 'A') and (lines[i+3][j+3] == 'S'):
        total += 1

    return total

# open the file, add new lines based on new line chars
file = open('Day_4_Input.txt', 'r')
lines = file.read().split('\n')
file.close()

total = 0

# loop through all lines. Then loop through each char in these lines. For any "X" found, see if "MAS" follows 
for i in range(len(lines)):
    linelen = len(lines[i])
    for j in range(0, linelen):
        if lines[i][j] != 'X':
            continue
        
        total += checkLeftRight(lines, linelen, i, j) + checkUpDown(lines, linelen, i, j) + checkDiagonals(lines, linelen, i, j)            


# Print the answer. The answer for my input is:    2575
print(total)
