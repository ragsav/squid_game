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
		print(Fore.CYAN+"Maze level : "+str(level+1)+"----------- superpower left : "+str(Superpower(user.currentSuperpower).name)+"->"+str(superpower))
		userInput = input("Enter 1,2,3 for doors. Enter 'power' for superpower and 'q' to quit :")
		door=-1
		if userInput.strip().lower()=="q" or userInput.strip().lower()=="quit":
			door=5
		elif userInput.strip().lower()=="power":
			door=4
		elif userInput.strip().lower()=="1":
			door=1
		elif userInput.strip().lower()=="2":
			door=2
		elif userInput.strip().lower()=="3":
			door=3




		if door==-1:
			print(Fore.RED+"Invalid input")
		if door==5:
			gameOver(user)
		elif door==4:
			if superpower==0:
				print(Fore.RED+str(Superpower(user.currentSuperpower).name)+" has no use in this level.")
			else:
				print(Fore.YELLOW+"You used a superpower")
				print(Fore.GREEN+"You are promoted to next level !!")
				superpower = superpower-1
				level=level+1
		elif maze1[level][door-1]==1:
			print(Fore.GREEN+"You picked correct door. Maze level : "+str(level+1)+" cleared")
			level = level + 1
		elif maze1[level][door-1]==0:
			print(Fore.YELLOW+"The door you picked is a blocked door and can be passed")
			print(Fore.YELLOW+"only by using superpower. Else you can retry selecting doors")
		elif maze1[level][door-1]==-1:
			print(Fore.RED+"Oops you picked a danger door. Eliminated")
			gameOver(user)


	user.currentStage = 1
	user.saveGame()
	print()
	print(Fore.GREEN+"Congratulations!!!!!  Maze escape cleared.")
	print(Fore.YELLOW+"Bot : "+getBot(user)+" eliminated!")
	print()
	print()
	# choice = input("Continue playing? (yes/no)")
	# if choice.lower().strip()=="no"or choice.lower().strip()=="n":
	# 	gameOver()
