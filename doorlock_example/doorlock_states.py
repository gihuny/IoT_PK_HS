import RPi.GPIO as GPIO
import time

from doorlock_gpios import *

# 상수들 
ON = GPIO.HIGH
OFF = GPIO.LOW

# 대기상태 함수
def mode_ready(SWITCH, LED):
    print("Set Ready Mode")

    # LED Y ON
    led_onoff(search_pin_led(LED,'LED_Y'), ON)
 
    # Event Enable: Enter and CHMOD button
#    for pin in SWITCH:
#        if SWITCH[pin]['name'] is 'ENTER' or SWITCH[pin]['name'] is 'MODE':
#            event_enable(pin)

    event_enable(search_pin_switch(SWITCH, 'ENTER'))
    event_enable(search_pin_switch(SWITCH, 'MODE'))

# 비번확인 상태함수
def check_password(SWITCH, LED, PASSWORD):
    print("Enter Password")

    # 번호키 활성화
    event_enable(search_pin_switch(SWITCH, '0'))
    event_enable(search_pin_switch(SWITCH, '1'))
    event_enable(search_pin_switch(SWITCH, '2'))

    # 비번변경 키 비활성화
    event_disable(search_pin_switch(SWITCH, 'MODE'))

#    print("chkpwd entered")
#    check_events(SWITCH)

    num_of_keypress = 0
    keypress_pattern = [0, 0, 0, 0]
    time_count = 0

    # 키가 눌릴때마다 키패턴에 저장
    while(True):
        # 번호확인
        if GPIO.event_detected(search_pin_switch(SWITCH, 'ENTER')) is True:
            break    # exit keypress
        elif GPIO.event_detected(search_pin_switch(SWITCH, '0')) is True:
            if num_of_keypress < 4:
                keypress_pattern[num_of_keypress] = 0
            num_of_keypress += 1
        elif GPIO.event_detected(search_pin_switch(SWITCH, '1')) is True:
            if num_of_keypress < 4:
                keypress_pattern[num_of_keypress] = 1
            num_of_keypress += 1
        elif GPIO.event_detected(search_pin_switch(SWITCH, '2')) is True:
            if num_of_keypress < 4:
                keypress_pattern[num_of_keypress] = 2
            num_of_keypress += 1

        # LED 점멸: 1초당 1번
        if(time_count >= 0.5):
            toggle_led(search_pin_led(LED,'LED_Y'))
            time_count = 0

        time_count += 0.1
        time.sleep(0.1)

    # Enter키가 눌렸다면 비번확인 모드 종료

    # 번호키 비활성화
    event_disable(search_pin_switch(SWITCH, '0'))
    event_disable(search_pin_switch(SWITCH, '1'))
    event_disable(search_pin_switch(SWITCH, '2'))

    # 비번변경 키 활성화
    event_enable(search_pin_switch(SWITCH, 'MODE'))

    # LED Y ON
    led_onoff(search_pin_led(LED,'LED_Y'), ON)

    # 결과 리턴
    if keypress_pattern == PASSWORD and num_of_keypress == 4:
        print('PASSWORD correct')
        return True
    else:
        print('PASSWORD wrong')
        return False

# 비번 맞았을 때 
def open_door(SWITCH, LED):
    print('Door Opened!')

    # 문 열기 - 모터 등을 연결해서 실제 움직임 표현한다면 이곳에.
    pass

    # 노란불은 끄고 초록불 켜고
    led_onoff(search_pin_led(LED,'LED_Y'), OFF)
    led_onoff(search_pin_led(LED,'LED_G'), ON)

    # 비번변경 키 비활성화
    event_disable(search_pin_switch(SWITCH, 'MODE'))

    # Enter키가 눌릴때까지 아무것도 하지 않는다.
    while(True):
        if GPIO.event_detected(search_pin_switch(SWITCH, 'ENTER')) is True:
            break
        else:
            time.sleep(0.1)
 
    # 비번변경 키 활성화
    event_enable(search_pin_switch(SWITCH, 'MODE'))

    # 노란불은 켜고 초록불 끄고
    led_onoff(search_pin_led(LED,'LED_Y'), ON)
    led_onoff(search_pin_led(LED,'LED_G'), OFF)

# 비번틀렸을 때
def lock_door(SWITCH, LED, locktime):
    time_count = 0

    # 모든 키 비활성화
    event_disable(search_pin_switch(SWITCH, 'MODE'))
    event_disable(search_pin_switch(SWITCH, 'ENTER'))

    # 노랑 LED는 끄자
    led_onoff(search_pin_led(LED,'LED_Y'), OFF)

    # 카메라 촬ㅋ영ㅋ
    # 일부러 비워놈
    pass

    # 빨간 LED를 마구 점멸시켜서 정신분산
    while(True):
	# LED 점멸: 0.1초당 1번
        if(time_count <= locktime):
            toggle_led(search_pin_led(LED,'LED_R'))

        # 시간 경과
        else:
            break

        time_count += 0.1
        time.sleep(0.1)

    # 경고 시간이 지났다면 Ready로 돌아감.
    led_onoff(search_pin_led(LED,'LED_R'), OFF)
    mode_ready(SWITCH, LED)

def change_pwd(SWITCH, LED):
    print('Set PASSWORD')
    pass

