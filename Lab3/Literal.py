class Literal:
    def __init__(self, value, is_not):
        self.value = value
        self.is_not = is_not
    
    def calculate_value(self, node):
        if self.is_not:
            return node[self.value]^1
        else:
            return node[self.value]
            
    def __str__(self):
        variables = ["a", "b", "c", "d"]
        return "~" + variables[self.value] if self.is_not else variables[self.value]
    
    def __eq__(self, other):
        if isinstance(other, Literal):
            return self.value == other.value and self.is_not == other.is_not
        return NotImplemented
        
    def __key(self):
        return (self.value, self.is_not)
        
    def __hash__(self):
        return hash(self.__key())