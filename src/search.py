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
from algorithms.dfs.main import l_union # list union


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

    current_node = None
    open_nodes = [(problem.getStartState(), None)]
    closed = [] # return me 
    paths = [] # stack based approach
    dead_ends = []

    depth_limit = 100
    iterations = 0

    while(open_nodes):                                    #While there's no open nodes
        if(iterations == depth_limit):
            print(f'[WARNING] Depth limit of {depth_limit} has been reached, cowardly refusing')
            break
        print(f'current dead ends {dead_ends}')
        print(f'current open nodes {open_nodes}')
        print(f'current paths: {paths}')
        current_node, current_path = open_nodes.pop(0)                        #remove the leftmost state from open, call it current_node
        if(problem.isGoalState(current_node)):                  #If current_node is a goal then return the NODE
            paths.append(current_path)
            return paths
        if(current_node in dead_ends):
            continue

        # entry point
        successors = problem.getSuccessors(current_node)         #Otherwisem generate the children of current_node
        closed.append(current_node)                             #put current_node on closed
        holding = []

        if(not successors):
            # hit bottom of call stack
            # we cannot branch out any further so we can confidently say this node is a dead end
            # the above if statement does a pre-check to ensure we are not discarding a goal node

            dead_ends.insert(0, current_node)

        if(current_node != problem.getStartState() and successors and current_path):
            paths.append(current_path)

        for state in successors:
            # if we put path in the paths container, we unconditionally do so
            # this will not work because we might not have processed all nodes in the queue to make a correct judgement
            node, path, cost = state
            if(node in dead_ends):
                continue
            # put remaining children on left most end of the open queue
            holding.insert(0, (node, path))

            # prepend the contents of the lookup while removing duplicates from both containers
            open_nodes[:0] = l_union(holding, open_nodes)
            # discard children of current_node if already on open or closed
        iterations+=1
    return []

    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
