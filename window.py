import pygame as pg

pg.init()
class Window:
    win = None
    def set_title(self, title: str = "UVEiUVE"):
        pg.display.set_caption(title)
    def run(self):
        self.win = pg.display.set_mode((1280, 720))
        self.icon = pg.image.load('icon.png')
        pg.display.set_icon(self.icon)
