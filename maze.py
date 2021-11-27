from util import *
from user import *
from constants import *

def mazeEscape(user):
	print()
	print()
	print(Fore.GREEN + '********************* MAZE ESCAPE ********************')
	print(Fore.GREEN + '******************************************************')
	print()
	superpower = 0
	if user.currentSuperpower==Superpower.SuperStrength.value:
		superpower = 3
		print(Fore.YELLOW+"You have 3 SuperStrength !!. Use all of them")
		print()
	level = 0

	while level < mazeLength:
		print()
		print()
		print(Fore.CYAN+"Maze level : "+str(level+1)+"----------- superpower left : "+str(superpower))
		userInput = int(input("Enter 1,2,3 for doors. 4 for superpower and 5 to quit :"))
		if userInput==5:
			gameOver(user)
		elif userInput==4:
			if superpower==0:
				print(Fore.RED+"You dont have any superpower left. Please pick any door")
			else:
				print(Fore.YELLOW+"You used a superpower")
				print(Fore.GREEN+"You are promoted to next level !!")
				superpower = superpower-1
				level=level+1
		elif maze1[level][userInput-1]==1:
			print(Fore.GREEN+"You picked correct door. Maze level : "+str(level+1)+" cleared")
			level = level + 1
		elif maze1[level][userInput-1]==0:
			print(Fore.YELLOW+"The door you picked is a blocked door and can be passed")
			print(Fore.YELLOW+"only by using superpower. Else you can retry selecting doors")
		else:
			print(Fore.RED+"Oops you picked a danger door. Eliminated")
			gameOver(user)
	user.currentStage = 1
	user.saveGame()
	print()
	print(Fore.GREEN+"Congratulations!!!!!  Maze escape cleared.")
	print(Fore.YELLOW+"Bot : "+getBot(user)+" eliminated!")
	print()
	print()
	choice = input("Continue playing? (yes/no)")
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()
