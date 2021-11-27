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
		print(Fore.CYAN+"Rock Paper Scissor level : "+str(level+1)+"----------- superpower left : "+str(superpower))
		userInput = int(input("Enter 1 for rock, 2 for paper and 3 for scissors. 4 for super power and 5 to quit :"))
		correctAnswer = (rockPaperScissor1[level]+1)%3 if rockPaperScissor1[level]+1 > 3 else rockPaperScissor1[level]+1
		if userInput==5:
			gameOver()
		elif userInput==4:
			if superpower==0:
				print(Fore.RED+"You dont have any superpower left. Please select any option")
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
				
		elif correctAnswer==userInput:
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
	
