from render import Renderer
from grid import Grid, Cell
from utils import set_interval

FRAMERATE = 60 # fps


class Game:
    def __init__(self):
        self.grid = Grid(50, 40)
        self.alive_cells = []
        self.alive_cells_coords = []
        self.width = 0   # has to be set by the app
        self.height = 0  # has to be set by the app


    @set_interval(1 / FRAMERATE) # OPTIMIZE: multiple threads
    def update(self):
        self.alive_cells = [cell for cell in self.grid.cells if cell.is_alive]
        self.dead_cells = [cell for cell in self.grid.cells if not cell.is_alive] # OPTIMIZE: remove ?
        for cell in self.alive_cells:
            n = self.grid.count_alive_neighbours(cell)
            if not (n == 2 or n == 3):
                cell.kill()
        for cell in self.dead_cells:
            n = self.grid.count_alive_neighbours(cell)
            if n == 3:
                cell.spawn()
        self.render()

    def render(self):
        Renderer.rect(0, 0, self.width, self.height, color='#F1E7DC') # background
        grid_gap = min(self.width/self.grid.cols, self.height/self.grid.rows)
        self.grid.render(self.width, self.height, grid_gap)
        for cell in self.alive_cells:
            cell.render(grid_gap)
