from util import *
from user import *
from constants import *

def rockPaperScissor(user):
	print()
	print()
	print(Fore.GREEN + '**************** STEPPING GLASS STONE ****************')
	print(Fore.GREEN + '******************************************************')
	print()
	superpower = 0
	if user.currentSuperpower==Superpower.EnhancedReflex.value:
		superpower = 1
		print(Fore.YELLOW+"You have 3 SuperStrength !!. Use all of them")
		print()
	level = 0
	while level < rockPaperScissorLength:
		print()
		print()
		print(Fore.CYAN+"Rock paper scissors level : "+str(level+1)+"----------- superpower left : "+str(Superpower(user.currentSuperpower).name)+"->"+str(Superpower(user.currentSuperpower).value))
		userInput = input("Enter 'rock', 'paper' or 'scissors'. Enter 'power' for superpower and 'q' to quit :")
		correctAnswer = (rockPaperScissor1[level]+1)%3 if rockPaperScissor1[level]+1 > 3 else rockPaperScissor1[level]+1

		sign=-1
		if userInput.strip().lower()=="q" or userInput.strip().lower()=="quit":
			sign=5
		elif userInput.strip().lower()=="power":
			sign=4
		elif userInput.strip().lower()=="rock" or userInput.strip().lower()=="r":
			sign=1
		elif userInput.strip().lower()=="paper" or userInput.strip().lower()=="p":
			sign=2
		elif userInput.strip().lower()=="scissors" or userInput.strip().lower()=="s":
			sign=3
		



		if sign==-1:
			print(Fore.RED+"Invalid input")

		elif sign==5:
			gameOver()
		elif sign==4:
			if superpower==0:
				print(Fore.RED+str(Superpower(user.currentSuperpower).name)+" has no use in this level.")
			else:
				print(Fore.YELLOW+"You used a superpower")
				print(Fore.MAGENTA+"************************ HINT ************************")
				superpower = superpower-1
				if rockPaperScissor1[level]==1:
					print(Fore.MAGENTA+"Opponent's palm is not opening.")
				elif rockPaperScissor1[level]==2:
					print(Fore.MAGENTA+"Opponent's palm is fully opening.")
				else:
					print(Fore.MAGENTA+"Opponent's two fingers are fully opening.")
				
		elif correctAnswer==sign:
			print(Fore.GREEN+"You picked correct option. Rock Paper Scissor level : "+str(level+1)+" cleared")
			level = level + 1
		else:
			print(Fore.RED+"Oops you picked a wrong choice. Eliminated")
			gameOver(user)
	user.currentStage = 0
	user.saveGame()
	print()
	print(Fore.GREEN+"Congratulations!!!!!  Rock paper scissors cleared.")
	print(Fore.YELLOW+"Bot : "+getBot(user)+" eliminated!")
	congratulations()
	
