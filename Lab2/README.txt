Run the code using the command:
./run.sh [INPUT TEXT FILE] [ALGORITHM CHOICE] [HEURISTIC CHOICE]

Algorithm Choice:
	-bfs: Best First Search
	-hill: Hill Climbing
Heuristic Choice:
	A number between 1 and 3 (both inclusive)

For example,
./run.sh input.txt bfs 1

The input.txt file should be in the following format:
Initial State is:
[3, 5, 4]
[2, 6, 1]
[]

Goal State is
[4, 2]
[6, 1, 5, 3]
[]