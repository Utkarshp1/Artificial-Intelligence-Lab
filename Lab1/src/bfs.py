from utils import MoveGen
from utils import GoalTest

def bfs(grid,m,n,goal_x,goal_y):
    '''
        This function implements the Breadth-first search algorithm
        on the given grid.
        
        Arguments:
            - grid: grid of maze
            - m: number of rows in the maze
            - n: number of columns in the maze
            - goal_x: x-coordinate of the target state
            - goal_y: y-coordinate of the target state
            
        Returns:
            - count: The number of state visited
    '''

    queue = []          # queue for bfs
    count = 0           # counter for number of nodes visited
    
    queue.append(grid[0][0])    # appending the first node in the queue
    while queue:
        current_node = queue.pop(0)     # poping the node to be visited now
        count +=1                       # icrementing the counter for new node   
        
		# determine whether target state is reached
        if GoalTest(current_node.x,current_node.y,goal_x,goal_y):
            break
            
        # Finding the states which can be reached from the given state
        neighbour = MoveGen(grid,current_node,m,n)
        
        # Filtering only those nodes which have not been visited
        neighbour = [node for node in neighbour if node.color == 'white']
        
        for node in neighbour:
            node.color = 'gray'                 # Visiting nodes colored as gray
            node.distance = current_node.distance + 1   # updating distance
            node.parent = current_node              # assigning parent
            queue.append(node)          # appending the visiting node in the queue                  
        current_node.color = 'black'    # visited nodes colored as black            
        
    return count