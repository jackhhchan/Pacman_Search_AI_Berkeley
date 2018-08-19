import search
from searchAgents import PositionSearchProblem

from pacman import GameState
import layout

# Create GameState object.
#gameState = GameState()
#layout_ = layout.getLayout( 'tinyMaze' )
#gameState.initialize(layout_, 4) #initialize layout for gameState object.

#sequence = search.uniformCostSearch(PositionSearchProblem(gameState))

#print ""
#print "Solution Sequence: ", sequence

import util

frontier = util.PriorityQueue()

frontier.push((5,5), 10)

test = frontier.pop()

print 'frontier.pop(): ', test