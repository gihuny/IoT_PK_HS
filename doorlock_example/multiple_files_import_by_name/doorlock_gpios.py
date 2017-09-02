import RPi.GPIO as GPIO
import time

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

# 연결 확인 - board 검사용
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

