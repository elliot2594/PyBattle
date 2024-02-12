import pytest

from character import Orc
from weapons import sword, axe, spear

orcTestName = "Test_orc"

class TestOrcObject:

	@pytest.fixture
	def orcObject(self):
		orc_obj = Orc(orcTestName)
		return orc_obj

	def test_orcClass(self, orcObject):
		assert orcObject.health == 100, "Should be 100"
		assert orcObject.equip(sword) == None
		
	def testHealth(self, orcObject):
		assert orcObject.health == 100, "Should be 100"

	def testName(self, orcObject):
		assert orcObject.name == orcTestName, f"Name should be equal to {orcTestName}"

	def testSwordAttack(self, orcObject):
		assert orcObject.equip(sword) == None
		for i in range(0,100):
			assert (1 <= int(orcObject.attack()) <= orcObject.weapon.damage), f"Damange should be between 1 and {orcObject.weapon.damage}"

	def testSpearAttack(self, orcObject):
		assert orcObject.equip(spear) == None
		for i in range(0,100):
			assert (1 <= int(orcObject.attack()) <= orcObject.weapon.damage), f"Damange should be between 1 and {orcObject.weapon.damage}"

	def testAxeAttack(self, orcObject):
		assert orcObject.equip(axe) == None
		for i in range(0,100):
			assert (1 <= int(orcObject.attack()) <= orcObject.weapon.damage), f"Damange should be between 1 and {orcObject.weapon.damage}"