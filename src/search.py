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

    visited, open_nodes, answer_path, dead_ends = [], [], [], []

    def all_children_present(container: list, baseline: list):
        if(not container):
            return False
        for x in container:
            if(x not in baseline):
                return False
        return True

    def dfs(visited, node, answer_path, dead_ends):  #function for dfs 
        current_node, current_path, cost = node
        if(current_node not in visited):
            if(problem.isGoalState(current_node)):
                answer_path.append(current_path)
                raise ValueError # very, very cheap way to halt recursive calls

            visited.append(current_node)

            children = problem.getSuccessors(current_node)
            # print(f"called get successors of {current_node}")

            if(not answer_path):
                parent = node
            elif(len(answer_path) < 1 and answer_path):
                parent = answer_path[0]
            else:
                parent = answer_path[-1]

            if(parent in visited and
               all_children_present(problem.getSuccessors(parent), dead_ends)):
                answer_path.pop()

            if(current_node != problem.getStartState() and
               current_path):
                answer_path.append(current_path)


            if(not children or
               (all_children_present(children, dead_ends) and node not in dead_ends) or
               parent in dead_ends):
                dead_ends.append(answer_path.pop())
            for neighbour in children[::-1]: # iterate the list in reverse
                dfs(visited, neighbour, answer_path, dead_ends)
        return

    try:
        dfs(visited, (problem.getStartState(), None, float('inf')), answer_path, dead_ends)
    except ValueError:
        pass # we don't care about you 
    return answer_path



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
