from tinydb import TinyDB, Query
from datetime import datetime
import json

from util import *
from constants import *


db = TinyDB('db.json')
USER = Query()

class User(object):

	def __init__(self,username,createdAt,updatedAt,lastPlayedAt,currentStage,currentCharacterName,currentSuperpower,bots):
		super(User, self).__init__()
		self.username = username
		self.createdAt = createdAt
		self.updatedAt = updatedAt
		self.lastPlayedAt = lastPlayedAt
		self.currentStage = currentStage
		self.currentCharacterName = currentCharacterName
		self.currentSuperpower = currentSuperpower
		self.bots = bots


	@classmethod
	def create(self,username):
		now = datetime.now()
		createdAt = now.strftime("%H:%M:%S")
		#adding user to db
		db.insert({'username':username,'createdAt':createdAt,'updatedAt':createdAt,'lastPlayedAt':-1,'currentStage':0,'currentCharacterName':"",'currentSuperpower':0,'bots':["bot1","bot2","bot3"]})
		print()
		print(Fore.GREEN+"New user with username: "+ username +" created at: "+ createdAt);
		print()

		#returning user object
		return self(username,createdAt,createdAt,-1,0,"",0,["bot1","bot2","bot3"])

	def saveGame(self):
		now = datetime.now()
		lastPlayedAt = now.strftime("%H:%M:%S")
		db.update({'currentStage':self.currentStage,'currentSuperpower':self.currentSuperpower,'currentCharacterName':self.currentCharacterName,'lastPlayedAt':lastPlayedAt,'bots':self.bots},USER.username==self.username)


	def toJSON(self):
		return {
			'username':self.username,'createdAt':self.createdAt,'updatedAt':self.updatedAt,'lastPlayedAt':self.lastPlayedAt,'currentStage':self.currentStage
		}
	@classmethod
	def DocumentToObject(self,db_user):
		return self(db_user['username'],db_user['createdAt'],db_user['updatedAt'],db_user['lastPlayedAt'],db_user['currentStage'],db_user['currentCharacterName'],db_user['currentSuperpower'],db_user['bots'])
		
	
		
