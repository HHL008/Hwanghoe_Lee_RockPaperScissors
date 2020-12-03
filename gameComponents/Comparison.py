from random import randint
from gameComponents import gameVars

def compare(status):

# this will be the AI chiice -> random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	# adding in separation
	print("________________")

	if (computer == gameVars.player):
		print("tie! no one loses a life\n")

	#alwats check for negative conditions first (the losing case)	
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.Ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.Ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose! you lose a life :(\n")
			gameVars.player_lives -= 1

		else:
			print("you win! computer loses a life\n")
			gameVars.Ai_lives -= 1