#import spidev
import time
import myspi
import RPi.GPIO as GPIO

#spi = spidev.SpiDev() # create SPI Class
#spi.open(0,0) # dev, port
#
#spi.max_speed_hz=100000
#spi.bits_per_word=8

PINLIST = { "CSN": 22, "CLK": 11, "MOSI": 13, "MISO": 15}
myspi.init(PINLIST)

dummy = 0xff
start = 0x47
sgl = 0x20
ch0 = 0x00
ch1 = 0x10
msbf = 0x8

def measure(ch):
#    ad = spi.xfer2( [ (start | sgl | ch | msbf), dummy] )
    ad = myspi.xfer( PINLIST, [ (start | sgl | ch | msbf), dummy] )
    val = (( ((ad[0] & 0x3) <<8) + ad[1] ) * 3.3) / 1023
    print("ch: %d rddata ad[0]: %x, ad[1]: %x, ad: %4d, calval: %f" % (ch>>4, ad[0], ad[1],( ((ad[0] & 0x3) << 8) | ad[1]), val))

    return val

try:
    while 1:
        mes_ch0 = measure(ch0)
        mes_ch1 = measure(ch1)
        print("ch0 - %2.2f [V] ch1 - %2.2f [V]" % (mes_ch0 , mes_ch1))

        time.sleep(1)

except KeyboardInterrupt:
    pass

#spi.close()
GPIO.cleanup()
