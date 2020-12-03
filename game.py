#import packages to extend python (just like we exted sublime, or Atom, or VSCode)
from gameComponents import gameVars, chooseWinner, Comparison

while gameVars.player is False:

	while gameVars.player_lives != 0 or gameVars.Ai_lives != 0:
		
		print("===============*/ RSP GAME */===============")
		print("Computer Lives: ", gameVars.Ai_lives, "/", gameVars.total_lives)
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

		# check to see what the user input

		#print outputs whatever is in the round vrackets -> in this case it outputs player to the command prompt window
		print("user chose: " + gameVars.player)
		
		Comparison.compare(gameVars.player)
		
		if gameVars.player_lives == 0:
			chooseWinner.winorlose("lost")

		if gameVars.Ai_lives == 0:
			chooseWinner.winorlose("won")
			
		print("________________")
		print("Player has", gameVars.player_lives, "lives left")
		print("AI has", gameVars.Ai_lives, "lives left\n")

		# make the loop keep running by setting player vack to False
		# unset, so that our loop condition above will evaluate to True
		gameVars.player = False