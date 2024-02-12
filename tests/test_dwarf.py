import pytest

from character import Dwarf
from weapons import sword, axe, spear

dwarfTestName = "Test_dwarf"

class TestDwarfObject:

	@pytest.fixture
	def dwarfObject(self):
		dwarf_obj = Dwarf(dwarfTestName)
		return dwarf_obj

	def test_dwarfClass(self, dwarfObject):
		assert dwarfObject.health == 100, "Should be 100"
		assert dwarfObject.equip(sword) == None
		
	def testHealth(self, dwarfObject):
		assert dwarfObject.health == 100, "Should be 100"

	def testName(self, dwarfObject):
		assert dwarfObject.name == dwarfTestName, f"Name should be equal to {dwarfTestName}"

	def testSwordAttack(self, dwarfObject):
		assert dwarfObject.equip(sword) == None
		for i in range(0,100):
			assert (1 <= int(dwarfObject.attack()) <= dwarfObject.weapon.damage), f"Damange should be between 1 and {dwarfObject.weapon.damage}"

	def testSpearAttack(self, dwarfObject):
		assert dwarfObject.equip(spear) == None
		for i in range(0,100):
			assert (1 <= int(dwarfObject.attack()) <= dwarfObject.weapon.damage), f"Damange should be between 1 and {dwarfObject.weapon.damage}"

	def testAxeAttack(self, dwarfObject):
		assert dwarfObject.equip(axe) == None
		for i in range(0,100):
			assert (1 <= int(dwarfObject.attack()) <= dwarfObject.weapon.damage), f"Damange should be between 1 and {dwarfObject.weapon.damage}"