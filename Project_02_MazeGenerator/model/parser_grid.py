from .grid import Grid
from .cell import WallCell, PathCell

def build_grid_from_raw(grid_raw):
    rows = len(grid_raw)
    cols = len(grid_raw[0])

    grid = Grid(rows=rows - 2, columns=cols - 2) 

    for row in range(rows):
        for col in range(cols):
            symbol = grid_raw[row][col]
            if symbol == "W":
                cell = WallCell(row, col)
            elif symbol == "P":
                cell = PathCell(row, col)
            else:
                raise ValueError(f"Invalid Symbol: {symbol}")
            grid.set_cell(row, col, cell)
    
    return grid