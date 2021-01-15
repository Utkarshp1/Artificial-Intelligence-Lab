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
    
def GoalTest(x,y,target_x,target_y): #returning true if target reached goal state otherwise returns false
    if x == target_x and y == target_y:
        return True
    return False
    
def trace_path(grid, target_x, target_y):
    back_track_node = grid[target_x][target_y]
    while back_track_node is not None:          # backtracking the path
        x_cor = back_track_node.x
        y_cor = back_track_node.y
        grid[x_cor][y_cor].value = "0"
        back_track_node = back_track_node.parent