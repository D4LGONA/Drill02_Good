from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():       # pass 일단 써놓기
    print('circle')
    pass

def run_rectangle():
    print('rectangle')
    pass

while True:
    run_circle()        # 함수를 먼저 만들고 내용을 만들 것
    run_rectangle()     
    break               # break를 써서 우선 제대로 되는지 확인


close_canvas()
