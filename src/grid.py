from render import Renderer

class Grid:
    def __init__(self, rows, cols):
        self.cells = []
        self.rows = rows
        self.cols = cols
        self.initialize()

    @staticmethod
    def generate(cols, width, height):
        ''' Generate a grid from a certain number of columns with square cells '''
        grid_gap = width / cols
        rows = int(height / grid_gap)
        return Grid(rows, cols)

    def initialize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells.append(Cell(i, j))

    def get_cell(self, x, y):
        cell_array = list(filter(lambda cell: cell.x == x and cell.y == y, self.cells))
        if len(cell_array):
            return cell_array[0]


    def toggle_state(self, x, y, state=True):
        # no args : toggle state / True = alive / False = dead
        cell = self.get_cell(x, y)
        if state:
            cell.is_alive = state
        else:
            cell.is_alive = not cell.is_alive

    def get_neighbours(self, cell):
        neighbours = []
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1) and not (cell.x - 1 + i < 0 or cell.y - 1 + j < 0 or cell.x - 1 + i >= self.cols or cell.y - 1 + i >= self.rows):
                    neighbours.append(self.get_cell(cell.x - 1 + i, cell.y - 1 + j))
        return neighbours

    def count_alive_neighbours(self, cell):
        return len(self.get_neighbours(cell))

    def render(self, width, height, grid_gap):
        for x in range(self.cols):
            Renderer.line(x*grid_gap, 0, x*grid_gap, height, color='#aaa')
        for y in range(self.rows):
            Renderer.line(0, y*grid_gap, width, y*grid_gap, color='#aaa')


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False

    def __repr__(self):
        return f'Cell at {self.x}, {self.y}'

    def render(self, grid_gap):
        Renderer.rect(self.x*grid_gap, self.y*grid_gap, grid_gap, grid_gap)
