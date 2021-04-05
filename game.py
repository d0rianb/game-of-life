from render import Renderer
from grid import Grid, Cell


# define by the interface
GRID_GAP = 10
WIDTH = 1024
HEIGHT = 720


class Game:
    def __init__(self):
        self.grid = Grid(50, 40)
        self.alive_cells = []
        self.alive_cells_coords = []

    def update(self):
        self.alive_cells = list(filter(lambda cell: cell.is_alive, self.grid.cells))
        self.dead_cells = [cell for cell in self.grid.cells if cell not in self.alive_cells]
        for cell in self.alive_cells:
            n = self.grid.count_alive_neighbours(cell)
            if not (n == 2 or n == 3):
                cell.kill()
            self.render(cell)
        for cell in self.dead_cells:
            n = self.grid.count_alive_neighbours(cell)
            if n == 3:
                cell.spawn()
            self.render(cell)
        # auto call after 16ms (tk.after ?)

    def render(self, cell):
        self.grid.render()
        for cell in self.alive_cells:
            cell.render(GRID_GAP)
