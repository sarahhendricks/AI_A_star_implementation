import queue

import SearchGrid


x, y = 5, 5
open_queue = queue.PriorityQueue()
closed_queue = queue.PriorityQueue()
grid = SearchGrid.SearchGrid(x, y)

grid