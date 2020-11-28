from gameComponents import gameVars

#define a win or lose function
def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	print("You", status, "! would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()
	elif choice == "Y" or choice == "y":
		# reset the player lives and the AI lives
		# and set player to False so that our loop will restart

		gameVars.player_lives = 5
		gameVars.Ai_lives = 5
		gameVars.player = False

	# this still throws a bug - dosen't present the right choice
	else:
		print("Make a valid choice - Y or N")
		#this will generate a bug that we need to fix later
		choice = input("Y / N ")

		gameVars.player_lives = 5
		gameVars.Ai_lives = 5
		gameVars.player = False