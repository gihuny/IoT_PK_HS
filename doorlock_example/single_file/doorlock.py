import RPi.GPIO as GPIO
import time

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

# 초기화 함수
def init_gpios(SWITCH, LED):
    # input mode 설정 - 초기값은 PULL DOWN
    #GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_DOWN)
    for pin in SWITCH:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    
    for pin in LED:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# 이벤트 등록
def event_enable(pin):
    GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=200)

# 이벤트 해제
def event_disable(pin):
    GPIO.remove_event_detect(pin)

# 연결 확인
def check_gpios(SWITCH, LED):

    # input EVENT 등록: SWITCH pin들에 FALLING event가 발생하는지 확인한다.
    for pin in SWITCH:
        event_enable(pin)
   
    # main loop
    try:
        while True:
            time.sleep(1)
    
            for pin in SWITCH:
                if GPIO.event_detected(pin) is True:            
                    print('Event detected at %s\n' %SWITCH[pin]['color'])
     
            for pin in LED:
                GPIO_LVL = GPIO.input(pin)
                GPIO.output(pin, not GPIO_LVL)
    
            #number_of_times += 1
    
    except KeyboardInterrupt:
        pass

# 이름으로 pin 번호 찾는 함수
def search_pin_switch(SWITCH, NAME):
    for pin in SWITCH:
        if SWITCH[pin]['name'] == NAME: 
            return pin

def search_pin_led(LED, NAME):
    for pin in LED:
        if LED[pin] == NAME: 
            return pin

# LED 조작
def toggle_led(led_pin):
    led_state = GPIO.input(led_pin)
    GPIO.output(led_pin, not led_state)

def led_onoff(led_pin,onoff):
    GPIO.output(led_pin,onoff)

# 이벤트 발생 확인 - coding중 Test함수, 실사용 안함.
def check_events(SWITCH):
    while(True):
        for pin in SWITCH:
            if GPIO.event_detected(pin) is True:            
                print('Event detected at %s\n' %SWITCH[pin]['color'])

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

