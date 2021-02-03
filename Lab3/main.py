import sys
import numpy as np
import copy

def is_tautology(clause):
    for i in range(3):
        clause[i] = clause[i].replace("~", "")
    
    if len(set(clause)) == 3:
        return False
        
    return True

file = open(sys.argv[1], "w")
n = 4
k = 5

literals = ["a", "~a", "b", "~b", "c", "~c", "d", "~d"]
clauses = set()

while len(clauses) != 5:
    clause = np.random.choice(literals, size=3, replace=False)
    copy_clause = copy.deepcopy(clause)
    if not is_tautology(copy_clause):
        clauses.add(tuple(clause))
    
for clause in clauses:
    file.write(" + ".join(clause) + "\n")