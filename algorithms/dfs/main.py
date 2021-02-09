"""
Example implementation of DFS in Python

Components include:

X <- stores current state
open <- all nodes that we are allowed to push onto the stack
closed <- can no longer travel to

Please refer to L02, part 2 at 12:45 for further details
"""

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
    # source : https://stackoverflow.com/questions/9792664/converting-a-list-to-a-set-changes-element-order
    # find the union of two sets <- probably should use in Funnel

    if(not isinstance(a, list) or
       not isinstance(b, list)):
       raise ValueError('two lists please')
    return [x for x in a if x not in b]

X = None
open_nodes = ["A"]
goal_nodes = ["X"]
closed = []

while(open_nodes):
    X = open_nodes.pop()
    print(f'Current node {X}')
    if(X in goal_nodes):
        print("FOUND IT")
        break
    children = l_union(graph[X], open_nodes)
    open_nodes[:0] = children
    print(open_nodes)
    closed.append(X)

if(not X):
    print('failed')
