from pygame import *
import random, time
from pygame.math import Vector2
from pygame.time import Clock, set_timer

init()

block_size = 45
menu_color = (241, 207, 185)
screen_size = (block_size*20+300, block_size*20+40)
count_column, count_row = 20, 20
snake_color = (231, 84, 128)
head_color = (191, 34, 74)
border_color = (202, 94, 136)
font_color = (145, 165, 241)
font_size = 30
ms = 150
cur_time = time.time()

class SNAKE():
    def __init__(self):
        # starting postion
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # doesn't move at the beginning
        self.direction = Vector2(0,0)
        self.new_block = False
        self.grow = random.randint(1,3)
        self.randint = 0

    def draw_snake(self):
        # draw head
        draw_block(head_color, self.body[0].x, self.body[0].y)
        # draw body
        for block in self.body[1:]:
            draw_block(snake_color, block.x, block.y)

    def make_bigger(self):
        #adds block to the front of the snake
        body_copy = self.body[:]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:]          

    def move_snake(self):
        # in case you've eaten pochita
        if self.new_block == True:
            #self.randint is the count of how many blovks you need to add to the snake
            self.randint += self.grow
            self.grow = random.randint(1, 3)
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
        self.random_spawn(10, 15)

    def random_spawn(self, x, y):
        # take random point that are within borders
        self.pos = Vector2(x, y)
        self.time = time.time()

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
        self.time_of_growth = time.time()
    
    # update all the changing elements of the game every self.speed miliseconds
    def update(self, cur_time):
        self.snake.move_snake()
        self.check_collision()
        if(self.snake.randint > 0):
            #add block with interval of 0.2 seconds
            if cur_time - self.time_of_growth > 0.2:
                self.snake.make_bigger()
                self.snake.randint -= 1
                self.time_of_growth = time.time()   
            # time.sleep(0.1) 
        self.check_dead()

    # draws everything that's needed
    def draw_elements(self):
        self.pochita.draw_pochita() 
        self.snake.draw_snake()
        self.draw_menu()

    # makes a menu at the right side which shows current score and level
    def draw_menu(self):
        draw.rect(screen, menu_color, [block_size*count_column+40, 0, 1000, 1000])
        score_text = fonts.render('score: ' + str(self.score), True, font_color, menu_color)
        level_text = fonts.render('level: ' + str(self.level), True, font_color, menu_color)
        screen.blit(score_text, (block_size*20+50, 20))
        screen.blit(level_text, (block_size*20+50, 20+font_size))
    
    #checks if snake has eaten pochita 
    def check_collision(self):
        if self.pochita.pos == self.snake.body[0]:
            mixer.Sound.play(eat_sound)
            x, y = self.give_random_coordinate()
            self.pochita.random_spawn(x, y)
            self.snake.new_block = True
            # adding score one by one to not skip the part where level is inreased
            # self.snake.grow is a random integer from 1 to 3, which determines how many blocks are added to the snake
            for _ in range(self.snake.grow):
                self.score += 1

                if self.score % 4 == 0:
                    self.level +=1
                    self.update_speed()

    def give_random_coordinate(self):
        x = random.randint(0, count_column - 1)
        y = random.randint(0, count_row - 1)
        while (Vector2(x,y) in self.snake.body):
            x = random.randint(0, count_column - 1)
            y = random.randint(0, count_row - 1)
        return x, y
        
    def update_speed(self):
        # increases speed by 1/5th of current speed
        self.speed -= self.speed//5
        set_timer(USEREVENT, self.speed)
           
    def check_dead(self):
        # if snake touched border it's dead
        if not 0 <= self.snake.body[0].x < count_column or not 0 <= self.snake.body[0].y < count_row:
            mixer.Sound.play(death_sound)
            self.game_over()

        # if snake touched itseld it's dead
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # reset all parameters
        self.speed = 150
        set_timer(USEREVENT, self.speed)
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
clock = Clock()

eat_sound = mixer.Sound(r"C:\PP 2\lab_9\nom.mp3")
death_sound = mixer.Sound(r"C:\PP 2\lab_9\oof.mp3")
start_sound = mixer.Sound(r"C:\PP 2\lab_9\mario.mp3")
mixer.music.set_volume(0.5)
mixer.music.load(r"C:\PP 2\lab_9\kirby.mp3")
mixer.music.play(-1)

# before game.update_speed() is called we use this
set_timer(USEREVENT, 150)

done = False

while not done:
    cur_time = time.time()

    for ev in event.get():
        if ev.type == QUIT:
            done = True
        if ev.type == USEREVENT:
                game.update(cur_time)
        if ev.type == KEYDOWN:
            if game.snake.direction == Vector2(0, 0):
                mixer.Sound.play(start_sound)
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
                colour = (241, 192, 185)
            else: colour = (255, 255, 255)
            draw_block(colour, column, row)
        
    cur_time = time.time()

    if cur_time - game.pochita.time > 6:
        x, y = game.give_random_coordinate()
        game.pochita.random_spawn(x, y)

    game.draw_elements()

    display.flip()

    clock.tick(60)