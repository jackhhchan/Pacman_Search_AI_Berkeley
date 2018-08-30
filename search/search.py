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
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    


    # Get Starting Node & return empty list if its the goal state.
    node = problem.getStartState()
    if problem.isGoalState(node): return []

    actions = []
    cost = 0
    frontier = util.Stack()                             # Initiate frontier
    frontier.push((node, actions))                      # Push starting state to frontier.

    explored = util.Stack()                             # Initiate explored 
    while not frontier.isEmpty():
        currentState, actions = frontier.pop()          # current state popped off the frontier stack.
        if problem.isGoalState(currentState): return actions
       

        if currentState not in explored.list and currentState not in frontier.list:
            explored.push(currentState)                # Update state to explored

            # Expand current state
            for succState, succAction, succCost in problem.getSuccessors(currentState):

                if succState not in explored.list:
                    accuActions = actions + [succAction]        # Accumulate actions to next successor.
                    frontier.push((succState, accuActions))     # Push successor to frontier.
    
    return []   # Goal state not found.

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    node = problem.getStartState()                 
    if problem.isGoalState(node): return actions   # Check if start state = goal state
    
    actions = []
    cost = 0
    frontier = util.Queue()           # Frontier data structure initialised as Queue.
    frontier.push((node, actions, cost))    # Initialize frontier with startState

    explored = util.Stack()           # Initialize explored
    while not frontier.isEmpty():
        currentState, actions, cost = frontier.pop() # Pop first state in frontier.

        if problem.isGoalState(currentState): return actions     # Check if current state = goal state
        
        if currentState not in explored.list and currentState not in frontier.list:   
            explored.push(currentState)                # Add current state to explored.

            # Expand current node.
            for succState, succAction, succCost in problem.getSuccessors(currentState):  # Get successors from currentNode.
                if succState not in explored.list:
                    accuActions = actions + [succAction]    # Accumulate actions to successor state.
                    accuCost = cost + succCost              # Accumulate cost.
                    frontier.push((succState, accuActions, accuCost)) # Add frontier with successor.

    return []   # Goal state not found.



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    frontier = util.PriorityQueue()                             # Initialise frontier with priority queue.

    node = problem.getStartState()
    if problem.isGoalState(node): return []                     # Check if starting state = goal state.

    actions = []
    cost = 0
    frontier.update((node, actions, cost), cost)

    explored = util.Stack()
    while not frontier.isEmpty():
        currentState, actions, costs = frontier.pop()
        if problem.isGoalState(currentState): return actions     # Goal state checked when node is selected for expansion.
        
        if currentState not in explored.list and currentState not in frontier.heap:
            explored.push(currentState)                         # Update current state to explored.

            for succState, succAction, succCost in problem.getSuccessors(currentState):
                if succState not in explored.list:
                    accuActions = actions + [succAction]
                    accuCost = costs + succCost
                    frontier.update((succState, accuActions, accuCost), accuCost)       # Update frontier with successor.

    
    return [] # Goal state not found.
        


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    node = problem.getStartState()  # Get start state of the problem.
    if problem.isGoalState(node): return [] # Check if start state = goal state.

    frontier = util.PriorityQueue() # Initialize frontier with Priority Queue.
    actions = []
    costs = 0
    eval = 0
    frontier.push((node, actions, costs), eval)

    explored = util.Stack()
    while not frontier.isEmpty():
        currentState, actions, costs = frontier.pop()

        if problem.isGoalState(currentState): return actions        # Check if current state = goal state

        if currentState not in explored.list and currentState not in frontier.heap:
            explored.push(currentState)                             # Add current state to explored.

            # Expanding current state
            for succState, succAction, succCost in problem.getSuccessors(currentState):
                if succState not in explored.list:
                    accuActions = actions + [succAction]
                    accuCosts = costs + succCost
                    eval = accuCosts + heuristic(succState, problem)                # f = g + h
                    frontier.update((succState, accuActions, accuCosts), eval)      # Add successors to frontier.

    return [] # Goal state not found.



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
