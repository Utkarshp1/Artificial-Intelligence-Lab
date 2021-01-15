from utils import MoveGen
from utils import GoalTest

def dfid(grid, target_x, target_y, m, n):
    global success
    global count
    
    depth = 0           # maximum allowed depth for dfs
    
    # check whether initial node is the target node
    if GoalTest(grid[0][0].x, grid[0][0].y, target_x, target_y):
        count = 1
        grid[0][0].distance = 1
        success = True
        return
    
    while not success:
        depth += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j].distance = -1
        
        grid[0][0].distance = 1
        
        dfs_visit(grid, grid[0][0], target_x, target_y, depth, m, n)
    return count
        
def dfs_visit(grid, node, target_x, target_y, depth, m, n):
    global success
    global count
    count += 1          # incrementing when visiting new node
    
    # check whether present node is the target node
    if GoalTest(node.x, node.y, target_x, target_y):
        success = True
        return
        
    # check whether max depth allowed is reached
    if node.distance - 1 == depth:
        return
    
    neighbors = MoveGen(grid, node, m, n)   # neighbors of the node
    # neighbors = neighbors[::-1]
    
    for neighbor in neighbors:
        if success:
            break
        # checking whether node is visited
        if neighbor.distance == -1:
            neighbor.distance = node.distance + 1
            neighbor.parent = node
            dfs_visit(grid, neighbor, target_x, target_y, depth, m, n)
        elif neighbor.distance > node.distance + 1:
            neighbor.distance = node.distance + 1
            neighbor.parent = node
            dfs_visit(grid, neighbor, target_x, target_y, depth, m, n)
        
count = 0           # number of visited nodes    
success = False     # boolean for whether target is achieved 