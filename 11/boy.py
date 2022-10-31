from pico2d import *

# 이베느 정의
#RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, A = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_a) : A,
}



# 스테이트를 구현 - 클래스를 이용해서
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0  # 정지 상태
        self.timer = 1000



    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 # 시간 감소
        if self.timer == 0: # 시간이 다 흐르면
            self.add_event(TIMER) #타이머 이벤트 큐에 삽입

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:

    def enter(self, event):
        print('ENTER RUN')
        self.dir = 0
        # 어떤 이벤트 떄문에, Run으로 들어왔는지 파악을 하고, 그 이벤트에 따라서 실제 방향을 결정
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir


    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) #clamp가 뭔지 찾아보기


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:

    def enter(self, event):
        print('ENTER AUTO_RUN')
        # 어떤 이벤트 떄문에, Run으로 들어왔는지 파악을 하고, 그 이벤트에 따라서 실제 방향을 결정
        if self.dir == 0:
            self.dir = self.face_dir

    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir


    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        #self.x = clamp(0, self.x, 800) #clamp가 뭔지 찾아보기
        if self.x == 800:
            self.dir = -1
        elif self.x == 0:
            self.dir = 1


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:

    def enter(self, event):
        self.dir = 0  # 정지 상태
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self):
        print('EXIT SLEEP')


    def do(self):
        self.frame = (self.frame + 1) % 8


    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)


# 상태 변환

next_state = {
    SLEEP: {RU:RUN, LU:RUN, RD:RUN, LD:RUN, TIMER:SLEEP, A:AUTO_RUN},
    IDLE : {RU:RUN, LU:RUN, RD:RUN, LD:RUN, TIMER:SLEEP, A:AUTO_RUN},
    RUN : { RU:IDLE, LU:IDLE, LD:IDLE, RD:IDLE, TIMER:RUN, A:AUTO_RUN},
    AUTO_RUN : {RU:RUN, LU:RUN, LD:RUN, RD:RUN, TIMER:AUTO_RUN, A:IDLE}
}


class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):#키입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

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
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        # 초기 상태 설정과
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # 큐에 이벤트가 있으면, 이벤트가 발생했으면
            event = self.q.pop()
            self.cur_state.exit(self)   # 현재 상태를 나가야되고,
            self.cur_state = next_state[self.cur_state][event]    # 다음 상태를 구한다.
            self.cur_state.enter(self, event)
        #self.frame = (self.frame + 1) % 8
        #self.x += self.dir * 1
        #self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

#        if self.dir == -1:
#            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
#        elif self.dir == 1:
#            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
#        else:


