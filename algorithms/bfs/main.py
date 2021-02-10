"""
Example implementation of BFS in Python
"""

import unittest

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["X", "Y"],
    "D": [],
    "E": [],
    "X": [],
    "Y": []
}

def l_union(a: list, b: list):
    # TODO : DUPLICATE CODE

    # source : https://stackoverflow.com/questions/9792664/converting-a-list-to-a-set-changes-element-order
    # find the union of two lists <- probably should use in Funnel

    if(not isinstance(a, list) or
       not isinstance(b, list)):
       raise ValueError('two lists please')
    return [x for x in a if x not in b]


def bfs(G: dict, S: list, GD: list) -> bool: # -> (TYPE BEING RETURNED)
    # type enforcement
    if(not isinstance(S, list) or # open nodes
       not isinstance(GD, list) or # acceptance states
       not isinstance(G, dict)): # graph in question
       raise ValueError

    X = None
    open_nodes = S
    goal_states = GD
    closed = []

    while(open_nodes):
        X = open_nodes.pop()
        if(X in goal_states):
            return True

        children = l_union(graph[X], open_nodes)
        open_nodes.extend(children) # append the contents of the lookup while removing duplicates from both containers
        closed.append(X)

    return False

class TestBFS(unittest.TestCase):
    def test_bfs_valid_dest(self):
        S, GD = ["A"], ["X"]
        self.assertTrue(bfs(graph, S, GD))
    def test_bfs_invalid_dest(self):
        S, GD = ["A"], ["Z"]
        self.assertFalse(bfs(graph, S, GD))

if __name__ == '__main__':
    unittest.main()
