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

children = ["A", "B", "C", "D"]
d = ["A"]
s = ["B"]
nsl = ["C"]

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

def backtracking(starting: str, GD: list) -> list:
    if(not isinstance(starting, str) or
       not isinstance(GD, list)):
        raise ValueError

    state_list, new_state_list = [starting], [starting]
    dead_ends = []
    current_state = starting
    if(current_state in GD):
        return state_list

    children = graph[current_state]
    if(not children)

# open_nodes = ["A"]

# state_list = open_nodes
# new_state_list = open_nodes
# dead_ends = []
# current_state = "A"
# goal_states = ["X"]

while(state_list):
    # current_state = state_list.pop()
    print(current_state)
    if(current_state in goal_states):
        print(f'[complete] {state_list}') # should be return
    children = graph[current_state]
    if(not children):
        while(state_list and current_state == state_list[0]):
            dead_ends.append(current_state)
            state_list.pop()
            new_state_list.pop()
            current_state = new_state_list[0]
        state_list.append(current_state)
    else:
        new_state_list.extend(children)
        current_state = new_state_list[0]
        state_list.append(current_state)
