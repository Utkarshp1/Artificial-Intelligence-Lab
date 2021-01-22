from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def best_first_search(start_node, target_node, heuristic):
    count = 0
    open_list = PriorityQueue()
    frontier = []
    closed_list = []
    open_list.put(start_node)
    frontier.append(start_node)
    while not open_list.empty():
        node = open_list.get()
        print(node.blocks, node.h)
        count +=1
        
        if goal_test(node, target_node):
            target_node.parent = node
            return count
            
        for neighbor in move_gen(node, target_node, heuristic):
            if neighbor not in frontier and neighbor not in closed_list:
                # print(neighbor.blocks, neighbor.h)
                neighbor.parent = node
                open_list.put(neighbor)
                frontier.append(neighbor)
        
        closed_list.append(node)
        
    return count        
         