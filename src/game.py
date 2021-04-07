from render import Renderer
from grid import Grid, Cell

class Game:
    def __init__(self, width, height):
        self.grid = Grid.generate(50, width, height) # 50 columns
        self.width = width
        self.height = height
        self.alive_cells = []
        self.alive_cells_coords = []

    def update(self):
        self.alive_cells = [cell for cell in self.grid.cells if cell.is_alive]
        # self.dead_cells = [cell for cell in self.grid.cells if not cell.is_alive] # OPTIMIZE: remove ?
        # for cell in self.alive_cells:
        #     n = self.grid.count_alive_neighbours(cell)
        #     if not (n == 2 or n == 3):
        #         self.grid.toggle_state(cell.x, cell.y, False)
        #         # cell.kill()
        # for cell in self.dead_cells:
        #     n = self.grid.count_alive_neighbours(cell)
        #     if n == 3:
        #         self.grid.toggle_state(cell.x, cell.y, False)
        #         # cell.spawn()
        self.render()

    def toggle_cell_state(self, x, y):
        grid_gap = min(self.width/self.grid.cols, self.height/self.grid.rows)
        self.grid.toggle_state(int(x/grid_gap), int(y/grid_gap))

    def render(self):
        Renderer.rect(0, 0, self.width, self.height, color='#F1E7DC') # background
        grid_gap = min(self.width/self.grid.cols, self.height/self.grid.rows)
        self.grid.render(self.width, self.height, grid_gap)
        for cell in self.alive_cells:
            cell.render(grid_gap)
