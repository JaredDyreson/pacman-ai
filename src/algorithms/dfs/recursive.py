# Using a Python dictionary to act as an adjacency list
# source : https://favtutor.com/blogs/depth-first-search-python

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["X", "Y"],
    "D": [],
    "E": [],
    "X": [],
    "Y": []
}

visited = []
answer_path = []
dead_ends = []
goal_node = "X"
parent = None

def all_children_present(container: list, baseline: list):
    if(not container):
        return False
    for x in container:
        if(x not in baseline):
            return False
    return True

def dfs(visited, graph, node, answer_path, dead_ends):  #function for dfs 
    if(node not in visited):
        if(node == goal_node):
            answer_path.append(node)
            return
        visited.append(node)
        children = graph[node]

        if(not answer_path):
            parent = node
        elif(len(answer_path) < 1 and answer_path):
            parent = answer_path[0]
        else:
            parent = answer_path[-1]

        if(parent in visited and
           all_children_present(graph[parent], dead_ends)):
            answer_path.pop()
        answer_path.append(node)

        if(not children or
           (all_children_present(children, dead_ends) and node not in dead_ends) or
           parent in dead_ends):
            dead_ends.append(answer_path.pop())
        for neighbour in children:
            dfs(visited, graph, neighbour, answer_path, dead_ends)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A', answer_path, dead_ends)

print(answer_path)

