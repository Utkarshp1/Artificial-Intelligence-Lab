from utils import MoveGen
from utils import GoalTest

def dfid(grid, target_x, target_y, m, n):
    '''
        This function implements the DFID search algorithm
        on the given grid.
        
        Arguments:
            - grid: grid of maze
            - m: number of rows in the maze
            - n: number of columns in the maze
            - target_x: x-coordinate of the target state
            - target_y: y-coordinate of the target state
            
        Returns:
            - count: Number of nodes visited
    '''
    global success         # Boolean for whether target is reached
    global count            # counter for number of nodes visited
    
    depth = 0           # maximum allowed depth for dfs
    
    # check whether initial node is the target node
    if GoalTest(grid[0][0].x, grid[0][0].y, target_x, target_y):
        count = 1
        grid[0][0].distance = 1
        success = True
        return
    
    # Perform DFS until target node is reached
    while not success:
        depth += 1          # increment the depth
        
        # updating the distance of each node
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j].distance = -1
        
        grid[0][0].distance = 1     # Initializing the distance of initial node
        
        # Perform DFS for the present depth
        dfs_visit(grid, grid[0][0], target_x, target_y, depth, m, n)
        
    return count
        
def dfs_visit(grid, node, target_x, target_y, depth, m, n):
    '''
        This function implements the DFS search algorithm
        on the given grid at a particular depth.
        
        Arguments:
            - grid: grid of maze
            - node: node to visit
            - depth: maximum depth in the DFS
            - m: number of rows in the maze
            - n: number of columns in the maze
            - target_x: x-coordinate of the target state
            - target_y: y-coordinate of the target state
            
        Returns:
            - count: Number of nodes visited
    '''
    global success      # Boolean for whether target is reached
    global count        # counter for number of nodes visited
    
    count += 1          # incrementing when visiting new node
    
    # check whether present node is the target node
    if GoalTest(node.x, node.y, target_x, target_y):
        success = True
        return
        
    # check whether max depth allowed is reached
    if node.distance - 1 == depth:
        return
    
    # Finding the states which can be reached from the given state
    neighbors = MoveGen(grid, node, m, n)   
    neighbors = neighbors[::-1]       # Uncomment for the alternative scheme
    
    # Visiting each neighbor node
    for neighbor in neighbors:
        if success:                 # If target state reached then break
            break
            
        # checking whether node is visited
        if neighbor.distance == -1:
            neighbor.distance = node.distance + 1       # Updating the distance
            neighbor.parent = node                      # Updating the parent
            dfs_visit(grid, neighbor, target_x, target_y, depth, m, n)      # Visiting the child
        
        # checking whether the node can be reached from a shorter path
        elif neighbor.distance > node.distance + 1:
            neighbor.distance = node.distance + 1       # Updating the distance
            neighbor.parent = node                      # Updating the parent
            dfs_visit(grid, neighbor, target_x, target_y, depth, m, n)      # Visiting the child  
        
count = 0           # number of visited nodes    
success = False     # boolean for whether target is achieved 