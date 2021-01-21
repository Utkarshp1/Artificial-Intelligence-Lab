def heuristic(start_node,current_node):
	start_block = start_node.blocks
	current_block = current_node.blocks
	count=0
	for i in range(len(start_block)):
		for j in range(len(start_block[i])):
			try:
				if current_block[i][j] is not None:
					if(start_block[i][j]==current_block[i][j]):
						x=0
					else:
						count = count + 1
				else:
					count = count + 1
			except Exception as e:
				count = count + 1
	return count