import queue

import SearchGrid


x, y = 5, 5
open_queue = queue.PriorityQueue()
closed_queue = []
grid = SearchGrid.SearchGrid(x, y)
n=[]
f=0

def seenbefore(node):
	for entry in closed_queue:
		if node.equals(entry):
			if node.f>entry.f:
				return True:
			else:
				b=closed_queue.index(entry)
				del closed_queue[b]
				closed_queue.add[node]
				return False:
	return False

grid
#user input for goal - goalnode
##user input for start- startnode
def search():
	open_queue.add(startnode(#set f value)) #f value =g(S)+h(S)
	if open_queue.empty():
		print "No solution!"
		return
	else:
		n=open_queue.get()
		if n.equals(goalnode): 
			print "Found it!"
			return n.lineage #list of parent, then parent's parent, all the way back to start
		else:
			for successor in n.neighbors: #list of n's traversible neighbors
				f = successor.g + successor.h
				if ((successor) not in closed_queue or seenbefore(sucessor) (successor in closed_queue and f) ???
				If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’



