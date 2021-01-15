def MoveGen(grid, node, m, n): #finding neighbours of a node in a list
    x_cor = node.x      # x-coordinate of the node
    y_cor = node.y      # y-coordinate of the node
    neighbours = []
    barriers = {'+', '-', '|'}
    
    if x_cor+1 < m and grid[x_cor+1][y_cor].value not in barriers:  # Down
        neighbours.append(grid[x_cor+1][y_cor])
    if x_cor-1 >= 0 and grid[x_cor-1][y_cor].value not in barriers:   # Top
        neighbours.append(grid[x_cor-1][y_cor])
    if y_cor+1 < n and grid[x_cor][y_cor+1].value not in barriers:  # Right
        neighbours.append(grid[x_cor][y_cor+1])
    if y_cor-1 >= 0 and grid[x_cor][y_cor-1].value not in barriers:   # Left
        neighbours.append(grid[x_cor][y_cor-1])
    return neighbours
    
def GoalTest(x,y,goal_x,goal_y): #returning true if target reached goal state otherwise returns false
    if x == goal_x and y == goal_y:
        return True
    return False