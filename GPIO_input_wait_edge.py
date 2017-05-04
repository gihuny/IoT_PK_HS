# check here
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# for your information

# 5초간 SWITCH가 눌리길 기다리는 예제. 
# SWITCH가 눌리면 LED를 반전하고 눌리지 않으면 TIMEOUT이라고 출력한다.
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

# output mode 설정
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO_LVL = GPIO.LOW

#polling - wait for edge
try:
    while True:
        # Timeout에 적힌 ms만큼 SWITCH가 눌리길 기다림.
        event = GPIO.wait_for_edge(SWITCH, GPIO.RISING, timeout=5000)

        # Timeout되었다면 event에 None이 return됨.
        if event is None:	# if event == None:
            print('TIMEOUT')
        else:
            print('SWITCH LEVEL: %d', GPIO_LVL)
            GPIO.output(LED, GPIO_LVL)
            GPIO_LVL = ~GPIO_LVL;

	#see for chattering / debounce
	# 스위치가 여러번 bouncing하는것을 방지하기 위해 0.5초 기다린다.
        time.sleep(0.5)
       
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
