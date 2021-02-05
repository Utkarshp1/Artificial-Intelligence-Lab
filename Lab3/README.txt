Run the code using the command:
./run.sh [Beam-Width] [Tabu-Tenure] [OUTPUT-FILE]

Beam-Width: It is the number of neighbours to be considered in each iteration of
            Beam Search.
			
Tabu-Tenure: The maximum number of iterations for which the a bit after modification 
			 should be considered Tabu.
			 
OUTPUT-FILE: It is the file where the clauses will be written.
			 
For example,
./run.sh 2 2 output.txt