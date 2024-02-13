from character import Dwarf, Human, Orc
from weapons import sword, axe, spear
numberOfPlayers = 0
characterList = []

def gameLoop():
	print("Welcome to PyBattle\n")
	print("Please pick how many players")
	validatePlayers()
	for i in range(numberOfPlayers):
		print("Please enter player {} name".format(i+1))
		userInputName = input()
		pickRace(i, userInputName)
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

def pickRace(playerNumber, characterName):
	while True:
		print("Pick Race: \n")
		print("Human\nOrc\nDwarf\n")
		userInputRace = input().strip()
		if (userInputRace == "Human"):
			characterList.append(Human(characterName))
			break
		elif(userInputRace == "Orc"):
			characterList.append(Orc(characterName))
			break
		elif(userInputRace == "Dwarf"):
			characterList.append(Dwarf(characterName))
			break
		else:
			print("Race must be Human, Orc or Dwarf")

			
def startGame():
	for player in characterList:
		print(player.name + "\n")
		print(player.race + "\n")







if __name__ == "__main__":
	gameLoop()


