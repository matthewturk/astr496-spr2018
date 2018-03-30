refinement_criteria = 32

class Node:
    def __init__(self, left_edge, right_edge):
        self.left_edge = left_edge
        self.right_edge = right_edge
        self.items = []
        self.children = []

    def find_action(self, value):
        if len(self.children) == 0:
            return self
        midpoint = (self.left_edge + self.right_edge)/2
        if value < midpoint:
            return self.children[0].find_action(value)
        else:
            return self.children[1].find_action(value)

    def add_action(self, action, points):
        if len(self.children) > 0:
            midpoint = (self.left_edge + self.right_edge)/2
            if points < midpoint:
                self.children[0].add_action(action, points)
            else:
                self.children[1].add_action(action, points)
            return
        self.items.append( (points, action) )
        if len(self.items) > refinement_criteria:
            midpoint = (self.left_edge + self.right_edge)/2
            child_left = Node(self.left_edge, midpoint)
            child_right = Node(midpoint, self.right_edge)
            self.children = [child_left, child_right]
            for value, action in self.items:
                if value < midpoint:
                    child_left.add_action( action, value )
                else:
                    child_right.add_action( action, value )
            self.items = []

actions1 = "Repairing a tricycle for a child that loves tricycles", 1.0
actions2 = "Repairing a tricycle for a child indifferent to tricycles", 0.1
actions3 = "Blowing up Starkiller Base", 0.8
actions4 = "Rooting against UIUC", -0.8
actions5 = "Rooting against Loyola", -1.0
actions6 = "Petting a dog", 0.5
actions7 = "Sneezing", 0.01
actions8 = "You didn't recognize your father", -0.2
actions9 = "Not reading APOD for two weeks", -0.4

root_node = Node( -1.0, 1.0 )
#root_node.add_action( *actions1 )
#root_node.add_action( *actions2 )
#root_node.add_action( *actions3 )
#root_node.add_action( *actions4 )
#root_node.add_action( *actions5 )
#root_node.add_action( *actions6 )
#root_node.add_action( *actions7 )
#root_node.add_action( *actions8 )
#root_node.add_action( *actions9 )

import numpy as np
values = np.random.normal(size = (3200), scale = 0.05)
np.clip(values, -1.0, 1.0, values)

for i, v in enumerate(values):
    root_node.add_action( i, v )
