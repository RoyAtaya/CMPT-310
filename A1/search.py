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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 20
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
I had a lot of trouble with heuristics, I still don't really know how to make a proper admissible and consistent heuristic.
The way I made the heuristic for Q2.2 was through logical reasoning
"""
#####################################################
#####################################################

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
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    
    myStack = util.Stack()  # make stack to hold unvisted nodes
    visitedNodes = [] # list of visited nodes to avoid infinite looping
    
    currNode = problem.getStartState()
    startTuple = (currNode, [])
    
    myStack.push(startTuple) # add starting node and empty array to hold directions to goal

    while not myStack.isEmpty(): # Check to see if stack is not empty
        currNode, currAction = myStack.pop() # pop the current node and the action pacman has to take to get there
        if problem.isGoalState(currNode): # check that we are not at the goal node
            return currAction
        
        if not(currNode in visitedNodes): #check if node has been visited
            visitedNodes.append(currNode) # add the unvisted node to visited node list
            
            newNode = problem.getSuccessors(currNode) # get the successor to the current node
            for nextNode in newNode:
                currNode = nextNode[0]
                pacDirection = nextNode[1]
                nextAction = currAction + [pacDirection] # next action that pacman has to take to get to the goal
                currTuple = (currNode, nextAction) # update the tuple
                myStack.push(currTuple) # push to the stack
    return []

def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    myQueue = util.Queue()  # make queue to hold unvisted nodes
    visitedNodes = [] # list of visited nodes to avoid infinite looping
    
    currNode = problem.getStartState()
    startTuple = (currNode, [])
    
    myQueue.push(startTuple) # add starting node and empty array to hold directions to goal

    while not myQueue.isEmpty(): # Check to see if queue is not empty
        currNode, currAction = myQueue.pop() # pop the current node and the action pacman has to take to get there
        if problem.isGoalState(currNode): # check that we are not at the goal node
            return currAction # return movement for pacman to take
        
        if not(currNode in visitedNodes): #check if node has been visited
            visitedNodes.append(currNode) # add the unvisted node to visited node list
            
            newNode = problem.getSuccessors(currNode) # get the successor to the current node
            for nextNode in newNode:
                currNode = nextNode[0]
                pacDirection = nextNode[1]
                nextAction = currAction + [pacDirection]  # next action that pacman has to take to get to the goal
                currTuple = (currNode, nextAction) # update the tuple
                myQueue.push(currTuple) # push to the queue
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    myPQueue = util.PriorityQueue()  # make queue to hold unvisted nodes
    visitedNodes = [] # list of visited nodes to avoid infinite looping
    
    currNode = problem.getStartState()
    startTuple = (currNode, [])
    actionCost = 0

    myPQueue.push(startTuple, nullHeuristic(currNode, problem)) # add starting node and empty array to hold directions to goal and the heurisitic for each node

    while not myPQueue.isEmpty(): # Check to see if queue is not empty
        currNode, currAction = myPQueue.pop() # pop the current node and the action pacman has to take to get there
        if problem.isGoalState(currNode): # check that we are not at the goal node
            return currAction # return movement for pacman to take
        
        if not(currNode in visitedNodes): #check if node has been visited
            visitedNodes.append(currNode) # add the unvisted node to visited node list
            newNode = problem.getSuccessors(currNode) # get the successor to the current node
            # have to change the below most probably
            for nextNode in newNode:
                currNode = nextNode[0]
                pacDirection = nextNode[1]
                nextAction = currAction + [pacDirection] # next action that pacman has to take to get to the goal
                currTuple = (currNode, nextAction) # update tuple
                actionCost = problem.getCostOfActions(nextAction) + heuristic(currNode,problem) # f(n) = cost(n) + h(n)
                myPQueue.push(currTuple,  actionCost) # push to the queue
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
