import tkinter as tk

# TODO: Zoom level
# View offset
offset_x, offset_y = 0, 0

class Renderer:

    @staticmethod
    def set_canvas(canvas):
        Renderer.canvas = canvas

    @staticmethod
    def ensure_canvas_initialized():
        if hasattr(Renderer, 'canvas'):
            return True
        raise Exception('Canvas has not been initialized. Please use Renderer.set_canvas()')

    @staticmethod
    def line(x1, y1, x2, y2, color='#999'):
        Renderer.ensure_canvas_initialized()
        Renderer.canvas.create_line(x1, y1, x2, y2, fill=color, smooth=1, capstyle='round')

    @staticmethod
    def rect(x, y, width, height, color='#999'):
        Renderer.ensure_canvas_initialized()
        Renderer.canvas.create_rectangle(offset_x + x, offset_y + y, offset_x + x + width, offset_y + y + height, fill=color, outline=color)
