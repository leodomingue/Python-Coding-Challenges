from model.parser_grid import build_grid_from_raw
from model.DFS import DFS
import unittest 

class TestStar(unittest.TestCase):

    def setUp(self):
        
        self.grid_1x1 = self._create_grid([
            ["W", "W", "W"],
            ["W", "P", "W"],
            ["W", "W", "W"]
        ])
        
        self.grid_2x2_case1 = self._create_grid([
            ["W", "W", "W", "W"],
            ["W", "P", "P", "W"],
            ["W", "W", "P", "W"],
            ["W", "W", "W", "W"]
        ])
        
        self.grid_2x2_case2 = self._create_grid([
            ["W", "W", "W", "W"],
            ["W", "P", "W", "W"],
            ["W", "P", "P", "W"],
            ["W", "W", "W", "W"]
        ])

    def _create_grid(self, raw_layout):
        return build_grid_from_raw(raw_layout)
    

    #TESTS
    def test_01_DFS_1x1_grid_visit_unique_cell_from_1_1(self):

        grid = self.grid_1x1

        initial_position = (1,1)
        final_position = (1,1)
        dfs = DFS(initial_position, final_position)


        dfs.make_path_in_grid_1(grid)
        path = dfs.return_visited_cells()

        grid.set_marked(path)

        current_cell = grid.get_cell(initial_position[0],initial_position[1])
        self.assertTrue(current_cell.was_visited())

    
    def test_02_DFS_2x2_grid_generate_path(self):

        grid = self.grid_2x2_case1


        initial_position = (1,1)
        final_position = (2,2)
        dfs = DFS(initial_position, final_position)
        expected_path = [(1,1),(1,2),(2,2)]
        not_expected = [(2,1)]

        dfs.make_path_in_grid_1(grid)
        path_created = dfs.return_visited_cells()

        grid.set_marked(path_created)

        for cell in expected_path:
            current_cell = grid.get_cell(cell[0],cell[1])
            self.assertTrue(current_cell.was_visited())
        
        for cell in not_expected:
            current_cell = grid.get_cell(cell[0],cell[1])
            self.assertFalse(current_cell.is_path())
        

    def test_03_DFS_2x2_grid_generate_path(self):

        grid = self.grid_2x2_case2


        initial_position = (1,1)
        final_position = (2,2)
        dfs = DFS(initial_position, final_position)
        expected_path = [(1,1),(2,1),(2,2)]
        not_expected = [(1,2)]

        dfs.make_path_in_grid_1(grid)
        path_created = dfs.return_visited_cells()

        grid.set_marked(path_created)

        for cell in expected_path:
            current_cell = grid.get_cell(cell[0],cell[1])
            self.assertTrue(current_cell.was_visited())
        
        for cell in not_expected:
            current_cell = grid.get_cell(cell[0],cell[1])
            self.assertFalse(current_cell.is_path())

    
    

if __name__ == '__main__':
    unittest.main()