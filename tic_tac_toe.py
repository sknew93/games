class InputError(Exception):
	def __init__(self, message):
		self.message = message

# To display the board initlally and reset the board if there needs to be another round.
def reset_board():
	board = ["-","-","-"
			,"-","-","-"
			,"-","-","-"]
	return board

# To display the board initially and after each move is made. 
def display_board(board):
	print("_______     _______")
	print('|'+'1'+'|'+'2'+'|'+"3"+'|'+"     "+'|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
	print('|'+'4'+'|'+'5'+'|'+"6"+'|'+"<--->"+'|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
	print('|'+'7'+'|'+'8'+'|'+"9"+'|'+"     "+'|'+board[6]+'|'+board[7]+'|'+board[8]+'|')
	print('```````     ```````')

# The actual sequence followed by the game during GAMEPLAY.
def gameplay():
	board = reset_board()
	# Display the Board
	display_board(board)
	player_turn(board)
	again = input("Do you want to try again? (Y/N) : ").upper()
	if again == "Y":
		# pdb.set_trace()
		return gameplay()
	else:
		print('Thank you for playing. Come back Soon!')
		exit()

# To check for a winner after every move is made.
def check_for_winner(board):
	for i in [0,3,6]:
		if board[i]==board[i+1]==board[i+2]=="X" or board[i]==board[i+1]==board[i+2]=="O":
			return True
	for i in [0,1,2]:
		if board[i]==board[i+3]==board[i+6]=="X" or board[i]==board[i+3]==board[i+6]=="O":
			return True
	if board[0]==board[4]==board[8]=="X" or board[0]==board[4]==board[8]=="O":
		return True
	if board[6]==board[4]==board[2]=="X" or board[6]==board[4]==board[2]=="O":
		return True
	else:
		return False

# To take correct input from the two players sequentially
def player_input(id, board):
	try:
		raw_position = int(input(f'Player {id} : Please choose an available position from 1-9 : '))
		if 0 < raw_position < 10:
			if board[raw_position-1] == '-':
				return raw_position
			else:
				raise InputError(f'Sorry ! The position, {raw_position} has already been taken. Please choose a position, indicated with a \" - \".')
		else:
			raise ValueError
	except InputError as e:
		print(e.message)
		return player_input(id, board)
	except ValueError:
		print('ValueERROR! Only integers from 1-9 are accepted.')
		return player_input(id, board)

# To differentiate between the turns of the two players and also check  if there is a draw.
def player_turn(board):
	keys = ["X","O"]
	winner = False
	i = 0
	while winner == False:
		# print(i)
		if i%2==0:
			position = player_input(1, board)
			board[position-1] = keys[0]

		else:
			position = player_input(2, board)
			board[position-1] = keys[1]


		winner = check_for_winner(board)
		display_board(board)
		i += 1
		if winner is False and i== 9:
			print('The game has ended in a draw !')
			break



	if winner is True and (i-1)%2==0:
		print('Player 1 has WON!')
	if winner is True and (i-1)%2 != 0:
		print('Player 2 has WON!')



gameplay()



# board
# display board
# play game
# alternating X and O
# check win
	# check rows
	# check columns
	# check diagonals
# check tie
	#if board full and no win
# flip player who starts
