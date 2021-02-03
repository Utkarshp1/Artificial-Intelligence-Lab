import copy

def move_gen(node, num_bits):
    neighbors = []
    
    if num_bits == 1:
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(copy_node)
            neighbors[i][i] = neighbors[i][i] ^ 1
            
    if num_bits == 2:
        for i in range(len(node)):
            for j in range(i+1, len(node)):
                copy_node = copy.deepcopy(node)
                copy_node[i] = copy_node[i] ^ 1
                copy_node[j] = copy_node[j] ^ 1
                neighbors.append(copy_node)
                
    if num_bits == 3:
        node = [literal ^ 1 for literal in node]
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(copy_node)
            neighbors[i][i] = neighbors[i][i] ^ 1
        
    if num_bits == 4:
        neighbor = []
        for i in range(len(node)):
            neighbor.append(node[i]^1)
        neighbors.append(neighbor)
        
    return neighbors
        
node = [0, 0, 0, 0]
print(move_gen(node, 1))       
print(move_gen(node, 2))       
print(move_gen(node, 3))       
print(move_gen(node, 4))       