from util import *
from user import *
from constants import *

def steppingGlassStone(user):
	print()
	print()
	print(Fore.GREEN + '**************** STEPPING GLASS STONE ****************')
	print(Fore.GREEN + '******************************************************')
	print()
	superpower = 0
	if user.currentSuperpower==Superpower.EnhancedVision.value:
		superpower = 2
		print(Fore.YELLOW+"You have 2 Enhanced vision !!. Use all of them")
		print()
	level = 0
	while level < steppingGlassLength:
		print()
		print()
		print(Fore.CYAN+"Stepping glass stone level : "+str(level+1)+"----------- superpower left : "+str(superpower))
		userInput = int(input("Enter 1 or 2 for stepping on glass of your choice. 4 for super power and 5 to quit :"))
		if userInput==5:
			gameOver()
		elif userInput==4:
			if superpower==0:
				print(Fore.RED+"You dont have any superpower left. Please pick any step")
			else:
				print(Fore.YELLOW+"You used a superpower")
				print(Fore.MAGENTA+"************************ HINT ************************")
				if steppingGlass[level][0]==0:
					print(Fore.MAGENTA+"2nd Glass has more scratches")
				else :
					print(Fore.MAGENTA+"2nd Glass has a greenish tint")
				# print("You are promoted to next level :)")
				# provide hints here
				superpower = superpower-1
		elif steppingGlass[level][userInput-1]==1:
			print(Fore.GREEN+"You picked correct step. Stepping glass stone level : "+str(level+1)+" cleared")
			level = level + 1
		else:
			print(Fore.RED+"Oops you stepped on glass. Eliminated")
			gameOver(user)


	user.currentStage = 2
	user.saveGame()
	print()
	print(Fore.GREEN+"Congratulations!!!!!  Stepping glass stone cleared.")
	print(Fore.YELLOW+"Bot : "+getBot(user)+" eliminated!")
	print()
	print()
	choice = input("Continue playing? (yes/no)")
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()
