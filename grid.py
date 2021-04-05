from render import Renderer


class Grid:
    def __init__(self, rows, cols):
        self.cells = []
        self.rows = rows
        self.cols = cols

    def initialize(self):
        for i in range(rows):
            for j in range(cols):
                self.add_cell(Cell(self, i, j))

    def toggle_state(self, x, y, state=True):
        # no args : toggle state / True = alive / False = dead
        cell = self.get_cell(x, y)
        if state:
            cell.is_alive = state
        else:
            cell.is_alive = not cell.is_alive

    def add_cell(self, cell):
        # TODO: check if cell already exists
        self.cells.append(self, cell)

    def get_neighbours(self, cell):
        neighbours = []
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1) and not (x - 1 + i < 0 or y - 1 + j < 0 or x - 1 + i >= self.cols or y - 1 + i >= self.rows):
                    neighbours.append(self.get_cell(x - 1 + i, y - 1 + j))
        return neighbours

    def count_alive_neighbours(self, cell):
        return len(self.get_neighbours(cell))

    def get_cell(self, x, y):
        return filter(lambda cell: cell.x == x and cell.y == y, self.cells)

    def render(self):
        for x in range(self.grid.cols):
            Renderer.line(x*GRID_GAP, 0, x*GRID_GAP, HEIGHT)
        for y in range(self.grid.rows):
            Renderer.line(0, y*GRID_GAP, WIDTH, y*GRID_GAP)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False

    def kill(self):
        self.grid.toggle_state(self.x, self.y)

    def spawn(self):
        self.grid.toggle_state(self.x, self.y)

    def render(self, grid_gap):
        Renderer.rect(self.x*grid_gap, self.y*grid_gap, grid_gap, grid_gap)
