import pygame
from model.grid import Grid
from model.maze_generator import RandomMazeGenerator  

CELL_SIZE = 5

class MazeGeneratorApp:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.grid_rows = height // CELL_SIZE
        self.grid_cols = width // CELL_SIZE
        self.grid = Grid(self.grid_rows-2, self.grid_cols-2)

        generator = RandomMazeGenerator()
        initial_pos = (1, 1)
        final_pos = (self.grid_rows-2, self.grid_cols-2)
        generator.generate(self.grid, initial_pos, final_pos)


    def draw_grid(self, grid):
        for row in range(grid.number_of_rows()):
            for col in range(grid.number_of_columns()):
                cell = grid.get_cell(row, col)

                x = col * CELL_SIZE
                y = row * CELL_SIZE

                if cell.is_wall():
                    color = (0, 0, 0)        
                elif cell.is_path():
                    color = (255, 255, 255)  
                else:
                    color = (150, 150, 150)  
                pygame.draw.rect(self.display, color, (x, y, CELL_SIZE, CELL_SIZE))

    def run(self):
        while self.running:
            self.handle_events()

            self.display.fill((0, 0, 0)) 
            self.draw_grid(self.grid)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == "__main__":
    app = MazeGeneratorApp(1200, 800)
    app.run()