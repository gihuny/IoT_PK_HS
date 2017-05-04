## GPIO output - LED 출력이 깜빡이는 예제

import RPi.GPIO as GPIO
import time

# PIN 형식 설정
GPIO.setmode(GPIO.BOARD)

# PIN 번호를 읽기 편한 변수로 할당
LED = 11

# GPIO 레벨이라는 변수에 초기값 설정
GPIO_LVL = GPIO.LOW

# GPIO PIN 설정, (PIN번호, 출력모드, 초기값=GPIO.LOW)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(LED, GPIO_LVL)
#        time.sleep(0.001)
        time.sleep(0.5)
        GPIO_LVL = ~GPIO_LVL #현재값을 반전

except KeyboardInterrupt:

    pass
    
GPIO.cleanup()
print('GPIO Cleanedup!\n')
