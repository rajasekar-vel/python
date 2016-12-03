# RockPaperScissors Game (Validations needs to be added)
import getpass as gp

while True:
	
	print "\nWelcome to Rock Paper Scissors\n"
	inp = int(raw_input("What do you want to do ?\n 1) Start a new Game \n 2) Exit\n Your Option :"))
	
	if inp == 1:
		print "\nUse r (rock),p(paper),s(scissors) \n"
		player1 = gp.getpass("Player 1 Choice (Rock/Paper/Scissors) :")
		player2 = gp.getpass("Player 2 Choice (Rock/Paper/Scissors) :")	

		if (player1 == player2):
			print "\nMatch Drawn"
			print "Player 1 Choice : %s\nPlayer 2 Choice : %s" %(player1,player2)

		elif (player1=='p' and player2 =='r'):
			print "\nPlayer 1 Won"
			print "Player 1 Choice : %s\nPlayer 2 Choice : %s" %(player1,player2)	

		elif (player1=='s' and player2 =='p'):
			print "\nPlayer 1 Won"
			print "Player 1 Choice : %s\nPlayer 2 Choice : %s" %(player1,player2)

		elif (player1=='r' and player2 =='s'):
			print "\nPlayer 1 Won"
			print "Player 1 Choice : %s\nPlayer 2 Choice : %s" %(player1,player2)

		else:
			print "\nPlayer 2 Won"
			print "Player 1 Choice : %s\nPlayer 2 Choice : %s" %(player1,player2)
	else:
		print "Exiting"
		break
	
	






