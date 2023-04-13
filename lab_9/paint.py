import pygame as pg

pg.init()
screen = pg.display.set_mode((1920, 1080))
pg.display.set_caption("paint")
clock = pg.time.Clock()

red = (150, 0, 0)
blue = (0, 0, 100)
pink = (200, 0, 200)
gray = (20, 20, 20)

redRect = pg.Rect(0, 0, 50, 50)
blueRect = pg.Rect(50, 0, 50, 50)
pinkRect = pg.Rect(100, 0, 50, 50)
grayRect = pg.Rect(150, 0, 50, 50)

rects = [[red, redRect], [blue, blueRect], [pink, pinkRect], [gray, grayRect]]
colour = (100, 120, 140)
size = 50

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
            colour = (20, 20, 20)

def draw(mode):
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    if clik[0]:
        if mode == "line":
            pg.draw.circle(screen, colour, (posX, posY), size*0.7)
        elif mode == "square":
            pg.draw.rect(screen, colour, pg.Rect(posX, posY, size, size), 1)
        elif mode == "rectangle":
            pg.draw.rect(screen, colour, pg.Rect(posX, posY, size, size*1.3), 1)
        elif mode == "circle":
            pg.draw.circle(screen, colour, (posX, posY), size*0.7, 1)
        elif mode == "right_triangle":
            pg.draw.line(screen, colour, (posX, posY), (posX+size, posY+size), 1)
            pg.draw.line(screen, colour, (posX, posY), (posX, posY+size), 1)
            pg.draw.line(screen, colour, (posX, posY+size), (posX+size, posY+size), 1)
        elif mode == "equilateral_triangle":
            pg.draw.line(screen, colour, (posX, posY), (posX+size, posY), 1)
            pg.draw.line(screen, colour, (posX, posY), (posX+size*0.5, posY+size*3**0.5/2), 1)
            pg.draw.line(screen, colour,(posX+size*0.5, posY+size*3**0.5/2), (posX+size, posY), 1)
        elif mode == "rhombus":
            pg.draw.line(screen, colour, (posX, posY),(posX+size*0.5, posY-size*3**0.5/2), 1)
            pg.draw.line(screen, colour, (posX+size*0.5, posY-size*3**0.5/2), (posX+size, posY), 1)
            pg.draw.line(screen, colour,(posX, posY), (posX+size*0.5, posY+size*3**0.5/2), 1)
            pg.draw.line(screen, colour, (posX+size*0.5, posY+size*3**0.5/2), (posX+size, posY), 1)
        elif mode == "eraser":
            pg.draw.circle(screen, (0,0,0), (posX, posY), size)
            
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
            if event.key == pg.K_1:
                figure = 'line'
            elif event.key == pg.K_2:
                figure = 'square'
            elif event.key == pg.K_3:
                figure = 'rectangle'  
            elif event.key == pg.K_4:
                figure = 'circle'  
            elif event.key == pg.K_5:
                figure = 'right_triangle'
            elif event.key == pg.K_6:
                figure = "equilateral_triangle"
            elif event.key == pg.K_7:
                figure = 'rhombus'
            elif event.key == pg.K_8:
                figure = 'eraser'
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                if size < 400:
                    size += 1
            elif event.button == 5:  # Mouse wheel down
                if size > 1:
                    size -= 1
    
    for colrs in rects:
        pg.draw.rect(screen, colrs[0], colrs[1])

    clik = pg.mouse.get_pressed()
    posX, posY = pg.mouse.get_pos()
    draw(figure)

    colour_pick()

    clear_all()
    clock.tick(600)
    pg.display.update()
