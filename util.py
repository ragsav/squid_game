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
from constants import *
import random
db = TinyDB('db.json')
init()
USER = Query()


# def soundLevelSuccess():
# def soundGameFail():
# def soundGameSuccess():
# def soundWinner():
def soundGameBGStart():
	winsound.PlaySound("arcade_retro.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
def soundGameBGStop():
	winsound.PlaySound(None, winsound.SND_ASYNC)
def soundIntroStart():
	winsound.PlaySound("entry.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )
def soundIntroStop():
	winsound.PlaySound(None, winsound.SND_ASYNC)

def getBot(user):
	totalBots = len(user.bots)
	print(totalBots)
	deletedBotIndex = random.randint(0,totalBots-1)
	deletedBot = user.bots[deletedBotIndex]
	del user.bots[deletedBotIndex]
	return deletedBot


def gameOver(*args):
	if args and args[0] !=None:
		db.update({'currentStage':0,'currentSuperpower':0,'currentCharacterName':""},USER.username==args[0].username)
	print()
	print()
	print(Fore.YELLOW + '******* Thanks for playing! Please visit again *******')

	exit()

def congratulations():
	print()
	print(Fore.CYAN + '****************** CONGRATULATIONS *******************')
	print(Fore.CYAN + '*                                                    *')
	print(Fore.CYAN + '*               Winner!!! You made it.               *')
	print(Fore.CYAN + '*                                                    *')
	print(Fore.CYAN + '******************************************************')


def repeatInput(msg,errorMsg):
	choice="yes"
	userInput=""
	while choice.lower().strip()=="yes"or choice.lower().strip()=="y":
		userInput = input(msg)
		if userInput.strip()=="":
			print(Fore.RED +errorMsg)
			print()
			choice = input("Continue playing ? (yes/no)")
		else:
			break
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()
	return userInput


def repeatInputWithRangeCheck(msg,errorMsg1,errorMsg2,r1,r2):
	choice="yes"
	userInput=""
	while choice.lower().strip()=="yes"or choice.lower().strip()=="y":
		userInput = input(msg)
		if userInput.strip()=="":
			print(Fore.RED +errorMsg)
			choice = input("Continue playing ? (yes/no)")
		elif int(userInput)<r1 or int(userInput)>r2:
			print(Fore.RED +errorMsg2)
			choice = input("Continue playing ? (yes/no)")
		else:
			break
	if choice.lower().strip()=="no"or choice.lower().strip()=="n":
		gameOver()
	return userInput
