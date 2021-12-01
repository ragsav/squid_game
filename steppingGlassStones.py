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
		print(Fore.CYAN+"Stepping glass stone level : "+str(level+1)+"----------- superpower left : "+str(Superpower(user.currentSuperpower).name)+"->"+str(Superpower(user.currentSuperpower).value))
		userInput = input("Enter 'left' or 'right' to step on one of the steps. Enter 'power' for super power and 'q' to quit :")
		

		#initialize which step user has taken
		step = -1
		if userInput.strip().lower()=="right":
			step=1
		elif userInput.strip().lower()=="left":
			step=0
		elif userInput


		# now check for all the possible conditions
		if userInput=="q":
			gameOver()
		elif userInput=='power':
			if superpower==0:
				print(Fore.RED+str(Superpower(user.currentSuperpower))+" has no use in this level.")
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
		elif step>=0 and steppingGlass[level][step]==1:
			print(Fore.GREEN+"You picked correct step. Stepping glass stone level : "+str(level+1)+" cleared")
			level = level + 1
		elif step>=0 and steppingGlass[level][step]==0:
			print(Fore.RED+"Oops you stepped on glass. Eliminated")
			gameOver(user)
		else :
			print(Fore.RED+"Invalid input")


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
