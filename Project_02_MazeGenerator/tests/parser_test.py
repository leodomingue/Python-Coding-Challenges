from model.parser_grid import build_grid_from_raw
from model.grid import Grid
from model.cell import WallCell, PathCell

def test_01_create_a_grid_from_raw_format(self):
    raw = [
        ["W", "W", "W"],
        ["W", "P", "W"],
        ["W", "W", "W"]
    ]

    grid = build_grid_from_raw(raw)


    self.assertEqual(grid.number_of_columns(), 3)
    self.assertEqual(grid.number_of_rows(), 3)

    rows = grid.number_of_rows()
    cols = grid.number_of_columns()
    
    for col in range(cols):
        self.assertTrue(grid.get_cell(0,col).is_wall())  #First Col
        self.assertTrue(grid.get_cell(rows - 1,col).is_wall())  #Last Col

    for row in range(rows):
        self.assertTrue(grid.get_cell(row,0).is_wall())   #First Row
        self.assertTrue(grid.get_cell(row,cols - 1).is_wall())  #Last Row

