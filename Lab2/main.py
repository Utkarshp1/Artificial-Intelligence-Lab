import sys
from Node import Node
from utils import read_input
from utils import move_gen
from bfs import best_first_search

file = open(sys.argv[1], "r")       # Reading test case file
file.readline()                     

start_node = Node()
read_input(start_node, file)

file.readline()
file.readline()

goal_node = Node()
read_input(goal_node, file)
       
print(start_node.blocks)
print(goal_node.blocks)

for node in move_gen(start_node):
    print(node.blocks)
    
print(best_first_search(start_node, goal_node))