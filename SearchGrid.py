import SearchNode

class SearchGrid(object):
    """description of class"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.n_nodes = self.height * self.width
        self.nodes = [SearchNode.SearchNode(x=_node % width, y=_node / height) for _node in range(self.n_nodes)]

    def get_node(self, x, y):
        return self.nodes[y * width + x]

      
            
        


