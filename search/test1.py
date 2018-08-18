def function():
    b = 0
    def function2 (c):
        c = 1

    function2(b)
    print b


function()


    def dfsexplore(v, action, state, visited, problem, actionSequence, solution):
        
        print "Current State: ", state
        if v not in visited:
            visited.append(v)
        actionSequence.append(action)
        print "Action Sequence: ", actionSequence
        # Check if current state is the goal state.
        if problem.isGoalState(state) == True:
            print "Goal found!"
            return actionSequence
        
        successors = problem.getSuccessors(state)
        for successor in successors:
            if successor[0] not in visited:
                dfsexplore(successor[0], successor[1], state, visited, problem, actionSequence, solution)
                visited.pop()
                actionSequence.pop()


    startState = problem.getStartState()
    state = (0, 0) # Initialize state variable
    visited = [startState]
    actionSequence = []
    solution = []
    
    print "State initialized at: ", startState
            
    initialSuccessors = problem.getSuccessors(startState)

    for successor in initialSuccessors:
        if successor[0] not in visited and not solution:
            dfsexplore(successor[0], successor[1], state, visited, problem, actionSequence, solution)
    
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    s = Directions.SOUTH
    w = Directions.WEST
    
    print "ALALALALAL: ", solution

    solution_list = []
    for direction in solution:
        if direction == "North":
            solution_list.append(n)
        elif direction == "East":
            solution_list.append(e)
        elif direction == "South":
            solution_list.append(s)
        elif direction == "West":
            solution_list.append(w)


    print solution_list
    return solution_list




#################################################
    sequence = []
    frontier = [] # frontier = open list = the set of all nodes available for expansion.
    explored = [] # explored nodes

    node = problem.getStartState() # state = root node
    frontier.append(node)
    

    if (problem.isGoalState(node) == True):
        return sequence

    while frontier:
        
        if not frontier: print "Failed." #Sanity check
        
        node = frontier.pop()
        print "expanding node: ", node

        if node in explored:
            continue


        for action in problem.getSuccessors(node):
            succNode = action[0]
            succDirec = action[1]
            print "succNode: ", succNode, " succDir: ", succDirec

            if succNode in explored:
                continue
            else:
                explored.append(node)
                if problem.isGoalState(node): return sequence
                frontier.append(succNode)        
