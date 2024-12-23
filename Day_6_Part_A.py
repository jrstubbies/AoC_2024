from enum import Enum

# Read input in as a list of lines.
with open('Day_6_Input.txt') as file:
    grid = file.read().strip().split('\n')

start_found = False

# find the start position (zero indexed my input start is (37, 65))
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            curr_pos = (i, j)
            start_found = True
            break
    
    if start_found:
        break

# Enum to store the directions and the index manipulations needed for each.
class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

# Start off with heading in the direction UP. Set to count unique steps, including the start position 
curr_dir = Direction.UP
visited = set()

# keep traversing the grid until move outside of the 'grid'
while True:

    visited.add(curr_pos)
    #grid[curr_pos[0]][curr_pos[1]] = "X"        # debug to see where have moved

    # calculate the next steps, using a tuple
    next_i = curr_pos[0] + curr_dir.value[0]
    next_j = curr_pos[1] + curr_dir.value[1]

    # have breached the ends of the grid meaning have successfully made it out
    if (next_i not in range(len(grid))) or (next_j not in range(len(grid))):
        break

    # if next step is a '#' then want to change the direction are facing, do NOT want to move into that location
    if grid[next_i][next_j] == "#":
        if curr_dir.name == "UP":
            curr_dir = Direction.RIGHT
        elif curr_dir.name == "RIGHT":
            curr_dir = Direction.DOWN
        elif curr_dir.name == "DOWN":
            curr_dir = Direction.LEFT
        elif curr_dir.name == "LEFT":
            curr_dir = Direction.UP
    else:
        curr_pos = (next_i, next_j)


# gives the answer.  Correct answer for my input  = 5409
print(len(visited))