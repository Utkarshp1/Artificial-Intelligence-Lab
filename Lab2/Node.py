class Node:
    def __init__(self):
        self.blocks = []
        self.h = None
        self.parent = None
        self.child = None
        
    def __eq__(self, other):
        if other is not None:
            return self.blocks == other.blocks
            
    def __lt__(self, other):
        if other is not None:
            return self.h < other.h