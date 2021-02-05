from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import newmovegen
from utils import goal_test

def TabuSearch(start_node, tabu_tenure, clauses):
    states_explored = 1
    current_node = start_node
    MAX_TRIES = 100
    memory = [0]*len(start_node.values)
    
    if goal_test(start_node, len(clauses)):
        print(states_explored)
        return start_node
        
    for i in range(MAX_TRIES):
        open_list = PriorityQueue() # create priority queue for the neighbors
        
        for neighbor in newmovegen(current_node.values, clauses, memory):
            open_list.put(neighbor)
            states_explored += 1    # increment the number of states explored
        
        node = open_list.get()
        
        if goal_test(node, len(clauses)):
            print(states_explored)
            return node
        
        update_memory(memory, current_node, node, tabu_tenure)
        
        current_node = node
        
        if i == MAX_TRIES-1:
            print("No Solution found for MAX_TRIES = 100")
            return
    
def update_memory(memory, current_node, next_node, tabu_tenure):
    for i in range(len(current_node.values)):
        if current_node.values[i] == next_node.values[i]:
            if memory[i] != 0:
                memory[i] -= 1
        else:
            memory[i] = tabu_tenure