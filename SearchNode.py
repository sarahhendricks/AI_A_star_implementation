class SearchNode(object):
    """description of class"""
    blocked = "X"
    free = ""
    def __init__(self, x=0, y=0, traversable=True, h_cost=0, g_cost=0):
        self.is_traversable=traversable
        self.h_cost=h_cost
        self.g_cost=g_cost
        self.x = x
        self.y = y

    def to_string(self):
        return blocked if not self.is_traversable else free
