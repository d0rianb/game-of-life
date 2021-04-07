import tkinter as tk

 
# TODO: Zoom level
# View offset
offset_x, offset_y = 0, 0


class Renderer:

    @staticmethod
    def set_canvas(canvas):
        Renderer.canvas = canvas

    @staticmethod
    def line(x1, y1, x2, y2, color='#555'):
        Renderer.canvas.create_line(x1, y1, x2, y2, fill=color, smooth=1, capstyle='round')

    @staticmethod
    def rect(x, y, width, height, color='#555'):
        Renderer.canvas.create_rectangle(offset_x, offset_y, offset_x + width, offset_y + height, fill=color, outline=color)
