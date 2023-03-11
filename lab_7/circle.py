import pygame

pygame.init()

default_size = (500, 500)
radius = 25
screen = pygame.display.set_mode(default_size)

done = False
x = 250
y = 250
color = (255, 0, 0)
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and y <= default_size[1]-radius:
                    y += 20
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP)and y >= radius:
                    y -= 20
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and x <= default_size[0]-radius:
                    x += 20
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and x >= radius:
                    x -= 20
        
        #makes the screen white
        screen.fill((255, 255, 255))
        
        pygame.draw.circle(screen, color, (x, y), radius)
        #sets refreshrate to 60
        clock.tick(60)
        #makes all updates to the screen visible
        pygame.display.flip()
        