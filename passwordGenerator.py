import random

class PasswordGenerator:
	"Contains all methods related to password generation"
	global UPPERCASE,LOWERCASE,numbers,symbols
	UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
	numbers = '0123456789'
	symbols = '-/@#$%&*!'
	
	def genPW(self,length):
		"Function genPW generates and returns a password based on the lenth passed"
		word = UPPERCASE + LOWERCASE+numbers+symbols
		pwd = random.sample(word,length)		
		return ''.join(pwd)

	def getLength(self):
		"getLenth collects the password length from the User"
		while True :
			try:
				length = int(raw_input("Enter the length of the password (4-32) : "))
				if length < 4 or length > 32:
					print "Please enter a number between 4 and 32 "
				else:
					return length
					break
			except:
				print "Please enter a number"						
		


pd = PasswordGenerator()
print pd.genPW(pd.getLength())



	


	
	