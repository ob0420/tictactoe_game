game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0],]

def win(current_game):
	for row in game:
		print(row)
		col1 = row[0]
		col2 = row[1]
		col3 = row[2]

		if col1 == col2 == col3:
			print("winner!!!")
win(game)
