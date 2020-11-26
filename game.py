#import packages to extend python (just like we exted sublime, or Atom, or VSCode)
from random import randint
from gameComponents import gameVars, chooseWinner#, Comparison


while gameVars.player is False:

	print("===============*/ RSP GAME */===============")
	print("Computer Lives: ", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("========================================")

	print("Choose your weapon! or type quit to exit\n")
	# this is the player choice
	gameVars.player = input("Choose rock, paper or scissors: \n")

	# if the player chose to quit, then exit the game
	if gameVars.player == "quit":
		print("you chose to quit")
		exit()

	# adding in separation
	print("________________")

	# this will be the AI chiice -> random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	# check to see what the user input

	#print outputs whatever is in the round vrackets -> in this case it outputs player to the command prompt window
	print("user chose: " + gameVars.player)
	
	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	# adding in separation
	print("________________")

	# MOVE THIS CHUNK OF CODE TO A PACKAGE - START HERE

	if (computer == gameVars.player):
		print("tie! no one loses a life\n")
		# print("________________")
		# print("Player has", player_lives, "lives left")
		# print("AI has", computer_lives, "lives left")

	#alwats check for negative conditions first (the losing case)	
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.computer_lives -= 1

	# STOP HERE - ALL OF THE ABOVE NEEDS TO MOVE

	if gameVars.player_lives == 0:
		chooseWinner.winorlose("lost")

	if gameVars.computer_lives == 0:
		chooseWinner.winorlose("won")
	
	print("________________")
	print("Player has", gameVars.player_lives, "lives left")
	print("AI has", gameVars.computer_lives, "lives left\n")

	# make the loop keep running by setting player vack to False
	# unset, so that our loop condition above will evaluate to True
	gameVars.player = False