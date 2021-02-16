"""
Example implementation of backtracking search in Python
"""

class node:
    def __init__(self, label: str):
        if(not isinstance(label, str)):
            raise ValueError
        self.label = label

    def __hash__(self):
        return hash(self.label)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["X", "Y"],
    "D": [],
    "E": [],
    "X": [],
    "Y": []
}

# children = ["A", "B", "C", "D"]
# d = ["A"]
# s = ["B"]
# nsl = ["C"]

def l_difference(*args):
    if not(all([isinstance(i, list) for i in args])):
        raise ValueError

    container = []
    for element in args:
        subcontainer = [i for i in element if i not in container]
        container.extend(subcontainer)
    return container

def l_union(a: list, b: list):
    # TODO : DUPLICATE CODE

    # source : https://stackoverflow.com/questions/9792664/converting-a-list-to-a-set-changes-element-order
    # find the union of two lists <- probably should use in Funnel

    if(not isinstance(a, list) or
       not isinstance(b, list)):
       raise ValueError('two lists please')
    return [x for x in a if x not in b]

def strip_containers(container: list, subdomains: list):
    subcontainer = []
    exit = False
    for element in container:
        for destination in subdomains:
            if(element in destination):
                exit = True
        if(not exit):
            subcontainer.append(element)
        exit = False
    return subcontainer

def backtracking(starting: str, GD: list) -> list:
    if(not isinstance(starting, str) or
       not isinstance(GD, list)):
        raise ValueError

    state_list, new_state_list = [starting], [starting]
    dead_ends = []
    current_state = starting
    max_depth, iterations = 100, 0

    while(new_state_list and iterations <= max_depth):
        iterations+=1
        if(current_state in GD):
            return state_list

        children = strip_containers(graph[current_state], [dead_ends, state_list, new_state_list])
        print(children)
        print(state_list)
        # children = l_union(graph[current_state],
                            # l_union(new_state_list, l_union(dead_ends, state_list)))
        if(not children):
            while((state_list) and (current_state == state_list[0])):
                dead_ends.append(current_state)
                state_list.pop()
                current_state = new_state_list.pop()
                # current_state = new_state_list.pop()
                # current_state = new_state_list[0]
            state_list.insert(0, current_state)
            # state_list.append(current_state)
        else:
            new_state_list[:0] = children
            # new_state_list.extend(children)
            # current_state = new_state_list.pop()
            current_state = new_state_list[0]
            # state_list.append(current_state)
            state_list.insert(0, current_state)

    if(iterations >= max_depth):
        print(f'[ERROR] Max recursion depth exceeded of {max_depth}, cowardly refusing to proceed')
    return []

resultant = backtracking("A", ["X"])
print(resultant)

# open_nodes = ["A"]

# state_list = open_nodes
# new_state_list = open_nodes
# dead_ends = []
# current_state = "A"
# goal_states = ["X"]

# while(state_list):
    # # current_state = state_list.pop()
    # print(current_state)
    # if(current_state in goal_states):
        # print(f'[complete] {state_list}') # should be return
    # children = graph[current_state]
    # if(not children):
        # while(state_list and current_state == state_list[0]):
            # dead_ends.append(current_state)
            # state_list.pop()
            # new_state_list.pop()
            # current_state = new_state_list[0]
        # state_list.append(current_state)
    # else:
        # new_state_list.extend(children)
        # current_state = new_state_list[0]
        # state_list.append(current_state)
