# 1초마다 40번 PIN의 GPIO 값을 읽어서 출력하는 예제
import RPi.GPIO as GPIO
import time

# PIN 표기방식 설정
GPIO.setmode(GPIO.BOARD)

# 스위치와 LED PIN 번호를 각각 읽기 좋게 변수에 할당
SWITCH = 40
LED = 11

# input mode 설정 - 초기값은 PULL DOWN
GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_DOWN)

# output mode 설정
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        # SWITCH의 값을 읽어서 SWITCH_IN_LVL 변수에 할당
        SWITCH_IN_LVL = GPIO.input(SWITCH)

        # LOW면 LOW라고 출력하고 LED를 끈다
        if SWITCH_IN_LVL==0:
            GPIO.output(LED, GPIO.LOW)
            print('SWITCH LEVEL: LOW')

        # 아니면 HIGH라고 출력하고 LED를 켠다
        else:
            GPIO.output(LED, GPIO.HIGH)
            print('SWITCH LEVEL: HIGH')

        #time.sleep(0.01)
        time.sleep(1)
       
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
