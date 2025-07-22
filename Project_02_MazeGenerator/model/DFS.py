import random
from model.cell import *
from model.grid import *

class DFS:

    def __init__(self, position,final_position):
        self.initial_position = position
        self.visited = set()
        self.final_position = final_position
        self.found = False

    def make_path_in_grid_2(self, grid):
        self._dfs_2(grid, self.initial_position[0], self.initial_position[1])

    def make_path_in_grid_1(self, grid):
        self._dfs(grid, self.initial_position[0], self.initial_position[1])

    def _dfs(self, grid, row, col):
        if self.found:  
            return
        
        self.visited.add((row, col))

        if (row, col) == self.final_position:
            self.found = True
            return 

        for new_position_x, new_position_y in self._neighbors_1(grid, row, col):
            if (new_position_x,new_position_y) not in self.visited:
                self._dfs(grid,new_position_x, new_position_y)

    def _dfs_2(self, grid, row, col):
        if self.found:  
            return
        
        self.visited.add((row, col))

        if (row, col) == self.final_position:
            self.found = True
            return 

        for new_position_x, new_position_y in self._neighbors_2(grid, row, col):
            if (new_position_x,new_position_y) not in self.visited:
                self._dfs(grid,new_position_x, new_position_y)

        
    def _neighbors_1(self, grid, row, col):
        directions = random.sample([(1, 0), (0, 1), (-1,0)], k=3)
        result = []

        for direction_x, direction_y in directions:
            new_position_x, new_position_y = row + direction_x, col + direction_y
            new_cell = grid.get_cell(new_position_x, new_position_y)
            if new_cell.is_path():
                result.append((new_position_x, new_position_y))

        return result

    def _neighbors_2(self, grid, row, col):
        directions = random.sample([(-2, 0), (2, 0), (0, -2), (0, 2)], k=4)
        result = []

        for direction_x, direction_y in directions:
            new_position_x, new_position_y = row + direction_x, col + direction_y
            new_cell = grid.get_cell(new_position_x, new_position_y)
            if new_cell.is_path():
                result.append((new_position_x, new_position_y))

        return result
    

    def return_visited_cells(self):
        return self.visited

