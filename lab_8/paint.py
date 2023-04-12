import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((1920, 1080))
pg.display.set_caption("paint")
clock = pg.time.Clock()


blue = (0, 0, 100)
red = (150, 0, 0)
black = (20, 20, 20)
pink = (200, 0, 200)

redRect = pg.Rect(0, 0, 50, 50)
blueRect = pg.Rect(50, 0, 50, 50)
blackRect = pg.Rect(150, 0, 50, 50)
pinkRect = pg.Rect(100, 0, 50, 50)

rects = [[red, redRect], [blue, blueRect], [black, blackRect], [pink, pinkRect]]
        #self.colour = colour
colour = (100, 120, 140)
def colour_pick():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    global colour
    if clik[0]:
        if posX < 50 and posY < 50:
            colour = red
        elif posX < 100 and posX > 50 and posY < 50:
            colour = blue
        elif posX < 150 and posX > 100 and posY < 50:
            colour = pink
        elif posX < 200 and posX > 150 and posY < 50:
            colour = (0, 0, 0)

def draw(mode):
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    if clik[0]:
        if mode == "line":
            pg.draw.circle(screen, colour, (posX, posY), 30)
        elif mode == "square":
            pg.draw.rect(screen, colour, pg.Rect(posX, posY, 80, 100), 1)
        elif mode == "circle":
            pg.draw.circle(screen, colour, (posX, posY), 60, 1)
        elif mode == "eraser":
             pg.draw.circle(screen, (0,0,0), (posX, posY), 40)
def clear_all():
        key = pg.key.get_pressed()
        if key[pg.K_LCTRL] and key[pg.K_c]:
            screen.fill((0, 0, 0))

figure = "line"

RUN = True
while RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            RUN = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                figure = 'circle'
            elif event.key == pg.K_s:
                figure = 'square'
            elif event.key == pg.K_e:
                figure = 'eraser'
            elif event.key == pg.K_l:
                figure = 'line'

    for colrs in rects:
        pg.draw.rect(screen, colrs[0], colrs[1])

    clik = pg.mouse.get_pressed()
    posX, posY = pg.mouse.get_pos()
    draw(figure)

    colour_pick()

    clear_all()
    clock.tick(600)
    pg.display.update()
