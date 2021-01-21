def heuristic(target_node,current_node):
	target_block = target_node.blocks
	current_block = current_node.blocks
	count=0
	for i in range(len(target_block)):
		for j in range(len(target_block[i])):
			try:
					if(target_block[i][j]==current_block[i][j]):
						count += 1
					else:
						count = count - 1
			except Exception as e:
				count = count - 1
	return -count