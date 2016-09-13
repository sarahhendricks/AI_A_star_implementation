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
