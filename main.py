# 19.10.50

from math import sin, cos
import pygame as pg
import window
from object import Object

app = window.Window()
app.set_title()
app.run()

ax = 0
ay = 0

run = True

cube = Object()
with open("test_pics/super_cube.tvp", 'r') as f:
    cube.load(f)

axis = Object()
with open("test_pics/axis.tvp", 'r') as f:
    axis.load(f)

clock = pg.time.Clock()

while run:

    clock.tick()
    delta = clock.get_time() / 1000

    vx = cos(ay), -sin(ax)*sin(ay)
    vy = 0, cos(ax)
    vz = -sin(ay), -sin(ax)*cos(ay)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    app.win.fill((122, 122, 122))
    for x in range(4):
        for y in range(4):
            for z in range(4):
                if cube.voxels[x][y][z]:
                    pos_x = x*vx[0] + y*vy[0] + z*vz[0]
                    pos_y = x*vx[1] + y*vy[1] + z*vz[1]
                    pg.draw.rect(app.win, cube.voxels[x][y][z], (300+32*pos_x, 300+32*pos_y, 32, 32))

    for x in range(8):
        for y in range(8):
            for z in range(8):
                if axis.voxels[x][y][z]:
                    pos_x = x*vx[0] + y*vy[0] + z*vz[0]
                    pos_y = x*vx[1] + y*vy[1] + z*vz[1]
                    pg.draw.rect(app.win, axis.voxels[x][y][z], (700+32*pos_x, 300+32*pos_y, 32, 32))

    pg.display.update()



    keys = pg.key.get_pressed()
    run -= keys[27]
    ay += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * delta
    ax += (keys[pg.K_DOWN] - keys[pg.K_UP]) * delta

i = 0
