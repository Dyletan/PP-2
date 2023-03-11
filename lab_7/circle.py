import pygame as pg

pg.init()

default_size = (500, 500)
radius = 25
screen = pg.display.set_mode(default_size)

done = False
x = 250
y = 250
color = (255, 0, 0)
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                    done = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN and y <= default_size[1]-radius:
                y += 20
            elif (event.type == pg.KEYDOWN and event.key == pg.K_UP)and y >= radius:
                y -= 20
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and x <= default_size[0]-radius:
                x += 20
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT and x >= radius:
                x -= 20
    
    #makes the screen white
    screen.fill((255, 255, 255))
    
    pg.draw.circle(screen, color, (x, y), radius)
    #sets refreshrate to 60
    clock.tick(60)
    #makes all updates to the screen visible
    pg.display.flip()
    