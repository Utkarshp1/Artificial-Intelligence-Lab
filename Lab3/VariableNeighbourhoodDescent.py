from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import move_gen
from utils import goal_test

def VariableNeighbourhoodDescent(start_node, num_variable, clauses):
    states_explored = 1
    current_node = start_node
    
    if goal_test(start_node, len(clauses)):
        print(states_explored)
        return start_node
    
    num_bit = 1
    while True:
        # path_length += 1            # increment the length of path
        open_list = PriorityQueue() # create priority queue for the neighbors
        
        # Search over each neighbor
        for neighbor in move_gen(current_node.values, num_bit, clauses):
            print(neighbor, neighbor.e)
            open_list.put(neighbor)
            states_explored += 1    # increment the number of states explored
            
        node = open_list.get()      # Pop the node with least heuristic value
        
        # Check whether the current node is the goal node
        if goal_test(node, len(clauses)):
            print(states_explored)
            return node
            
        elif node.e >= current_node.e:
            num_bit +=1 
            
        else:
            current_node = node
        