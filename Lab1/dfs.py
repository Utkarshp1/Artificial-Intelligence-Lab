from utils import MoveGen
from utils import GoalTest

def dfs_visit(grid, node, m, n, target_x, target_y):
    global success
    node.color = 'gray'     # vertex colored gray to indicate visiting node
    print("hello")
    if GoalTest(node.x, node.y, target_x, target_y):
        node.color = 'black'
        success = True
        return
    print("hello1")
    neighbors = MoveGen(grid, node, m, n)   # neighbors of the node
    # neighbors = neighbors[::-1]
    print(len(neighbors))
    for neighbor in neighbors:
        if success:
            break
        if neighbor.color == "white":               # consider the node only if not visited
            neighbor.parent = node                  # Assigning the parent 
            neighbor.distance = node.distance + 1   # Assigning the distance from the root node
            dfs_visit(grid, neighbor, m, n, target_x, target_y) # Visiting the child
    
    node.color = "black"        # Once visited, then black color 
  
success = False