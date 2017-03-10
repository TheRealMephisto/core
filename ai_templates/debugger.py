
# Don't fork - just for testing (pretty bad AI; you might win against it)

import random

# CoRe
def turn(board, symbol):
	x = random.choice(range(8))
	y = random.choice(range(8))
	return (x,y)
