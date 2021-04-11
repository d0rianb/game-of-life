from render import Renderer
from grid import Grid, Cell

class Game:
    def __init__(self, width, height):
        self.grid = Grid.generate(50, width, height) # 50 columns
        self.width = width
        self.height = height

    def update(self):
        print('update')
        # for cell in self.grid.cells:
        #     n = self.grid.count_alive_neighbours(cell)
        #     if cell.is_alive and not (n == 2 or n == 3):
        #         self.grid.toggle_state(cell.x, cell.y, False) # kill a cell
        #     if not cell.is_alive and n == 3:
        #         self.grid.toggle_state(cell.x, cell.y, True) # spawn a cell
        self.render()

    def toggle_cell_state(self, x, y):
        grid_gap = min(self.width/self.grid.cols, self.height/self.grid.rows)
        self.grid.toggle_state(int(x/grid_gap), int(y/grid_gap))

    def render(self):
        Renderer.rect(0, 0, self.width, self.height, color='#F1E7DC') # background
        grid_gap = min(self.width/self.grid.cols, self.height/self.grid.rows)
        self.grid.render(self.width, self.height, grid_gap)
        for cell in self.grid.cells:
            if cell.is_alive:
                cell.render(grid_gap)
