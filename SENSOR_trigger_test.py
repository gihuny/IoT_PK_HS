# 1초마다 40번 PIN의 GPIO 값을 읽어서 출력하는 예제
import RPi.GPIO as GPIO
import time

# PIN 표기방식 설정
GPIO.setmode(GPIO.BOARD)

# 스위치와 LED PIN 번호를 각각 읽기 좋게 변수에 할당
DETECT = 40
RED = 11
GREEN = 13

on = GPIO.HIGH
off = GPIO.LOW

# input mode 설정 - 초기값은 PULL DOWN
GPIO.setup(DETECT, GPIO.IN, GPIO.PUD_DOWN)

# output mode 설정
GPIO.setup(RED, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)


##event based
# input EVENT 등록: DETECT PIN에 RIGING event가 발생하는지 확인한다.
GPIO.add_event_detect(DETECT, GPIO.RISING, bouncetime=200)

# timer
DETECT_IN_LVL = GPIO.LOW
time_elapsed = 0

try:
    while True:
        # DETECT의 값을 읽어서 DETECT_IN_LVL 변수에 할당
        DETECT_IN_LVL_P = DETECT_IN_LVL
        DETECT_IN_LVL = GPIO.input(DETECT)
        if DETECT_IN_LVL is not DETECT_IN_LVL_P:
            time_elapsed = 0
        else:
            time_elapsed += 1

        # LOW면 LOW라고 출력하고 LED를 끈다
        if DETECT_IN_LVL==0:
            print('INPUT LEVEL: LOW,   time_elasped: %s sec' %time_elapsed)
            sleep_time = 1 #ms

        # 아니면 HIGH라고 출력하고 LED를 켠다
        else:
            print('INPUT LEVEL: HIGH,   time_elasped: %s sec' %time_elapsed)
            sleep_time = 0.1 #ms

        #time.sleep(0.01)
        #time.sleep(1)
        sleep_dur = 0
        while sleep_dur <= 1:
            GPIO.output(RED,on)
            GPIO.output(GREEN,off)
            time.sleep(sleep_time/2)
            #time.sleep(1)
            GPIO.output(RED,off)
            GPIO.output(GREEN,on)
            time.sleep(sleep_time/2)
            #time.sleep(1)
            sleep_dur += sleep_time
       
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
