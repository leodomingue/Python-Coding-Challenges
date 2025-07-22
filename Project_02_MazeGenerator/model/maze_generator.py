from model.parser_grid import build_grid_from_raw
from model.DFS import DFS
from model.grid import *

class BasicBorderGridGenerator:
    def generate(self, grid):
        rows = grid.number_of_rows()
        cols = grid.number_of_columns()

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    grid.set_cell(row, col, WallCell(row, col))
                else:
                    grid.set_cell(row, col, PathCell(row, col))


class RandomMazeGenerator:

    def generate(self, grid, initial_position, final_position):


        layout_generator = BasicBorderGridGenerator()
        layout_generator.generate(grid)
        
        grid.set_cell(initial_position[0], initial_position[1], PathCell(initial_position[0], initial_position[1]))
        grid.set_cell(final_position[0], final_position[1], PathCell(final_position[0], final_position[1]))

        dfs = DFS(initial_position, final_position)


        dfs.make_path_in_grid_1(grid)
        path = dfs.return_visited_cells()

        grid.set_all_wall()
        grid.make_set_path(path)
        grid.add_random_paths()

        grid.set_cell(initial_position[0], initial_position[1], PathCell(initial_position[0], initial_position[1]))
        grid.set_cell(final_position[0], final_position[1], PathCell(final_position[0], final_position[1]))


