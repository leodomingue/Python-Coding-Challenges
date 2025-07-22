from model.cell import PathCell, WallCell
import random

class Grid:

    def __init__(self, rows, columns):
        self.columns = columns + 2
        self.rows = rows + 2

        self.grid = [[None for _ in range(self.columns)] for _ in range(self.rows)]


    def number_of_columns(self):
        return self.columns
    
    def number_of_rows(self):
        return self.rows
    
    
    def set_cell(self, row, col, cell):
        self.grid[row][col] = cell

    def get_cell(self, row, col):
        return self.grid[row][col]
    
    def set_marked(self, set):
        for position_cell in set:
            cell = self.get_cell(position_cell[0], position_cell[1])
            cell.is_visit()

    def make_set_wall(self, set):
        for position_cell in set:
            self.grid[position_cell[0]][position_cell[1]] = WallCell(position_cell[0],position_cell[1])

    def make_set_path(self, set):
        for position_cell in set:
            self.set_cell(position_cell[0], position_cell[1], PathCell(position_cell[0],position_cell[1]))

    def set_all_wall(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.set_cell(row, col, WallCell(row,col))
    
    def print(self):
        for row in range(self.number_of_rows()):
            for col in range(self.number_of_columns()):
                cell = self.get_cell(row, col)
                print('W' if isinstance(cell, WallCell) else 'P', end=' ')
            print()

    def add_random_paths(self, probability=0.5):
    
        for row in range(1, self.rows - 1):  
            for col in range(1, self.columns - 1):
                if random.random() < probability:  
                    current_cell = self.get_cell(row, col)
                    if isinstance(current_cell, WallCell): 
                        self.set_cell(row, col, PathCell(row, col))

    def is_inside(self, row, col):
        return 0 <= row < self.number_of_rows() and 0 <= col < self.number_of_columns()
        



