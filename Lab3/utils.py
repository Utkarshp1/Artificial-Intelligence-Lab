import copy
from Node import Node

def move_gen(node, num_bits, clauses):
    neighbors = []
    
    if num_bits == 1:
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(Node(copy_node))
            neighbors[i].values[i] = neighbors[i].values[i] ^ 1
            neighbors[i].e = evaluate_node(neighbors[i], clauses)
            
    if num_bits == 2:
        for i in range(len(node)):
            for j in range(i+1, len(node)):
                copy_node = copy.deepcopy(node)
                copy_node[i] = copy_node[i] ^ 1
                copy_node[j] = copy_node[j] ^ 1
                neighbors.append(Node(copy_node))
                neighbors[-1].e = evaluate_node(neighbors[-1], clauses)
                
    if num_bits == 3:
        node = [literal ^ 1 for literal in node]
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(Node(copy_node))
            neighbors[i].values[i] = neighbors[i].values[i] ^ 1
            neighbors[i].e = evaluate_node(neighbors[i], clauses)
        
    if num_bits == 4:
        neighbor = []
        for i in range(len(node)):
            neighbor.append(node[i]^1)
        neighbors.append(Node(neighbor))
        neighbors[-1].e = evaluate_node(neighbors[-1], clauses)
    
    return neighbors
    
def evaluate_node(node, clauses):
    num_satisfied = 0 
    for clause in clauses:
        result = 0
        for literal in clause:
            result = result | literal.calculate_value(node.values)
        
        if result:
            num_satisfied += 1
    return -num_satisfied
    
def is_tautology(clause):
    for i in range(len(clause)):
        clause[i].is_not = clause[i].is_not | 1
    
    if len(set(clause)) == len(clause):
        return False
        
    return True 

def goal_test(node, num_clauses):
    return node.e == -num_clauses

def newmovegen(node,clauses,memory):
    neighbors = []
    for i in range(len(node)):
        copy_node = copy.deepcopy(node)
        neighbors.append(Node(copy_node))
        neighbors[i].values[i] = neighbors[i].values[i] ^ 1
        neighbors[i].e = evaluate_node(neighbors[i], clauses)
    # x = copy.deepcopy(list_nvalid)
    # x.sort()
    for i, j in enumerate(memory[::-1]):
        if j != 0:
           del neighbors[len(memory)-i-1] 
    
    # for i in reversed(x):
        # del neighbors[i]
    # minimum = 1
    # for i in neighbors:
        # if i.e<minimum:
            # minimum=i.e
    # for i in neighbors:
        # if i.e==minimum:
            # for j in range(len(i.values)):
                # if i.values[j]!=node[j] and j not in list_nvalid:
                    # list_nvalid.append(j)
    return neighbors