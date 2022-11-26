def MoveGen(grid, node, m, n):
    '''
        This function accepts a state and returns all the states 
        that can be reached from the given state in one step in the
        order of DOWN > UP > RIGHT > LEFT.
        
        Arguments:
            - grid: grid of the maze
            - node: node/state whose neighbours have to be found
            - m: number of rows in the grid
            - n: number of columns in the grid
            
        Returns:
            List of Valid neighbours/state which can be visited from
            the given state.
    '''
    
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
    
def GoalTest(x,y,target_x,target_y):
    '''
        This function checks whether the state is the target(goal) 
        state or not. If it is a target state it returns true otherwise 
        false.
        
        Arguments:
            - x: x-coordinate of the state to be checked
            - y: y-coordinate of the state to be checked
            - target_x: x-coordinate of the target state
            - target_y: y-coordinate of thr target state
            
        Returns:
            True if the given state is the target state else False.
    '''
    
    if x == target_x and y == target_y:
        return True
    return False
    
def trace_path(grid, target_x, target_y):
    '''
        This function is to trace the path found by the searcg
        algorithm.
        
        Arguments:
            - grid: grid of the maze
            - target_x: x-coordinate of the target state
            - target_y: y-coordinate of thr target state

        Returns:
            None
    '''
    
    back_track_node = grid[target_x][target_y]
    while back_track_node is not None:              # backtracking the path
        x_cor = back_track_node.x
        y_cor = back_track_node.y
        
        # updating the value of the node in the path as 0
        grid[x_cor][y_cor].value = "0"              
        back_track_node = back_track_node.parent    # updating the track node