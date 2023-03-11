import pygame as pg
import datetime

minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
diff_minute = minute - 30
diff_second = second - 30
oldtime = datetime.datetime.now().second

angle = -6 * diff_minute
angle2 = -6 * diff_second
count = second

pg.init()
pos = (500, 500)
screen = pg.display.set_mode((1000, 1000))

bg = pg.image.load(r"lab_7\clock\clock.png")
arrow = pg.image.load(r"lab_7\clock\arrow.png")
arrow2 = pg.image.load(r"lab_7\clock\arrow2.png")

w, h = arrow.get_size()
box = [pg.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]

w2, h2 = arrow2.get_size()
box2 = [pg.math.Vector2(p) for p in [(0, 0), (w2, 0), (w2, -h2), (0, -h2)]]

done = False
screen.fill((255, 255, 255))
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                    done = True

    box_rotate = [p.rotate(angle) for p in box]

    box_rotate2 = [p.rotate(angle2) for p in box2]

    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    min_box2 = (min(box_rotate2, key=lambda p: p[0])[0], min(box_rotate2, key=lambda p: p[1])[1])
    max_box2 = (max(box_rotate2, key=lambda p: p[0])[0], max(box_rotate2, key=lambda p: p[1])[1])

    origin = (pos[0] + min_box[0]-5, pos[1] - max_box[1])
    origin2 = (pos[0] + min_box2[0], pos[1] - max_box2[1])

    screen.blit(bg, (37, 10))
    pg.draw.circle(screen, (0,0,0), pos, 25)
    
    rotated_image2 = pg.transform.rotate(arrow2, angle2)
    screen.blit(rotated_image2, origin2)    
    rotated_image = pg.transform.rotate(arrow, angle)
    screen.blit(rotated_image, origin)

    cur_time =  datetime.datetime.now().second
    time_passed = cur_time - oldtime
    if time_passed >= 1 or time_passed <= -50:
        count += 1
        angle2 -= 6
        oldtime = cur_time
        
    if count >= 60:
          angle -= 6
          count = 0
   
    pg.display.flip()
    clock.tick(60)