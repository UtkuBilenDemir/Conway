import numpy as np

def alive_neighbors(loc, grid, grid_size):
    x = loc[0]
    y = loc[1]
    return np.sum(grid[max(x-1, 0):min(x+2, grid_size), max(y-1, 0):min(y+2, grid_size)]) - grid[x, y]