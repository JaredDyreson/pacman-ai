# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
# user made functions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    "*** YOUR CODE HERE ***"
    current_node    = None
    current_path    = None
    open_nodes = [(problem.getStartState(), None)]

    closed_nodes = []
    answer_path = [] # return me

    while(open_nodes != []):                                            #While there's no open nodes                         
        current_node, current_path = open_nodes.pop(0)                  #remove the leftmost state from open, call it current_node
        if(problem.isGoalState(current_node)):                          #If current_node is a goal then return the NODE
            answer_path.append(current_path)
            return answer_path
        successors = problem.getSuccessors(current_node)                #Otherwisem generate the children of current_node
        closed_nodes.append(current_node)                               #put current_node on closed

        #If the current node isn't our starting node, has successors and is part of the current path
        if(current_node != problem.getStartState() and successors and current_path):
            answer_path.append(current_path)                            #Add it to our answer_path
        
        temp = []
        for element in successors:
            node, path, cost = element
            if node not in open_nodes and node not in closed_nodes:     #discard children of current_node if already on open or closed
                temp.insert(0, [node, path])
        open_nodes[:0] = temp
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    current_node = None
    open_nodes = [problem.getStartState()]
    open_paths = []
    closed = [] # return me

    while(open_nodes != []):                                    #While there's no open nodes
        current_node = open_nodes.pop(0)                        #remove the leftmost state from open, call it current_node
        if(problem.isGoalState(current_node)):                  #If current_node is a goal then return the NODE
            return closed
        container = problem.getSuccessors(current_node)         #Otherwisem generate the children of current_node
        closed.append(current_node)                             #put current_node on closed
        temp = []
        for element in container:
            node, path, cost = element
            if node not in open_nodes and node not in closed:   #discard children of current_node if already on open or closed
                temp.append(node)                               #put remaining children on left end of open
        open_nodes.extend(temp)                                   # prepend the contents of the lookup while removing duplicates from both containers

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
