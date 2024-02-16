import os
import random

from character import Dwarf, Human, Orc
from weapons import sword, axe, spear
numberOfPlayers = 0
characterList = []
raceList = {1: "Human", 2: "Orc", 3: "Dwarf"}

clear = lambda: os.system('clear')


def gameLoop():
	clear()
	print("Welcome to PyBattle\n")
	print("Create character\n")
	print("Enter player name")
	userInputName = input()
	print("Pick Race: \n")
	print("1. Human\n2. Orc\n3. Dwarf\n")
	userInputRace = input().strip().lower()
	pickRace(userInputName, userInputRace)
	enemyCharacter()
	startGame()


def validatePlayers():
	while True:
		userInput = input()
		if userInput.strip().isdigit() != True:
			print("Please enter a number")
		elif int(userInput) <= 0:
			print("Please enter a number larger than 0")
		else:
			global numberOfPlayers
			numberOfPlayers = int(userInput)
			break


def pickRace(characterName, race):
	while True:
		if (race == "human" or race == "1"):
			characterList.append(Human(characterName))
			break
		elif(race == "orc" or race == "2"):
			characterList.append(Orc(characterName))
			break
		elif(race == "dwarf" or race == "3"):
			characterList.append(Dwarf(characterName))
			break
		else:
			print("Race must be Human, Orc or Dwarf")

def enemyCharacter():
	playerCharacter = characterList[0].race
	characterName = "EnemyOne"
	race = raceList[random.randint(1, 3)].lower()
	pickRace(characterName, race)



			
def startGame():
	clear()
	characterList[0].health_bar.draw()
	print("\n\n")
	characterList[1].health_bar.draw()







if __name__ == "__main__":
	gameLoop()


