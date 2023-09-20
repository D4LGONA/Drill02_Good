from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():       # pass 일단 써놓기
    print('circle')
    
    cx, cy, r = 800 / 2, 600 / 2, 200 # 이런 식의 표현이 좋음
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def run_rectangle():
    print('rectangle')
    pass

while True:
    run_circle()        # 함수를 먼저 만들고 내용을 만들 것
    run_rectangle()     
    break               # break를 써서 우선 제대로 되는지 확인


close_canvas()
