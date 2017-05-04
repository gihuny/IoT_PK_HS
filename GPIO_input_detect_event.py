# check here
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# for your information

# input event를 등록하고 확인, 마지막으로 제거하는 예제
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

# PIN 표기방식 설정
GPIO.setmode(GPIO.BOARD)

# 스위치와 LED PIN 번호를 각각 읽기 좋게 변수에 할당
SWITCH = 40
LED = 11

# input mode 설정 - 초기값은 PULL DOWN
GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO_LVL = GPIO.LOW

##event based
# input EVENT 등록: SWITCH PIN에 RIGING event가 발생하는지 확인한다.
GPIO.add_event_detect(SWITCH, GPIO.RISING, bouncetime=200)

# 변수초기화
number_of_times = 0

#time sleep example
try:
    while True:
        global number_of_times
        #invoke chattering
        #time.sleep(5)
        time.sleep(1)
        print(number_of_times)

        # 5번 event가 등록되었다면 event를 제거한다.
        if number_of_times is 5:
            GPIO.remove_event_detect(SWITCH)
                
        # elif 는 else if이다.
        # SWITCH에 event가 발생한 적이 있으면 (눌린적이 있으면)  실행한다. 
        #if GPIO.event_detected(SWITCH) == True:
        elif GPIO.event_detected(SWITCH) is True:            
            if GPIO_LVL is GPIO.LOW:
                print('Set SWITCH LEVEL: LOW->HIGH\n')
            else:
                print('Set SWITCH LEVEL: HIGH->LOW\n')
            GPIO.output(LED, GPIO_LVL)
            GPIO_LVL = ~GPIO_LVL;
            number_of_times += 1

	# 눌리지 않았다면 아무것도 하지 않는다
        else:
            pass

except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
