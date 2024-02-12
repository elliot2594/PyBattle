import pytest

from character import Dwarf, Human, Orc
from weapons import sword

humanTestName = "Test_Human"
orcTestName = "Test_Orc"

class TestCharacterClass:

	@pytest.fixture
	def humanObject(self):
		human_obj = Human(humanTestName)
		return human_obj

	def test_HumanClass(self, humanObject):
		assert humanObject.health == 100, "Should be 100"
		assert humanObject.equip(sword) == None
		

	def testHealth(self, humanObject):
		assert humanObject.health == 100, "Should be 100"

	def testName(self, humanObject):
		assert humanObject.name == humanTestName, f"Name should be equal to {humanTestName}"

	def testSwordAttack(self, humanObject):
		assert humanObject.equip(sword) == None
		for i in range(0,100):
			assert (1 <= int(humanObject.attack()) <= humanObject.weapon.damage), f"Damange should be between 1 and {humanObject.weapon.damage}"



	def testOrcClass(self):
		orc_obj = Orc(orcTestName)
		assert orc_obj.health == 100, "Should be 100"
		assert orc_obj.name == orcTestName, f"Name should be equal to {orcTestName}"