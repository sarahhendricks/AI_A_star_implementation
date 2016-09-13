import SearchNode

class SearchGrid(object):
    """description of class"""
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.n_nodes = self.height * self.width
        self.nodes = [SearchNode.SearchNode(x=_node % width, y=_node / width) for _node in range(self.n_nodes)]

    def set_to_traversable(self, list_of_indexes, is_traversable):
        """Set a list of points (or a single point) travesersibilty to is_traverrsable"""
        if isinstance(list_of_indexes, int):
            list_of_indexes = list(list_of_indexes)
        for index in list_of_indexes:
            self.nodes[index].is_traversable = is_traversable
    
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

    def equals(self, first_node, second_node):
        """Returns True if the two passed nodes are the same node.
        The variables x and y act as a set of keyes for the nodes"""
        return first_node.x == second_node and first_node.y == second_node.y

    def get_traversable_neighbors(self, start_node):
            """Get all the nodes that can be reached from start_node."""
            x = start_node.x
            y = start_node.y
            possible_neighbors_coordinates = [(x + 1, y - 1), (x, y + 1), (x - 1, y - 1),
                                              (x, y + 1), (x, y - 1), (x - 1, y + 1),
                                              (x - 1, y), (x - 1, y - 1)]
            neighbors = [self.get_node(*coordinates) for coordinates in possible_neighbors_coordinates]
            traversable_neighbors = [neighbor for neighbor in neighbors if neighbor.is_traversable]


    def get_coordinates(self, index):
        """Convert integer index to Cartesian coordinate."""
        if index >= self.n_nodes or index < 0:
            return (-1, -1)
        return (index / width, index % width)
    
    def get_node(self, x, y):
        """Get node from Cartesian coordinates."""
        if x < 0 or y < 0 or y >= self.height or x >= self.width:
            #catches out of bounds
            return -1
        return self.nodes[y * width + x]

    def get_start_index(self):
        """Get the index of the start node"""
        for index, node in enumerate(self.nodes):
            if node.is_start:
                return index
        return -1
