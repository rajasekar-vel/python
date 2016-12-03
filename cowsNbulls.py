import random

def getInput():
	"Collects a 4 digit number from the User"
	while True:
		try:
			num = int(raw_input("Enter a 4 digit number : "))
			if num < 1000 or num > 9999:
				print "Please enter a 4 digit number"
			else:
				return num
				break
		except:
			print "Please enter a number"

def gamePlay():
	"Prints out the game Menu and controls the new Game"
	print "\nWelcome to cows and bulls game"
	print "Every correct guessed digit is a COW and a wrong guess is a BULL\n"
	
	while True:
		print "\nMenu"
		print "1.New Game"
		print "2.Exit\n"
		try:
			choice = int(raw_input("Your Option : "))
			if choice == 1:
				print "Starting a new game\n"
				newGame()				
			else:
				print "Exiting"
				break
		except:
			print "Please enter a digit"	
	
def newGame():
	"Contains the logic for game"
	sysNum = random.randint(1000,9999)
	sysNum_list = [dig for dig in str(sysNum)]
	s_dig1 = int(sysNum_list[0])
	s_dig2 = int(sysNum_list[1])
	s_dig3 = int(sysNum_list[2])
	s_dig4 = int(sysNum_list[3])
	userNum = 0
	while sysNum <> userNum:
		userNum = getInput()
		cow = 0
		bull = 0
		userNum_list = [dig for dig in str(userNum)]
		u_dig1 = int(userNum_list[0])
		u_dig2 = int(userNum_list[1])
		u_dig3 = int(userNum_list[2])
		u_dig4 = int(userNum_list[3])
		
		if s_dig1 == u_dig1:
			cow += 1
		else:
			bull += 1		
		if s_dig2 == u_dig2:
			cow += 1
		else:
			bull += 1
		if s_dig3 == u_dig3:
			cow += 1
		else:
			bull += 1
		if s_dig4 == u_dig4:
			cow += 1
		else:
			bull += 1
			
		print '%d cows, %d bulls' %(cow, bull)
		
		if cow == 4 and bull == 0:
			print "\n\nCongrats !!!, you have identified the number\n\n"
			
		
		
if __name__=="__main__":
	gamePlay()
	
	