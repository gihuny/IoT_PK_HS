import RPi.GPIO as GPIO
import time

from doorlock_gpios import *
from doorlock_states import *

GPIO.cleanup()

# PIN 표기방식 설정
GPIO.setmode(GPIO.BOARD)

# 상수들 
ON = GPIO.HIGH
OFF = GPIO.LOW

PUSHED = GPIO.LOW
LOCKTIME = 10

# 스위치와 LED PIN 번호를 각각 읽기 좋게 변수에 할당
SWITCH = {
    40: { 'color': 'BTN_W', 'name': '0'},
    38: { 'color': 'BTN_Y', 'name': '1'},
    36: { 'color': 'BTN_B', 'name': '2'},
    16: { 'color': 'BTN_G', 'name': 'ENTER'},
    12: { 'color': 'BTN_R', 'name': 'MODE'}
}

LED = {
    37: 'LED_G', # 0, GREEN
    35: 'LED_R', # 1, RED
    33: 'LED_Y'  # 2, YELLOW
}

# 도어락 메인함수
def doorlock(SWITCH, LED):
    print('Doorlock started')

    # Ready 모드 설정
    mode_ready(SWITCH, LED)

    # 무한루프 (Ready 모드에서 시작)
    while(True):
        # check_events(SWITCH)

        # 조건 검색 및 분기

        # 입력이면 비번확인 모드로 진입.
        check_pin = search_pin_switch(SWITCH, 'ENTER')
        if GPIO.event_detected(check_pin) is True:
            pwd_result = check_password(SWITCH, LED, PASSWORD)

            # 성공시 open 모드로 진입.
            if pwd_result is True:
                open_door(SWITCH,LED)

            # 실패시 lock 모드로 진입.
            else:
                lock_door(SWITCH, LED, LOCKTIME) # locktime 10초

            print("Ready Mode")

        # 비번변경이면 비번변경 모드로 진입.
        check_pin = search_pin_switch(SWITCH, 'MODE')
        if GPIO.event_detected(check_pin) is True:
	    #비번변경 모드
            change_pwd(SWITCH,LED)

        # 100미리동안 쉬기
        time.sleep(0.1)	# 100ms sleep

if __name__ == '__main__':
    # GPIO 초기화
    init_gpios(SWITCH, LED)
    PASSWORD = [1, 2, 1, 0]
    #check_gpios(SWITCH, LED)
    doorlock(SWITCH, LED)
    GPIO.cleanup()
    print('GPIO Cleanedup!\n')

