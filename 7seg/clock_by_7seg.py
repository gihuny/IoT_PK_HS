import RPi.GPIO as GPIO
import time
import datetime

ON = GPIO.HIGH
OFF = GPIO.LOW

def control_segment(character, is_alphabet):
    if character > 9 :
        Segment_state = {OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF} # all off
    else :
        if character == 0 :
            Segment_state = [ON , ON , ON , ON , ON , ON , OFF, OFF]   # 0
        elif character == 1 :
            Segment_state = [OFF, ON , ON , OFF, OFF, OFF, OFF, OFF]   # 1
        elif character == 2 :
            Segment_state = [ON , ON , OFF, ON , ON , OFF, ON , OFF]   # 2
        elif character == 3 :
            Segment_state = [ON , ON , ON , ON , OFF, OFF, ON , OFF]   # 3
        elif character == 4 :
            Segment_state = [OFF, ON , ON , OFF, OFF, ON , ON , OFF]   # 4
        elif character == 5 :
            Segment_state = [ON , OFF, ON , ON , OFF, ON , ON , OFF]   # 5
        elif character == 6 :
            Segment_state = [ON , OFF, ON , ON , ON , ON , ON , OFF]   # 6
        elif character == 7 :
            Segment_state = [ON , ON , ON , OFF, OFF, OFF, OFF, OFF]   # 7
        elif character == 8 :
            Segment_state = [ON , ON , ON , ON , ON , ON , ON , OFF]   # 8
        elif character == 9 :
            Segment_state = [ON , ON , ON , ON , OFF, ON , ON , OFF]   # 9

    return Segment_state

def clock_onoff(on):
    GPIO.cleanup()

    if(on == False):
        print('GPIO Cleanedup!\n')
        return
 
    GPIO.setmode(GPIO.BOARD)
   
    SegSel = [31,35,33,37]
    Segment = {
         0: 11 ,#     'A'   : 11 ,
         1: 13 ,#     'B'   : 13 ,
         2: 38 ,#     'C'   : 38 ,
         3: 22 ,#     'D'   : 22 ,
         4: 32 ,#     'E'   : 32 ,
         5: 15 ,#     'F'   : 15 ,
         6: 40 ,#     "G"   : 40 ,
         7: 36 }#     'dot' : 36 }
    
    #initialize
    for pin in SegSel:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    for pin in Segment:
        GPIO.setup(Segment[pin], GPIO.OUT, initial=GPIO.LOW)
    
    try:
        while True:
            # get time and set appropreate database
            now = datetime.datetime.now()
    
            # convert to digits
            digit = [0,0,0,0]
            digit[0] = int(int(now.hour)/10)
            digit[1] = int(int(now.hour)%10)
            digit[2] = int(int(now.minute)/10)
            digit[3] = int(int(now.minute)%10)
    
            # time division display
            second_cnt = 0 # s
            time_resolution = 0.005
            while second_cnt < 1:
    	    # per segment display
                for i in range (0,4):
    
                    # select Segment
                    for j in range (0,4):
                        if j == i:
                            GPIO.output(SegSel[j], OFF)
                        else:
                            GPIO.output(SegSel[j], ON)
    
                    # display segment
                    segment_control = control_segment(digit[i], False)
                    for pincon in range(0,8): 
                        GPIO.output(Segment[pincon], segment_control[pincon])
    
    		# time multiplexing control
                    second_cnt += time_resolution
                    time.sleep(time_resolution)
      
    except KeyboardInterrupt:
        pass
        
    GPIO.cleanup()
    print('GPIO Cleanedup!\n')

if __name__ == "__main__":
    clock_onoff(True)
