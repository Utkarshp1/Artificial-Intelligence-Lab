import sys
from Node import Node
from utils import MoveGen
from dfs import dfs_visit

file = open(sys.argv[1], "r")   #Reading test case file
choice = file.readline()           # 0 for BFS, 1 for DFS, 2 for DFID 
choice = int(choice[0])

goal_x = -1
goal_y = -1

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
   
# print(len(grid))
# print(len(grid[8]))
# for i in range(len(grid)):
    # for j in range(len(grid[0])):
        # print(grid[i][j].value, end="")
    # print()
    
m = len(grid)               # Number of rows in the state space
n = len(grid[0])            # Number of columns in the state space

# result = MoveGen(grid, grid[0][0], m, n)

# for i in result:
    # print(i)  
grid[0][0].color = 'gray'
grid[0][0].dis = 0
    
if choice == 1:
    dfs_visit(grid, grid[0][0], m, n, goal_x, goal_y)
    
print(grid[goal_x][goal_y].distance)
