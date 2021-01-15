import sys
from Node import Node
from utils import MoveGen
from dfs import dfs_visit
from utils import GoalTest
from bfs import bfs
from utils import trace_path
from dfid import dfid

if len(sys.argv) != 3:
    print("Usage: ./run.sh [INPUT TEXT FILE] [OUTPUT TEXT FILE]")
    quit()
    
file = open(sys.argv[1], "r")       # Reading test case file
choice = file.readline()            # 0 for BFS, 1 for DFS, 2 for DFID 
choice = int(choice[0])

goal_x = -1
goal_y = -1

# Constructing the grid
grid = []
for i, line in enumerate(file):
    grid_line = []
    for j, character in enumerate(line[0:len(line)-1]):
        temp = Node()           # Creating an object of Node class
        temp.x = i              # x-coordinate of the node
        temp.y = j              # y-coordinate of the node
        temp.value = character
        if character == '*':    # finding the coordinates of target node
            goal_x = i
            goal_y = j
        grid_line.append(temp)
    grid.append(grid_line)
    
m = len(grid)               # Number of rows in the state space
n = len(grid[0])            # Number of columns in the state space
  
grid[0][0].color = 'gray'
grid[0][0].distance = 1

count = 0           # Number of states visited
if choice == 0:     # 0 for BFS   
    count = bfs(grid,m,n,goal_x,goal_y)
    
if choice == 1:     # 1 for DFS
    dfs_visit(grid, grid[0][0], m, n, goal_x, goal_y)
    
    # Counting the number of visited states
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].color == "black":
                count += 1
                
if choice == 2:     # 2 for DFID
    count = dfid(grid, goal_x, goal_y, m, n)
    
trace_path(grid, goal_x, goal_y)        # tracing the path discovered


with open(sys.argv[2], "w") as file:
    file.write(str(count) + "\n")      # Number of states explored
    file.write(str(grid[goal_x][goal_y].distance) + "\n") # Length of the path found
    # printing the path found
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            file.write(grid[i][j].value)
        file.write("\n")