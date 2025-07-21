import unittest 
from model.grid import Grid 
from model.maze_generator import BasicBorderGridGenerator

class TestStar(unittest.TestCase):
    
    def test_01_grid_1x1_contain_3_rows_3_columns(self):
        column_count = 1
        rows_count = 1
        grid_1x1 = Grid(rows = rows_count, columns=column_count)

        self.assertEqual(grid_1x1.number_of_columns(), 3)
        self.assertEqual(grid_1x1.number_of_rows(), 3)


    def test_02_border_cells_are_walls(self):
        grid = Grid(rows=1, columns=1)
        generator = BasicBorderGridGenerator()
        generator.generate(grid)
        rows = grid.number_of_rows()
        cols = grid.number_of_columns()

        for col in range(cols):
            self.assertTrue(grid.get_cell(0,col).is_wall())  #First Col
            self.assertTrue(grid.get_cell(rows - 1,col).is_wall())  #Last Col

        for row in range(rows):
            self.assertTrue(grid.get_cell(row,0).is_wall())   #First Row
            self.assertTrue(grid.get_cell(row,cols - 1).is_wall())  #Last Row


if __name__ == '__main__':
    unittest.main()
