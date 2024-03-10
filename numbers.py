from random import randint
from time import time

WIDTH = 400
HEIGHT = 400

start_time = time()

dots = []
lines = []
red_dots = []
blue_lines = []

next_dot = 0
next_red_dot = 0
number_of_dots = 5
number_of_red_dots = 5
game_over = False

#blue dots
for dot in range(0, number_of_dots):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

# red dots
for red_dot in range(0, number_of_red_dots):
    actor_red = Actor("red-dot")
    actor_red.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    red_dots.append(actor_red)

def update():
    pass

def draw():
    global start_time
    current_time = time()
    elapsed_time = current_time - start_time

    screen.fill("black")
    number = 1
    number_red = 1
    screen.draw.text("Time: " + str(round(elapsed_time)), topleft=(10, 10))
    # Draw blue dots and lines
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 0, 0))
    # Draw red dots and lines
    for red_dot in red_dots:
        screen.draw.text(str(number_red), (red_dot.pos[0], red_dot.pos[1] + 12))
        red_dot.draw()
        number_red += 1
    for blue_line in blue_lines:
        screen.draw.line(blue_line[0], blue_line[1], (0, 0, 255))
    # Game over text
    if game_over:
        global end_time
        total_time = end_time - start_time
        screen.clear()
        screen.draw.text("Game Over!", topleft=(50, 50), fontsize=60, color=(100, 0, 0))
        screen.draw.text("Total time: " + str(round(total_time)), topleft=(100,100), fontsize=60)

def next_level():
    global next_dot, number_of_dots
    if next_dot == number_of_dots - 1:
        new_dot = Actor("dot")
        new_dot.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(new_dot)
        number_of_dots += 1

    global next_red_dot, number_of_red_dots
    if next_red_dot == number_of_red_dots - 1:
        new_red_dot = Actor("red-dot")
        new_red_dot.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        red_dots.append(new_red_dot)
        number_of_red_dots += 1

def on_mouse_down(pos):
    global next_dot, lines, game_over, next_red_dot, blue_lines, end_time
    if not game_over:
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot += 1
            next_level()
   
        elif red_dots[next_red_dot].collidepoint(pos):
            if next_red_dot:
                blue_lines.append((red_dots[next_red_dot - 1].pos, red_dots[next_red_dot].pos))
            next_red_dot += 1
            next_level()

        else: 
            game_over = True
            end_time = time()
    else:
        lines = []
        next_dot = 0
        next_red_dot = 0
        blue_lines = []
        game_over = True
        end_time = time()

