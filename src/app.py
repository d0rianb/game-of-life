import tkinter as tk
import asyncio

from render import Renderer

class App:
    def __init__(self, game):
        self.game = game
        self.main_window = Window(100, 100)
        self.game.width, self.game.height = self.main_window.width, self.main_window.height
        self.canvas = tk.Canvas(self.main_window, width=self.game.width, height=self.game.height, bg='#EEE', highlightthickness=0)
        self.mainloop = None
        Renderer.set_canvas(self.canvas)

    def start(self):
        self.canvas.pack()
        self.mainloop = self.game.update()
        self.main_window.start()

    def kill(self):
        self.mainloop.set() # stope the mainloop


class Window(tk.Tk):
    def __init__(self, width_percentage, height_percentage):
        ''' width, height are percentage of the screen size '''
        super().__init__()
        self.title('Conway\'s Game of life')
        self.protocol('WM_DELETE_WINDOW', self.kill)
        self.state('zoomed')
        # self.attributes('-topmost', True)
        screenwidth, screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.width, self.height = screenwidth * width_percentage / 100, screenheight * height_percentage / 100
        offset_x, offset_y = (screenheight - self.width) / 2, (screenheight - self.height) / 2  # center the window
        self.geometry('%dx%d%+d%+d' % (self.width, self.height, offset_x, offset_y))
        # TODO: handle on resize event

    def start(self):
        self.mainloop()

    def kill(self, *args):
        self.destroy()
