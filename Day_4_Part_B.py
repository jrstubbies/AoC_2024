# open the file, add new lines based on new line chars
file = open('Day_4_Input.txt', 'r')
lines = file.read().split('\n')
file.close()

total = 0

# Dont need to look at first or last lines. Find any 'A' and check diagonals for 'SAM' or 'MAS'
for i in range(1, len(lines[0]) - 1):    
    for j in range(1, len(lines) - 1):
        if lines[i][j] == 'A':
            diag1 = lines[i-1][j+1] + 'A' + lines[i+1][j-1]
            diag2 = lines[i-1][j-1] + 'A' + lines[i+1][j+1]
            
            if (diag1 == "SAM" or diag1 == "MAS") and (diag2 == "SAM" or diag2 == "MAS"):
                total += 1
        
# Print the answer. The answer for my input is:    2041
print(total)
