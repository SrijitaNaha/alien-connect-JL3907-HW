import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 600

aliens_list = []
lines_list = []
next_alien = 0

time_start = 0
time_end = 0
time_total = 0

number_of_aliens = 6

def create_alien():
    global time_start
    for i in range (0,number_of_aliens):
        alien = Actor("alien")
        alien.pos = random.randint(40,WIDTH-40), random.randint(40,HEIGHT-40)
        aliens_list.append(alien)
    time_start = time()
    


def draw():
    global time_total
    screen.blit("background",(0,0))
    x = 1
    for alien in aliens_list:
        screen.draw.text(str(x), (alien.pos[0], alien.pos[1]+50))
        alien.draw()
        x += 1
    for line in lines_list:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_alien < number_of_aliens:
        total_time = time() - time_start
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
        



def update():
    pass

def on_mouse_down(pos):
    global next_alien,lines_list
    if next_alien < number_of_aliens:
        if aliens_list[next_alien].collidepoint(pos):
            if next_alien:
                lines_list.append((aliens_list[next_alien-1].pos, aliens_list[next_alien].pos))
            next_alien = next_alien + 1
        else:
            lines_list = []
            next_alien = 0
    

create_alien()
pgzrun.go()        