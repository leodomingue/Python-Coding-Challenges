import unittest 
from model.cell import PathCell, WallCell, PlayerCell, Cell


class TestStar(unittest.TestCase):
    
    def test_01_pathCell_is_passable(self):
        pathcell = PathCell(1,1)
        self.assertTrue(pathcell.is_passable())

    def test_02_wallCell_is_not_passable(self):
        wallcell = WallCell(1,1)
        self.assertFalse(wallcell.is_passable())

    def test_03_PlayerCell_initial_position(self):
        playercell = PlayerCell(1,1)
        self.assertTrue(playercell.is_position(1,1))

    def test_04_PlayerCell_movement_up(self):
        playercell = PlayerCell(1,1)
        playercell.movement_up()
        self.assertTrue(playercell.is_position(1,0))

    def test_05_PlayerCell_movement_down(self):
        playercell = PlayerCell(1,1)
        playercell.movement_down()
        self.assertTrue(playercell.is_position(1,2))

    def test_06_PlayerCell_movement_right(self):
        playercell = PlayerCell(1,1)
        playercell.movement_right()
        self.assertTrue(playercell.is_position(2,1))

    def test_07_PlayerCell_movement_left(self):
        playercell = PlayerCell(1,1)
        playercell.movement_left()
        self.assertTrue(playercell.is_position(0,1))

    def test_08_Pathcell_change_visit_mode(self):
        pathcell = PathCell(1,1)
        self.assertFalse(pathcell.was_visited())
        pathcell.is_visit()
        self.assertTrue(pathcell.was_visited())



if __name__ == '__main__':
    unittest.main()