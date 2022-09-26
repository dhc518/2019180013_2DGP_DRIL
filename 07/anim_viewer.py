from pico2d import *
open_canvas()
grass = load_image('grass.png')
run = load_image('Knuckles_run.png')
running = load_image('Knuckles_running.png')
climb = load_image('Knuckles_climb.png')
falling = load_image('Knuckles_falling.png')
landing = load_image('Knuckles_landing.png')

x = 0
y = 70
frame = 0

def draw(name, frame, width,height, x, y, sec):
    clear_canvas()
    grass.draw(400, 30)
    name.clip_draw(frame * width, 0, width, height, x, y)
    update_canvas()
    delay(sec)
    get_events()

while (x < 400):
    draw(run, frame,42,45,x, 70, 0.05)
    frame = (frame + 1) % 8
    x += 5

while (x < 800):
    draw(running, frame, 32,45, x, 70, 0.01)
    frame = (frame + 1) % 4
    x += 5

while(y<300):
    draw(climb, frame, 43,45, 780, y, 0.05)
    frame = (frame + 1) % 8
    y += 5

while(y>280):
    draw(falling, 0, 43,52, 780, y, 0.05)
    y -= 5

while(y>80):
    draw(falling, 1, 43,52, 780, y, 0.01)
    y -= 5

while(y>70):
    draw(landing,frame, 40,52, 780, y, 0.05)
    frame = (frame + 1) % 2
    y -= 5

close_canvas()
