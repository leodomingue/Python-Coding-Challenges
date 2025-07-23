import pygame
class GridDrawer:

    def __init__(self, cell_size):
        self.cell_size = cell_size

    def draw_grid(self, grid, surface):
        for row in range(grid.number_of_rows()):
            for col in range(grid.number_of_columns()):
                cell = grid.get_cell(row, col)
                x = col * self.cell_size
                y = row * self.cell_size

                color = cell.get_color()

                pygame.draw.rect(surface, color, (x, y, self.cell_size, self.cell_size))


