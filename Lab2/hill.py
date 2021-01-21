from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def hill_climb(start_node,target_node):
    count = 1
    current_node = start_node
    if goal_test(current_node,target_node):
        target_node.parent = current_node
        return count
        
    while True:
        count += 1
        open_list = PriorityQueue()
        for neighbor in move_gen(current_node, target_node):
            neighbor.parent = current_node
            open_list.put(neighbor)
        node = open_list.get()
        print(node.blocks)
        if goal_test(node,target_node):
            target_node.parent = node
            return count
        elif node.h >= current_node.h:
            print("Search is stuck in local minima")
            return count
        else:
            current_node = node