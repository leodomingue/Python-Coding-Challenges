from model.grid import Grid
from model.maze_generator import RandomMazeGenerator  


rows, cols = 10, 10
initial_pos = (1, 1)
final_pos = (10, 10)


grid = Grid(rows, cols)
maze_generator = RandomMazeGenerator()

maze_generator.generate(grid, initial_pos, final_pos)

grid.print()