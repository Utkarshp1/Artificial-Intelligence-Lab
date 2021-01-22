def heuristic1(target_node,current_node):
	target_block = target_node.blocks
	current_block = current_node.blocks
	count=0
	for i in range(len(current_block)):
		for j in range(len(current_block[i])):
			try:
					if(target_block[i][j]==current_block[i][j]):
						count += 1
					else:
						count = count - 1
			except Exception as e:
				count = count - 1
	return -count
    
def heuristic2(target_node, current_node):
    target_block = target_node.blocks
    current_block = current_node.blocks
    count=0
    for i in range(len(current_block)):
        for j in range(len(current_block[i])):
            try:
                if(target_block[i][j]==current_block[i][j]):
                    count += j
                else:
                    count -= j
            except:
                count -= j
    return -count
    
def heuristic3(target_node, current_node):
    target_block = target_node.blocks
    current_block = current_node.blocks
    count = 0
    for i in range(len(current_block)):
        for j in range(len(current_block[i])):
            index = None
            for k in range(len(target_block)):
                try:
                    index = (k, target_block[k].index(current_block[i][j]))
                    break
                except:
                    continue
            count += abs(i - index[0]) + abs(j - index[1])
    return count