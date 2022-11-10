from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from ball import Ball, BigBall

boy = None
grass = None
balls = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)

    # 충돌 대상 정보 기록
    game_world.add_collision_pairs(boy, balls, 'boy:ball')
    game_world.add_collision_pairs(grass, balls, 'grass:ball')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


    for a, b, group in game_world.all_collision_pairs():
        if collide(a,b):#충돌 체크
            print("COLLISION", group)
            # 충돌 처리
            # 객체 스스로 제거
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    #충돌 체크
    # 충돌 처리
    # for ball in balls.copy(): # 모든 볼에 대해
    #     if collide(boy, ball): # 서로 출돌을 하면
    #         print("COLLISION boy:ball") # 메세지를 보내겠다.
    #         balls.remove(ball)
    #         game_world.remove_object(ball)
    delay(0.9)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True
