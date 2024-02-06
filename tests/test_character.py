import pytest

from character import Dwarf, Human, Orc
from weapons import sword

humanTestName = "Test_Human"
orcTestName = "Test_Orc"

class TestClass:

	def test_HumanClass(self):
		human_obj = Human(humanTestName)
		assert human_obj.health == 100, "Should be 100"
		assert human_obj.name == humanTestName, f"Name should be equal to {humanTestName}"
		assert human_obj.equip(sword) == None
		for i in range(0,100):
			assert (1 <= int(human_obj.attack()) <= human_obj.weapon.damage), f"Damange should be between 1 and {human_obj.weapon.damage}"

	def testOrcClass(self):
		orc_obj = Orc(orcTestName)
		assert orc_obj.health == 100, "Should be 100"
		assert orc_obj.name == orcTestName, f"Name should be equal to {orcTestName}"