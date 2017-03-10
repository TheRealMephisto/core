
import random

# CoRe
def turn(board, symbol):
	while 1:
		x = random.choice(range(8))
		y = random.choice(range(8))
		if board[y][x] == '#': return (x,y)
