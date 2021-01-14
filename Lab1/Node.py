class Node:
    def __init__(self):
        self.value = ''     # values can be +,-,|,* or blank
        self.color = 'white'
        self.distance = -1  # distance from [0][0] in tree
        self.parent = None
        self.x = -1    # coordinates of node
        self.y = -1

    def __str__(self):   # printing
        return self.value + " " + str(self.x) + " " + str(self.y) + " dis: " + str(self.distance)