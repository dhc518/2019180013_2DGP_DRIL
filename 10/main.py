import pico2d
import play_state
import logo_state
start_state = logo_state

def run_program():
    start_state.enter()#초기화
    while start_state.running:  # game main loop code
        start_state.handle_events()
        start_state.update()
        start_state.draw()
        pico2d.delay(0.05)
    start_state.exit()  # 종료
'''
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()
'''
pico2d.open_canvas()
run_program()
start_state = play_state
run_program()
pico2d.close_canvas()