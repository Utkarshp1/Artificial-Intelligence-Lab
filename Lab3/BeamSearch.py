import numpy as np
from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import move_gen
from utils import goal_test

def BeamSearch(beam_width, clauses):
    states_explored = beam_width
    
    # np.random.seed(2)
    start_states = np.random.randint(low=0, high=2, size=(beam_width, 4))
    # start_states = [[1, 0, 0, 0], [0, 1, 0, 0]]
    
    print(start_states)
    
    best_neighbor = []
    for node in start_states:
        start_node = Node(list(node))
        start_node.e = evaluate_node(start_node, clauses)
        best_neighbor.append(start_node)
        
        if goal_test(start_node, len(clauses)):
            print(states_explored)
            return start_node
    
    
    while True:
        open_list = PriorityQueue()
        
        result = True
        for i in range(beam_width):
            neighbors = PriorityQueue()
            for neighbor in move_gen(best_neighbor[i].values, 1, clauses):
                open_list.put(neighbor)
                neighbors.put(neighbor)
                states_explored += 1
                
            neighbor = neighbors.get()
            
            result = result & (neighbor.e >= best_neighbor[i].e)
            
        if result:
            print("Search is stuck in local minima")
            print(states_explored)
            return
        
        best_neighbor = []
        for i in range(beam_width):
            neighbor = open_list.get()
            best_neighbor.append(neighbor)
            
            if goal_test(neighbor, len(clauses)):
                print(states_explored)
                return neighbor
                
        [print(neighbor.values, neighbor.e) for neighbor in best_neighbor]