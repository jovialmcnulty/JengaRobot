# import the necessary packages
import numpy as np

#--------------------------------- Picking block function start ---------------------------------
def pick_block(tower_state):
	block_index = [0,0]

	toprows = len(tower_state)-3

	x = 5;
	for x in range(2, toprows):
		if (tower_state[x][0]==1 and tower_state[x][1]==1 and tower_state[x][2]==1):
			block_index[0] = x;
			block_index[1] = 1;
			return block_index
#--------------------------------- Picking block function end ---------------------------------




#--------------------------------- Testing picking block function start ---------------------------------
tower_state = np.array([[1, 1, 1],
			[1, 1, 1], 
			[1, 1, 1],
			[1, 1, 1], 
			[1, 1, 1],
			[1, 1, 1], 
			[1, 1, 1],
			[1, 1, 1], 
			[1, 1, 1],
			[1, 1, 1], 
		    	[1, 1, 1],
			[1, 1, 1], 
		    	[1, 1, 1],
			[1, 1, 1], 
		    	[1, 1, 1],
			[1, 1, 1], 
		    	[1, 1, 1],
			[1, 1, 1]])

block_index = pick_block(tower_state)
print("\nBlock Index: ["+str(block_index[0])+"]["+str(block_index[1])+"]\n")
#--------------------------------- Testing picking block function end ---------------------------------
