from utils import MoveGen
from utils import GoalTest

def dfs_visit(grid, node, m, n, target_x, target_y):
    '''
        This function implements the Depth-first search algorithm
        on the given grid.
        
        Arguments:
            - grid: grid of maze
            - node: node to visit
            - m: number of rows in the maze
            - n: number of columns in the maze
            - target_x: x-coordinate of the target state
            - target_y: y-coordinate of the target state
            
        Returns:
            None
    '''
    
    global success      # Boolean for whether target is reached
    
    node.color = 'gray'     # vertex colored gray to indicate visiting node
    
    # determine whether target state is reached
    if GoalTest(node.x, node.y, target_x, target_y):
        node.color = 'black'
        success = True
        return
    
    # Finding the states which can be reached from the given state
    neighbors = MoveGen(grid, node, m, n)
    
    neighbors = neighbors[::-1]       # Uncomment for alternating the scheme
    
    # consider the node only if not visited
    neighbors = [neighbor for neighbor in neighbors if neighbor.color == "white"]
    
    # Nodes to be visited should be colored gray
    for neighbor in neighbors:          
        neighbor.color = "gray"
        
    # Visiting each node in the neighbors
    for neighbor in neighbors:
        if success:             # If target state reached then break
            break
        
        neighbor.parent = node                  # Assigning the parent 
        neighbor.distance = node.distance + 1   # Assigning the distance from the root node
        dfs_visit(grid, neighbor, m, n, target_x, target_y) # Visiting the child
    
    node.color = "black"        # Once visited, then black color
  
success = False         # Boolean for whether target is reached