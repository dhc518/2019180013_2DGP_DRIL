from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global dir_x
    global dir_y
    global looking
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                looking = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                looking = 0
            if event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1



open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
looking = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir_x or dir_y != 0:
        character.clip_draw(frame * 100, 100 * looking, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * (2+looking), 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y *5
    #이동 한계
    if(x > TUK_WIDTH): x = TUK_WIDTH
    if (x < 0): x = 0
    if (y > TUK_HEIGHT): y = TUK_HEIGHT
    if (y < 0): y = TUK_WIDTH

    delay(0.01)

close_canvas()