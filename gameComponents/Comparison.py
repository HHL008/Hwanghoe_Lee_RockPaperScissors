from gameComponents import gameVars
from game import computer

def compare(gameVars.player):

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