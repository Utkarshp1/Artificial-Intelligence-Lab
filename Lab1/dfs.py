from utils import MoveGen
from utils import GoalTest

def dfs_visit(grid, node, m, n, target_x, target_y):
    global success
    
    node.color = 'gray'     # vertex colored gray to indicate visiting node
    
    if GoalTest(node.x, node.y, target_x, target_y):
        node.color = 'black'
        success = True
        return
    
    neighbors = MoveGen(grid, node, m, n)   # neighbors of the node
    neighbors = neighbors[::-1]
    # consider the node only if not visited
    neighbors = [neighbor for neighbor in neighbors if neighbor.color == "white"]
    
    for neighbor in neighbors:          
        neighbor.color = "gray"
        
    for neighbor in neighbors:
        if success:
            break              
        neighbor.parent = node                  # Assigning the parent 
        neighbor.distance = node.distance + 1   # Assigning the distance from the root node
        dfs_visit(grid, neighbor, m, n, target_x, target_y) # Visiting the child
    
    node.color = "black"        # Once visited, then black color
  
success = False