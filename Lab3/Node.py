class Node:
    def __init__(self, values):
        self.values = values
        self.e = None
        
    def __eq__(self, other):
        '''
            Function to compare the two objects of node.
        '''
        if other is not None:
            return self.values == other.values
            
    def __lt__(self, other):
        '''
            Function to check whether one node is less than the other node.
        '''
        if other is not None:
            return self.e < other.e
            
    def __str__(self):
        return str(self.values)