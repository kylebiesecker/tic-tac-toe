import itertools
global tempList


def horizontal_win_check(game):
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != 0:
			return True, print(f"Player {row[0]} got a horizontal win!(-)")
					

def vertical_win_check(game):
	for col in range(len(game)):
		tempList = []
		for row in game:
			tempList.append(row[col])
		if check_tempList(tempList):
			print(f"Player {tempList[0]} got a vertical win!(|)")
			return True


def left_diagonal_win_check(game):
	tempList = []
	for index in range(len(game)):
		tempList.append(game[index][index])
	if check_tempList(tempList):
		print(f"Player {tempList[0]} got a top left diagonal win!(\\)")
		return True


def right_diagonal_win_check(game):
	tempList = []
	for col, row, in enumerate(reversed(range(len(game)))):
		tempList.append(game[col][row])
	if check_tempList(tempList):
		print(f"Player {tempList[0]} got a top right diagonal win!(/)")
		return True


#checks a temporary list of each win-con item for count of first item to equal length of list
def check_tempList(tempList):
	if tempList.count(tempList[0]) == len(tempList) and tempList[0] != 0:
		return True
	else:
		return False


def check_all_wincons(game):
	if(right_diagonal_win_check(game) or
	left_diagonal_win_check(game) or
	horizontal_win_check(game) or
	vertical_win_check(game)):
		return True


#prints the game board using a for loop and enumerate method and basic print statement
def game_board(game_map, player=0, row=0, column=0, just_display=False): 
	try:
		if game_map[row][column] != 0:
			print("This position is already taken, please choose another")
			return game_map, False
		print("\n\n   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True
	except IndexError as e:
		print("Error: check that input is 0, 1, or 2. Currently:",e)
		return game_map, False
	except Exception as e:
		print("Something went wrong! ", e)
		return game_map, False


def run_game(play = True, players = [1,2], game_won = False, current_player = itertools.cycle([1,2])):
	#play is set to false when players opt to not play again after a finished game
	while play:
		game = [[0,0,0],
				[0,0,0],
				[0,0,0]]
		game, _ = game_board(game, just_display=True)

		#game_won is set to true if one wincon is found to be true
		while not game_won:
			player_choice = next(current_player)
			print(f"Current Player: {player_choice}")

			#played is set to true if game_board function is able to return with no error
			played = False
			while not played:
				col_choice = int(input("What column would you like to play? (0, 1, 2): "))
				row_choice = int(input("What row would you like to play? (0, 1, 2): "))
				game, played = game_board(game, player_choice, row_choice, col_choice)
				
			if check_all_wincons(game):
				game_won = True
				again = input("The game is over, would you like to play again? y/n: ")
				if again.lower() == "y":
					print("restarting")
				else:
					print("goodbye!")
					play = False


run_game()