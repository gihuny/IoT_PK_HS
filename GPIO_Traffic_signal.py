import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# variable set
# 변수설정
RED = 11
YELLOW = 13
GREEN = 15

SWITCH = 40

on = GPIO.HIGH
off = GPIO.LOW

red_duration = 5
yellow_duration = 1
green_duration = 10
green_blink_duration = 5
green_blink_interval = 1


# initial value for GPIO
# GPIO 초기세팅
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_DOWN)

#invoke event
#event 등록
GPIO.add_event_detect(SWITCH, GPIO.RISING, bouncetime=200)

try:
    while True:

        # RED SIGNAL ON
	# 빨간신호
        GPIO.output(RED, on)
        GPIO.output(GREEN, off)
        #time.sleep(5)
        #time.sleep(red_duration)		#red_duration = 5

        GPIO.event_detected(SWITCH)             #이전에 발생한 event를 제거

	# 총 5초간 1초에 한번씩 SWITCH가 눌렸었는지 확인하여 눌렸으면 바로 진행
        for i in range(red_duration):
            time.sleep(1)
            if GPIO.event_detected(SWITCH) is True:
                break

	# YELLOW SIGNAL ON
	# 노랑신호
        GPIO.output(RED, off)
        GPIO.output(YELLOW, on)
        #time.sleep(1)
        time.sleep(yellow_duration)		#yellow_duration = 1

	# GREEN SIGNAL ON
	# 녹색신호
        GPIO.output(YELLOW, off)
        GPIO.output(GREEN, on)
        #time.sleep(10)

        for i in range(green_duration):
            print((green_duration - i))

	    # GREEN SIGNAL BLINKING after 5 seconds
	    # 5초 이후라면 녹색 깜빡임
            if (green_duration - i) <= green_blink_duration:
                GPIO.output(GREEN, off)
            #time.sleep(0.5)
            time.sleep(green_blink_interval / 2)
            GPIO.output(GREEN, on)
            #time.sleep(0.5)
            time.sleep(green_blink_interval / 2)

except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
