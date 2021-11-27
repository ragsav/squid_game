from tinydb import TinyDB, Query
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime
import json
from enum import Enum

import random
from random import randrange
from playsound import playsound
import winsound
db = TinyDB('db.json')
init(autoreset=True)
USER = Query()
from maze import * 
from rockPaperScissors import * 
from steppingGlassStones import *
from rockPaperScissors import *
from util import *
from user import *
from constants import *
# username = "ragsav"





		
def login():
	print()
	#get username
	username=repeatInput("Enter your username :","Username cannot be empty!")

	#check if username is present in database
	db_user = db.search(USER.username==username)
	if(db_user):
		currentUser = User.DocumentToObject(db_user[0])
		print(Fore.GREEN+"Character retrieved and all set")
		print()
		print(Fore.CYAN + '****** Welcome '+str(currentUser.username)+' ******')
		return currentUser
	else:
		print(Fore.RED+"User not found")
		choice = input("Create new user with provided username ? (yes/no)")
		if choice.lower().strip()=="no"or choice.lower().strip()=="n":
			gameOver()
		else:
			currentUser = User.create(username)
			print(Fore.CYAN + '****** Welcome '+str(currentUser.username)+' ******')
			return currentUser
	
	
def entryScreen(user):
	print(Fore.YELLOW + "(1) New game")
	if user.currentStage>0:
		print(Fore.YELLOW + "(2) Continue game")
		print(Fore.RED + "(3) Exit game")
	else :
		print(Fore.RED + "(2) Exit game")
	option = int(repeatInputWithRangeCheck("Enter corrensponding option :","Please enter valid input!","Input out of range!",1,3))
	if(user.currentStage>0 and option==3) or (user.currentStage==0 and option==2):
		gameOver()

	return option

def newGameScreen(user):
	print()
	print()
	print(Fore.GREEN + '***************** CHARACTER SELECTION ****************')
	print()
	characterName = repeatInput("Enter your character name :","Character name cannot be empty!")
	print()
	
	print(Fore.GREEN +"Your character can have one out of the following superpowers :")
	print()
	for index,superpower in enumerate(Superpower):
		print(Fore.YELLOW +"("+str(index+1)+")"+" . "+superpower.name)

	superpower = int(repeatInputWithRangeCheck("Enter corrensponding superpower number :","Superpower cannot be empty","Superpower out of range!",1,3))
	db.update({'currentStage':0,'currentCharacterName':"",'currentSuperpower':0,'bots':['bot1','bot2','bot3']}, USER.username == user.username)
	user.currentSuperpower = superpower
	user.currentCharacterName = characterName
	print()
	print(Fore.CYAN +"Character created : "+characterName+ " ("+Superpower(superpower).name+")")
	print()



def startGames(cont):
	print()
	if cont:
		print(Fore.GREEN+"Character retrieved and all set")
	else:
		print(Fore.GREEN+"Character created and all set")
	choice = input("Start games? (yes/no)")
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()










		



def intro():
	# soundIntroStart()
	print()
	print()
	print(Fore.CYAN + '***************** ANOTHER SQUID GAME *****************')
	print(Fore.CYAN + '*                                                    *')
	print(Fore.CYAN + '*   Welcome to another squid game, a text based      *')
	print(Fore.CYAN + '*   role-playing adventure game based on Netflix     *')
	print(Fore.CYAN + '*   show "SQUID GAME"                                *')
	print(Fore.CYAN + '*                                                    *')
	print(Fore.CYAN + '******************************************************')
	print()
	print(Fore.GREEN + '********************* DESCRIPTION ********************')
	print()
	print(Fore.CYAN + 'Another quid game has three games in total that are :')
	print()
	print(Fore.GREEN + '1. Maze Escape : ' + Fore.YELLOW + 'Maze escape contains 5 rounds')
	print(Fore.YELLOW + '	of selection between three doors. One of the ')
	print(Fore.YELLOW + '	doors is blocked, one of them is danger door and ')
	print(Fore.YELLOW + '	the other one is door to next choice')
	print()
	print(Fore.GREEN + '2. Stepping Glass Stones : '+ Fore.YELLOW + 'Stepping Glass stone is')
	print(Fore.YELLOW + '	similar to the game we saw in orignal squid game.')
	print(Fore.YELLOW + '	You have to choose which to step on using your ')
	print(Fore.YELLOW + '	super power or intuition. One of them is glass')
	print(Fore.YELLOW + '	and other is acrylic (which is hardened)')

	print()
	print(Fore.GREEN + '3. Rock Paper Scissors :' + Fore.YELLOW + 'Rock paper is a simple')
	print(Fore.YELLOW + '	game where you have to choose either rock, paper')
	print(Fore.YELLOW + "	or scissors and based on your and opponent's choice ")
	print(Fore.YELLOW + "	winner will be decided. This also has 5 rounds")
	print()
	print()
	print(Fore.GREEN + '*********************** RULES ************************')
	print()
	print(Fore.YELLOW + '1.	Enter your username to start the game.')
	print()
	print(Fore.YELLOW + '2.	Select whether to start new game or continue saved')
	print(Fore.YELLOW + '	game, if you have')
	print()
	print(Fore.YELLOW + '3.	If you have selected new game then you have to enter')
	print(Fore.YELLOW + '	a character name and select one of the three super ')
	print(Fore.YELLOW + '	powers for it.')
	print(Fore.MAGENTA + '	(Remember every superpower has only one level to use)')
	print()
	print(Fore.YELLOW + '4.	If you have selected continue game, you can start')
	print(Fore.YELLOW + '	playing from the game which you left.')
	print()
	print()
	choice = input('Are you ready to start adventure? (yes/no)')
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()



	

def newGame(user):
	# soundIntroStop()
	# soundGameStart()
	newGameScreen(user)
	startGames(False)
	mazeEscape(user)
	steppingGlassStone(user)
	rockPaperScissor(user)


def continueGame(user):
	if user.currentStage==0:
		print(Fore.RED+"Please start a new game!")
	elif user.currentStage==1:
		startGames(True)
		steppingGlassStone(user)
		rockPaperScissor(user)
	elif user.currentStage==2:
		startGames(True)
		rockPaperScissor(user)

	





def main():
    intro()
    currentUser = login()
    entryScreenOption = entryScreen(currentUser)
    if entryScreenOption==1:
    	newGame(currentUser)
    else :
    	continueGame(currentUser)

    
    
def main2():
	# winsound.PlaySound("C:/Users/Raghav/Desktop/squid game python/arcade_retro.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
	# await play_file_async(DEFAULT_SONG, block=False)
	# winsound.PlaySound(None, winsound.SND_ASYNC)
	playsound('C:/Users/Raghav/Desktop/squid game python/arcade_retro.wav',False)
	intro()




if __name__ == "__main__":
    main()
