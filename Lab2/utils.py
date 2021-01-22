from Node import Node
from heuristic import heuristic1
from heuristic import heuristic2
import copy

def read_input(node, file):
    for i in range(3):
        line = file.readline()
        line = line[1:-2]
        line = line.replace(" ", "")
        blocks_list = line.split(",")
        blocks_list = [int(block) for block in blocks_list if len(block) > 0]
        node.blocks.append(blocks_list)
        
def move_gen(node, target_node, heuristic):
    neighbours = []
    for i, blocks_list in enumerate(node.blocks):
        if len(blocks_list) > 0:
            for j in range(1, 3):
                neighbour = Node()
                neighbour.blocks = copy.deepcopy(node.blocks)
                block = neighbour.blocks[i].pop(-1)
                neighbour.blocks[(i+j)%3].append(block)
                neighbour.h = heuristic(target_node, neighbour)
                neighbours.append(neighbour)
    return neighbours
    
def goal_test(node, target_node):
    if node == target_node:
        return True
    return False