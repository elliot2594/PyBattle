class Weapon:
	def __init__(self, name: str, weapon_type: str, damage: int, value: int):
		self.name = name
		self.type = weapon_type
		self.damage = damage
		self.value = value


sword = Weapon(name="Sword", weapon_type="sharp", damage=5, value=10)
axe = Weapon(name="Axe", weapon_type="Two Handed", damage=10, value=10)
spear = Weapon(name="Spear", weapon_type="Sharp", damage=3, value=10)


	

