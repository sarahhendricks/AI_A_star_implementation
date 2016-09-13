import SearchNode

class SearchGrid(object):
    """description of class"""
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.n_nodes = self.height * self.width
        self.nodes = [SearchNode.SearchNode(x=_node % width, y=_node / height) for _node in range(self.n_nodes)]

    def get_node(self, x, y):
        if x < 0 or y < 0 or y >= self.height or x >= self.width:
            #catches out of bounds
            return -1
        return self.nodes[y * width + x]

    def config(self, x, y, start=None, goal=None, traversable=None, g_cost=None, h_cost=None):
        #need to use kwargs when I get time
        index = self.get_node(x, y)
        if index < 0:
            return False
        node = self.nodes[index]
        if start is False or start is True:
            node.is_start = start
        if goal is False or goal is True:
            node.is_goal = goal
        if traversable is False or traversable is False:
            node.is_traversable = traversable
        if g_cost > 0:
            node.g_cost = g_cost
        if node.h_cost > 0:
            node.h_cost = node.h_cost
        self.nodes[index] = node
        return True