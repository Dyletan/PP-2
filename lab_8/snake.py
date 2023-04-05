from pygame import *
import random
from pygame.math import Vector2

init()

block_size = 45
menu_color = (60, 60, 60)
font_size = 30
screen_size = (block_size*20+300, block_size*20+40)
count_column, count_row = 20, 20
snake_color = (0, 90, 10)
head_color = (0, 102, 0)
border_color = (150, 200, 30)
ms = 150

class SNAKE():
    def __init__(self):
          # starting postion
          self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
          # doesn't move at the beginning
          self.direction = Vector2(0,0)
          self.new_block = False

    def draw_snake(self):
         # draw head
         draw_block(head_color, self.body[0].x, self.body[0].y)
         # draw body
         for block in self.body[1:]:
              draw_block(snake_color, block.x, block.y)

    def move_snake(self):
        # in case you've eaten pochita
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # copy without tail
            body_copy = self.body[:-1]
            # insert a head and move it to direction of input
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    def reset(self):
        # when game over start at this position again
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class POCHITA(SNAKE):
    def __init__(self):
        super().__init__()
        self.random_spawn()

    def random_spawn(self):
        # take random point that are within borders
        self.x = random.randint(0, count_column - 1)
        self.y = random.randint(0, count_row - 1)
        # if point is inside snake take another one
        while(Vector2(self.x, self.y) in self.body):
            self.x = random.randint(0, count_column - 1)
            self.y = random.randint(0, count_row - 1)
        # initialize the point
        self.pos = Vector2(self.x, self.y)

    def draw_pochita(self):
        # draws pochita at a randomrly created position
        screen.blit(poch, (int(self.pos.x * block_size+20) , int(self.pos.y * block_size+20)))

class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.pochita = POCHITA()
        self.score = 0
        self.level = 0
        # every 150 miliseconds game.update() method is triggered
        self.speed = 150
    # checks for any updates and acts accrodingly
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_dead()
    # draws everything that's needed
    def draw_elements(self):
        self.pochita.draw_pochita() 
        self.snake.draw_snake()
        self.draw_menu()
    # makes a menu at the right side which shows current score and level
    def draw_menu(self):
        draw.rect(screen, menu_color, [block_size*count_column+40, 0, 1000, 1000])
        score_text = fonts.render('score: ' + str(self.score), True, (255,255,255), menu_color)
        level_text = fonts.render('level: ' + str(self.level), True, (255,255,255), menu_color)
        screen.blit(score_text, (block_size*20+50, 20))
        screen.blit(level_text, (block_size*20+50, 20+font_size))
    #checks if snake has eaten pochita 
    def check_collision(self):
        if self.pochita.pos == self.snake.body[0]:
           self.pochita.random_spawn()
           self.snake.new_block = True
           self.score += 1
           if self.score % 4 == 0:
               self.level +=1
               self.update_speed()

    def update_speed(self):
        # increases speed by 1/5th of current speed
        self.speed -= self.speed//5
        time.set_timer(USEREVENT, self.speed)
           
    def check_dead(self):
        # if snake touched border it's dead
        if not 0 <= self.snake.body[0].x < count_column or not 0 <= self.snake.body[0].y < count_row:
            self.game_over()

        # if snake touched itseld it's dead
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # reset all parameters
        self.speed = 150
        time.set_timer(USEREVENT, self.speed)
        self.level = 0
        self.score = 0
        self.snake.reset()
         
def draw_block(colour, column, row):
            draw.rect(screen, colour, [20+block_size*column, 20+row*block_size, block_size, block_size])

# render an image of pochita         
poch = image.load(r"C:\PP 2\lab_8\sprite_snake\pochita.png")
# make the image the size of block	
poch = transform.scale(poch, (block_size, block_size))

# create font
fonts = font.Font('freesansbold.ttf', font_size)

game = MAIN()

screen = display.set_mode(screen_size)
screen.fill(border_color)
clock = time.Clock()

# before game.update_speed() is called we use this
time.set_timer(USEREVENT, 150)

done = False

while not done:
    for ev in event.get():
        if ev.type == QUIT:
            done = True
        if ev.type == USEREVENT:
                game.update()
        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                game.snake.direction = Vector2(0, -1)
            if ev.key == K_DOWN:
                game.snake.direction = Vector2(0, 1)
            if ev.key == K_RIGHT:
                game.snake.direction = Vector2(1, 0)
            if ev.key == K_LEFT:
                game.snake.direction = Vector2(-1, 0)
    
    for row in range(count_column):
        for column in range(count_row):
            if (column+row) % 2 == 0:
                colour = (0, 100, 90)
            else: colour = (0, 80, 80)
            draw_block(colour, column, row)

    game.draw_elements()

    display.flip()

    clock.tick(60)