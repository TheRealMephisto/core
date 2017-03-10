
# CoRe Turn
def turn(board, symbol):
	for x in range(8):
		for y in range(8):
			if board[y][x] != '#' and board[y][x] != symbol:
				if x == 0 and y == 0 and board[1][1] == '#': return (1,1)
				if x == 0 and y == 7 and board[1][6] == '#': return (1,6)
				if x == 7 and y == 0 and board[6][1] == '#': return (6,1)
				if x == 7 and y == 7 and board[6][6] == '#': return (6,6)
				else:
					if at(board,x,y+1) == '#': return (x,y+1)
					if at(board,x+1,y) == '#': return (x+1,y)
					if at(board,x,y-1) == '#': return (x,y-1)
					if at(board,x-1,y) == '#': return (x-1,y)
	return (0,0)

def at(board,x,y):
	if not x in range(8): return None
	if not y in range(8): return None
	else: return board[y][x]
