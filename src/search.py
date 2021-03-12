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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Takes 2 arguments: a state in the search problem (main argument), and the problem itself (for reference information).
# Returns the estimated least cost from the current state to the destination


def nullHeuristic(state, problem):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    INF = -1  # -1 will signify the distance from the destination if it is not determined
    FOUND = 0

    # find h(n) - Perform a manhattan search (sum the distance we are from a goal state)
    h_n, min_val = INF, INF
    pair = []

    # Get this node's successors
    successors = problem.getSuccessors(state)

    # For each successor
    for successor in successors:
        node, direction, cost = successor
        if(min_val == INF):  # at the beginning of the list
            min_val = cost
        # If the problem is a goal state
        if problem.isGoalState(node):
            # Set the distance from the goal state to zero
            h_n = FOUND
            break
        else:
            # Else, find out the shortest distance from those successors to the goal state
            min_val = cost if(cost < min_val) else min_val
            pair = [f'{node}', cost]
            print(pair)
    h_n = min_val if(h_n != FOUND) else FOUND
    if(len(pair) == 2):
        node, _ = pair
    else:
        node = None
    print(f'{state} -> {node} has a heuristic of {min_val}')
    # h_n = min_val
    return h_n

# A* takes a heuristic function as an argument


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    """
    f(n) = g(n) + h(n)
    g(n) is the distance or cost from the start to current state, n
    h(n) is an estimate of the measure from state n to a goal
    h(n) guides search towards heuristically promising states, g(n) prevents search from indefinitely fruitless path
    """

    # problem - a tuple containing each index, [destination, direction, cost].

    INF = -1  # -1 will signify the distance from the destination if it is not determined
    runs = 0  # debugging

    # Set g(n) and h(n) for the starting state
    g_n = 0  # Cost from start
    h_n = INF  # Cost to destination

    state = problem.getStartState()
    open_set = util.Stack()

    # state - element we're at
    open_set.push([state, 'NONE', g_n])
    came_from = {}

    nextState = []
    solution = []

    # While we're not at the destination and haven't 'timed out'
    while runs < 10 and not open_set.isEmpty():
        f_n = INF  # assume the worst and cannot reach the destination

        # Unpack the current state and g_n
        state, direction, g_n = open_set.pop()

        if(problem.isGoalState(state)):
            print("found the goal")
            solution.append(direction)
            break

        # Get the current node's successors
        successors = problem.getSuccessors(state)

        for successor in successors:
            node, direction, cost = successor
            # Update successor's g(n) by adding the cost taken to get there from the previous state
            g_n += cost

            # Get the cost from a particular successor to the destination
            h_n = heuristic(node, problem)

            # determine f_n for that successor
            # If we've found a path from the start to the destination and it's less than our current best
            if (h_n != INF and g_n != INF) and ((g_n + h_n < f_n) or (f_n == INF)):
                f_n = g_n + h_n
                open_set.push([node, direction, g_n])
                solution.append(direction)

        # Update our next state

        # Decide which route to take by checking
        runs += 1

    # Return an empty solution
    print(state)
    return solution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
