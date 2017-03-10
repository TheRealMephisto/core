import gamelib

def initialize_board():
	board = []
	for x in range(8):
		board.append([])
		for y in range(8):
			board[x].append('#')
	return board

def board_is_full(board):
	for line in board:
		for item in line:
			if item == '#': return False
	return True

def score(board):
	player_1 = 0
	player_2 = 0
	for line in board:
		for item in line:
			if item == 'X': player_1 += 1
			if item == 'O': player_2 += 1
	return (player_1, player_2)

def flip_the_shit_out_of_it(board, x, y, player, other):
	# right side of it
	found = False
	for i in range(x+1,8):
		if board[y][i] == player: found = True
	if found:
		flipped = False
		for i in range(x+1,8):
			if board[y][i] == player: break
			elif board[y][i] == other:
				flipped = True
				board[y][i] = player
		if flipped: gamelib.report('Flip right!')
	# left side of it
	found = False
	for i in range(x)[::-1]:
		if board[y][i] == player: found = True
	if found:
		flipped = False
		for i in range(x)[::-1]:
			if board[y][i] == player: break
			elif board[y][i] == other:
				flipped = True
				board[y][i] = player
		if flipped: gamelib.report('Flip left!')
	# bottom side of it
	found = False
	for i in range(y+1,8):
		if board[y][i] == player: found = True
	if found:
		flipped = False
		for i in range(y+1,8):
			if board[i][x] == player: break
			elif board[i][x] == other:
				flipped = True
				board[i][x] = player
		if flipped: gamelib.report('Flip bottom!')
	# upper side of it
	found = False
	for i in range(y)[::-1]:
		if board[i][x] == player: found = True
	if found:
		flipped = False
		for i in range(y)[::-1]:
			if board[i][x] == player: break
			elif board[i][x] == other:
				flipped = True
				board[i][x] = player
		if flipped: gamelib.report('Flip top!')

@gamelib.game('CoRe', 'Computer Reversi')
def game(*ai_list):
	board = initialize_board()
	player = 1 # becomes 0 at first switch
	while True:
		if board_is_full(board): break
		gamelib.turn() # <- increases a counter value
		player = 1-player # switch player
		symbol = 'XO'[player]
		pos_x, pos_y = gamelib.get(ai_list[player], 'turn')(gamelib.copy_board(board), symbol)
		if pos_x in range(8) and pos_y in range(8) and board[pos_y][pos_x] == '#':
			gamelib.report('Player {} moved to {},{}'.format(player+1,pos_x+1,pos_y+1))
			board[pos_y][pos_x] = symbol
			flip_the_shit_out_of_it(board, pos_x, pos_y, player=symbol, other='OX'[player])
		else:
			gamelib.report('Player {} can not move to {},{}'.format(player+1,pos_x+1,pos_y+1))
		gamelib.display_board(board)
	(player_1, player_2) = score(board)
	gamelib.report('Score: {} / {}'.format(player_1, player_2))
	if player_1 > player_2:
		gamelib.report('Player 1 won!')
	if player_2 > player_1:
		gamelib.report('Player 2 won!')
	if player_1 == player_2:
		gamelib.report("It's a tie!")
