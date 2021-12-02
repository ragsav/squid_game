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
		print(Fore.CYAN+"Stepping glass stone level : "+str(level+1)+"----------- superpower left : "+str(Superpower(user.currentSuperpower).name)+"->"+str(superpower))
		userInput = input("Enter left or right for stepping on glass of your choice. Enter 'power' for superpower and 'q' to quit :")
		step=-1
		if userInput.strip().lower()=="q" or userInput.strip().lower()=="quit":
			step=5
		elif userInput.strip().lower()=="power":
			step=4
		elif userInput.strip().lower()=="left" or userInput.strip().lower()=="l":
			step=1
		elif userInput.strip().lower()=="right" or userInput.strip().lower()=="r":
			step=2
		



		if step==-1:
			print(Fore.RED+"Invalid input")
		elif step==5:
			gameOver()
		elif step==4:
			if superpower==0:
				print(Fore.RED+str(Superpower(user.currentSuperpower).name)+" has no use in this level.")
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
		elif steppingGlass[level][step-1]==1:
			print(Fore.GREEN+"You picked correct step. Stepping glass stone level : "+str(level+1)+" cleared")
			level = level + 1
		elif steppingGlass[level][step-1]==0:
			print(Fore.RED+"Oops you stepped on glass. Eliminated")
			gameOver(user)


	user.currentStage = 2
	user.saveGame()
	print()
	print(Fore.GREEN+"Congratulations!!!!!  Stepping glass stone cleared.")
	print(Fore.YELLOW+"Bot : "+getBot(user)+" eliminated!")
	print()
	print()
	# choice = input("Continue playing? (yes/no)")
	# if choice.lower().strip()=="no"or choice.lower().strip()=="n":
	# 	gameOver()
