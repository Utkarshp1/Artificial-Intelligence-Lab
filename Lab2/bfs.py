from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def best_first_search(start_node, target_node):
    count = 0
    open_list = PriorityQueue()
    frontier = []
    closed_list = []
    open_list.put((start_node.h, start_node))
    frontier.append(start_node)
    while not open_list.empty():
        node = open_list.get()
        count +=1
        
        if goal_test(node[1], target_node):
            target_node.parent = node[1]
            return
            
        for neighbor in move_gen(node[1]):
            if neighbor not in frontier and neighbor not in closed_list:
                neighbor.parent = node[1]
                open_list.put((neighbor.h, neighbor))
                frontier.append(neighbor)
        
        closed_list.append(node[1])
        
    return count        
         