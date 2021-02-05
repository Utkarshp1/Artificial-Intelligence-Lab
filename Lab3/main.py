import sys
import numpy as np
import copy
from Literal import Literal
from utils import is_tautology
from utils import evaluate_node
from utils import move_gen
from utils import newmovegen
from Node import Node
from BeamSearch import BeamSearch
from VariableNeighbourhoodDescent import VariableNeighbourhoodDescent

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
start_node.e = evaluate_node(start_node, clauses)

# list_nvalid = []
# neighbours,list_nvalid = newmovegen(start_node.values,clauses,list_nvalid)
# for i in neighbours:
#     print(i.values,i.e)
# print(list_nvalid)
# neighbours,list_nvalid = newmovegen(start_node.values,clauses,list_nvalid)
# for j in neighbours:
#     print(j.values,j.e)
# print(list_nvalid)
# neighbours,list_nvalid = newmovegen(start_node.values,clauses,list_nvalid)
# for j in neighbours:
#     print(j.values,j.e)
# print(list_nvalid)
# print(start_node)
# for i in move_gen(start_node.values, 4, clauses):
    # print(i.values, i.e)

# print(evaluate_node(start_node, clauses))

# print(BeamSearch(2, clauses))
# print(VariableNeighbourhoodDescent(start_node, n, clauses))

# Good test case for VND with initial [0, 0, 0, 0] sol [1, 0, 1, 1]
# ~a + d + ~b
# c + a + ~d
# ~a + c + b
# a + ~d + ~b
# d + b + a