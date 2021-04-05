import tkinter as tk


class App:
    def __init__(self, game):
        self.main_window = Window(100, 100)
        self.game = game

    def start(self):
        self.main_window.start()
        self.game.update()


class Window(tk.Tk):
    def __init__(self, width_percentage, height_percentage):
        ''' width, height are percentage of the screen size '''
        super().__init__()
        self.title('Conway\'s Game of life')
        self.protocol('WM_DELETE_WINDOW', self.kill)
        self.attributes('-topmost', True)
        screenwidth, screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.width, self.height = screenwidth * width_percentage / 100, screenheight * height_percentage / 100
        offset_x, offset_y = (screenheight - self.width) / 2, (screenheight - self.height) / 2  # center the window
        self.geometry('%dx%d%+d%+d' % (self.width, self.height, offset_x, offset_y))
        self.resizable(width=False, height=False)

    def start(self):
        self.mainloop()

    def kill(self, *args):
        self.destroy()
