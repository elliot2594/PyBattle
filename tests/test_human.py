import pytest

from character import Human
from weapons import sword, axe, spear

humanTestName = "Test_Human"

class TestHumanObject:

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

	def testSpearAttack(self, humanObject):
		assert humanObject.equip(spear) == None
		for i in range(0,100):
			assert (1 <= int(humanObject.attack()) <= humanObject.weapon.damage), f"Damange should be between 1 and {humanObject.weapon.damage}"

	def testAxeAttack(self, humanObject):
		assert humanObject.equip(axe) == None
		for i in range(0,100):
			assert (1 <= int(humanObject.attack()) <= humanObject.weapon.damage), f"Damange should be between 1 and {humanObject.weapon.damage}"