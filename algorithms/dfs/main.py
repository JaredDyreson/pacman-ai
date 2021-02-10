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
    # find the union of two lists <- probably should use in Funnel

    if(not isinstance(a, list) or
       not isinstance(b, list)):
       raise ValueError('two lists please')
    return [x for x in a if x not in b]

# parameters have their desired types
def dfs(G: dict, S: list, GD: list) -> bool: # -> (TYPE BEING RETURNED)
    # type enforcement
    if(not isinstance(S, list) or
       not isinstance(GD, list) or
       not isinstance(G, dict)):
       raise ValueError

    X = None
    open_nodes = S # renaming
    goal_nodes = GD # renaming
    closed = []

    while(open_nodes): # while len(open_nodes) > 0, python is cool
        X = open_nodes.pop()
        if(X in goal_nodes):
            return True
        children = l_union(graph[X], open_nodes)
        open_nodes[:0] = children # prepend the contents of the lookup while removing duplicates from both containers
        closed.append(X) # current node exhausted

    return False

resultant = dfs(graph, ["A"], ["X"])

if(resultant):
    print("[INFO] We found a result")
else:
    print("[ERROR] We could not find a result")
