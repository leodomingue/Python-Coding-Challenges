import pygame
from model.grid import Grid
from model.maze_generator import RandomMazeGenerator  
from .gridDrawer import GridDrawer
from .UI.UI_Controller import UIController
from .pathDrawer import PathDrawer

def return_pass():
    print("pass")

class MazeGeneratorApp:
    def __init__(self, width, height, CELL_SIZE):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.MAZE_HEIGHT_RATIO = 0.9
        self.maze_height = int(height*self.MAZE_HEIGHT_RATIO)
        self.ui_height = height - self.maze_height 
        

        self.CELL_SIZE = CELL_SIZE
        self.drawer = GridDrawer(CELL_SIZE)
        self.grid_rows = self.maze_height// CELL_SIZE
        self.grid_cols = width // CELL_SIZE
        self.grid = Grid(self.grid_rows-2, self.grid_cols-2)


        self.generator = RandomMazeGenerator()
        self.initial_pos = (1, 1)
        self.final_pos = (self.grid_rows-2, self.grid_cols-2)
        self.generator.generate(self.grid, self.initial_pos, self.final_pos)

        self.pathDrawer = None

        self.ui = UIController(
            top_y=self.maze_height,
            width=width,
            height=self.ui_height,
            on_generate_maze_function = lambda: self.generate_maze(), 
            on_make_dfs_function = lambda: self.draw_path(), 
            on_change_color_function = return_pass
        )

    def generate_maze(self):
        self.pathDrawer = None
        self.generator.generate(self.grid, self.initial_pos, self.final_pos)

    def draw_path(self):
        if self.pathDrawer is not None:
            self.pathDrawer.undraw_path(self.display)
        self.pathDrawer = PathDrawer(self.CELL_SIZE, self.grid, self.initial_pos, self.final_pos)
        self.pathDrawer.draw_path(self.display)

    def run(self):
        while self.running:
            self.handle_events()
            self.display.fill((0, 0, 0)) 
            self.drawer.draw_grid(self.grid, self.display)
            self.ui.draw(self.display)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            self.ui.handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == "__main__":
    app = MazeGeneratorApp(1200, 800, 10)
    app.run()