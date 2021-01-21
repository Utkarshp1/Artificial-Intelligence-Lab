from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def hill_climb(start_node,target_node):
	count =0
	current_node = Node()
	current_node = start_node
	if goal_test(current_node,target_node):
		target_node.parent = current_node
		return
	flag = True
	while flag:
		count++
		open_list = PriorityQueue()
		for neighbor in move_gen(current_node):
			open_list.put((neighbor.h, neighbor))
		node = open_list.get()
		if goal_test(node,target_node):
			node.parent = current_node
			target_node.parent = node
			flag = False
		else:
			if node.h >= current_node.h:
				flag = False
			else:
				node.parent = current_node
				current_node = node