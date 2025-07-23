import pygame
from model.DFS import DFS
from model.grid import Grid
class PathDrawer:

    def __init__(self, cell_size, grid, initial_position, final_position):
        self.cell_size = cell_size
        self.DFS = DFS(initial_position, final_position)
        self.grid = grid
        self.path = None

    def draw_path(self, surface):
        self.DFS.make_path_in_grid_normal(self.grid)
        self.path = self.DFS.return_visited_cells()
        self.grid.set_marked(self.path)

        for cell_position in self.path:
            cell = self.grid.get_cell(cell_position[0], cell_position[1])
            color = cell.get_color()
            x = cell_position[0] * self.cell_size
            y = cell_position[1] * self.cell_size
            pygame.draw.rect(surface, color, (x, y, self.cell_size, self.cell_size))

    def undraw_path(self, surface):
        self.grid.set_unmarked(self.path)
        for cell_position in self.path:
            cell = self.grid.get_cell(cell_position[0], cell_position[1])
            color = cell.get_color()
            x = cell_position[0] * self.cell_size
            y = cell_position[1] * self.cell_size
            pygame.draw.rect(surface, color, (x, y, self.cell_size, self.cell_size))
