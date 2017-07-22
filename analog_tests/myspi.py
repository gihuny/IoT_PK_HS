import RPi.GPIO as GPIO
import time

def init(PINLIST):
   GPIO.cleanup()
   GPIO.setmode(GPIO.BOARD)
#   CSN = 22
#   CLK = 11
#   MISO = 13
#   MOSI = 15

   GPIO.setup(PINLIST["CSN"], GPIO.OUT)
   GPIO.setup(PINLIST["CLK"], GPIO.OUT)
   GPIO.setup(PINLIST["MOSI"], GPIO.OUT)
   GPIO.setup(PINLIST["MISO"], GPIO.IN, GPIO.PUD_UP)

   GPIO.output(PINLIST["CSN"], GPIO.HIGH)
   GPIO.output(PINLIST["CLK"], GPIO.LOW)
   GPIO.output(PINLIST["MOSI"], GPIO.LOW)

def xfer(PINLIST,bytelist):
   val = [0x0, 0x0]
   #print("%x %x" %(bytelist[0], bytelist[1]))

   # Set CSN LOW
   GPIO.output(PINLIST["CSN"], GPIO.LOW)
   #print(PINLIST["CSN"], GPIO.LOW)

   for i in range(0,2):
      for j in range(0,8):
         #prepare data
         #print(i, (bytelist[i] & (0x1<<j)))
         if( (bytelist[i] & (0x1<<(7-j))) == 0x0):
            outval = GPIO.LOW
         else:
            outval = GPIO.HIGH
         #print("bytelist[%d]: %x, j: %d, %x" % (i, bytelist[i], j, outval) )
         GPIO.output(PINLIST["MOSI"], outval)
         #print(PINLIST["MOSI"], outval)

         #clk 0->1
         GPIO.output(PINLIST["CLK"], GPIO.HIGH)
         #print("CLK 0->1")
         time.sleep(0.001)

	 # getdata
         val[i] = val[i]<<1
#         inval = GPIO.input(PINLIST["MISO"])
#         val[i] = val[i] | inval
         val[i] = val[i] | GPIO.input(PINLIST["MISO"])
         #print("inval %x val %x" %(inval, val[i]))

	 #clk 1->0
         GPIO.output(PINLIST["CLK"], GPIO.LOW)
         #print("CLK 1->0")

   # End of Transfer
   GPIO.output(PINLIST["CSN"], GPIO.HIGH)
   #print(PINLIST["CSN"], GPIO.HIGH)

   return val
#   return [0xff, 0xff]
        



