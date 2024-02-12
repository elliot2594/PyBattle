import random

class Character:
	def __init__(self, name):
		self.name = name
		self.health = 100

	def getHealth(self):
		return self.health

	def equip(self, weapon):
		self.weapon = weapon
		print(f"{self.name} equipped {self.weapon.name}")

	def attack(self):
		return float(self.weapon.damage) * (random.randint(40, 100) / 100)


class Human(Character):
	def __init__(self, name: str):
		Character.__init__(self, name)
		self.name = name
		self.strength = 80
		self.defence = 50
		self.agility = 100
		self.race = "Human"

class Orc(Character):
	def __init__(self, name:str):
		Character.__init__(self, name)
		self.name = name
		self.strength = 100
		self.defence = 80
		self.agility = 40
		self.race = "Orc"

class Dwarf(Character):
	def __init__(self, name:str):
		Character.__init__(self, name)
		self.name = name
		self.strength = 90
		self.defence = 100
		self.agility = 65
		self.race = "Dwarf"









