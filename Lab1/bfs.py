from utils import MoveGen
from utils import GoalTest

def bfs(grid,m,n,goal_x,goal_y):
	queue = list()
	count = 0
	queue.append(grid[0][0])
	while queue:
		current_node = queue.pop(0)
		if GoalTest(current_node.x,current_node.y,goal_x,goal_y):
			break
		neighbour = MoveGen(grid,current_node,m,n)
		count +=1
		neighbour = [node for node in neighbour if node.color == 'white']
		for node in neighbour:
			node.color = 'gray'
			node.distance = current_node.distance + 1   # updating distance
			node.parent = current_node        # assigning parent
			queue.append(node)
		current_node.color = 'black'
		
	# return count