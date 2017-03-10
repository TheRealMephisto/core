
# CoRe Turn
def turn(board, symbol):
	for x in range(8):
		for y in range(8):
			if board[y][x] == '#': # Empty
				return (x,y)
			elif board[y][x] == symbol: # Self
				pass
			else: # Other
				pass
