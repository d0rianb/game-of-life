import tkinter as tk

from game import Game
from render import Renderer

FRAMERATE = 60  # fps

class App:
    def __init__(self):
        self.main_window = Window(100, 100)
        self.game = Game(self.main_window.width, self.main_window.height)
        self.canvas = tk.Canvas(self.main_window, width=self.game.width, height=self.game.height, bg='#EEE', highlightthickness=0)
        self.canvas.pack()
        self.bind_keys()
        Renderer.set_canvas(self.canvas)

    def update(self):
        self.game.render()
        self.main_window.after(1000 // FRAMERATE, self.update)

    def bind_keys(self):
        self.main_window.on_event('<Button-1>', lambda event: self.game.toggle_cell_state(event.x, event.y))
        self.main_window.on_event('<space>', lambda event: self.update())

    def start(self):
        self.main_window.state('zoomed')
        self.update()
        self.main_window.mainloop()


class Window(tk.Tk):
    def __init__(self, width_percentage, height_percentage):
        """ width, height are percentage of the screen size """
        super().__init__()
        self.title('Conway\'s Game of life')
        self.protocol('WM_DELETE_WINDOW', self.kill)
        # self.attributes('-topmost', True)
        screenwidth, screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.width, self.height = screenwidth * width_percentage / 100, screenheight * height_percentage / 100
        offset_x, offset_y = (screenheight - self.width) / 2, (screenheight - self.height) / 2  # center the window
        self.geometry('%dx%d%+d%+d' % (self.width, self.height, offset_x, offset_y))
        # TODO: handle on resize event

    def on_event(self, event_name, callback):
        self.bind(event_name, callback)

    def kill(self, *args):
        self.destroy()
