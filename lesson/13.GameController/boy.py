from pico2d import *

# 이베느 정의
#RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
}



# 스테이트를 구현 - 클래스를 이용해서
class IDLE:
    @staticmethod
    def enter():
        print('ENTER IDLE')
        pass

    @staticmethod
    def exit():
        print('EXIT IDLE')
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass

class RUN:

    def enter():
        print('ENTER RUN')
        pass

    def exit():
        print('EXIT RUN')
        pass

    def do():
        pass

    def draw():
        pass

next_state = {
    IDLE : {RU:RUN, LU:RUN, RD:RUN, LD:RUN},
    RUN : { RU:IDLE, LU:IDLE, LD:IDLE, RD:IDLE}
}


class Boy:

    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):#키입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if self.q:# 만약에 list q에 뭔가 들어있으면
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state =  next_state[self.cur_state][event]
            self.cur_state.enter()

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        # 초기 상태 설정과
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()

        #self.frame = (self.frame + 1) % 8
        #self.x += self.dir * 1
        #self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw()

#        if self.dir == -1:
#            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
#        elif self.dir == 1:
#            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
#        else:
#            if self.face_dir == 1:
#                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
#            else:
#                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

