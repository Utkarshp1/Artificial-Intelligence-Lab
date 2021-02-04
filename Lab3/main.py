import sys
import numpy as np
import copy
from Literal import Literal
from utils import is_tautology
from utils import evaluate_node
from utils import move_gen
from Node import Node

file = open(sys.argv[1], "w")
n = 4
k = 5

literals = [Literal(i, j) for i in range(4) for j in range(2)]
clauses = set()

while len(clauses) != 5:
    clause = np.random.choice(literals, size=3, replace=False)
    copy_clause = copy.deepcopy(clause)
    if not is_tautology(copy_clause):
        clauses.add(frozenset(clause))
    
for clause in clauses:
    for i, literal in enumerate(clause):
        if i != 2:
            file.write(str(literal))
            file.write(" + ")
        else:
            file.write(str(literal))
    file.write("\n")
    
start_node = Node([0, 0, 0, 0])
# print(start_node)
# for i in move_gen(start_node.values, 4, clauses):
    # print(i.values, i.e)

# print(evaluate_node(start_node, clauses))