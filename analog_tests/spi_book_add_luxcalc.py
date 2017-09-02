import spidev
import time
from light_sensor import *

spi = spidev.SpiDev() # create SPI Class
spi.open(0,0) # dev, port

#spi.max_speed_hz=100000
spi.max_speed_hz=10000
spi.bits_per_word=8

dummy = 0xff
start = 0x47
sgl = 0x20
ch0 = 0x00
ch1 = 0x10
msbf = 0x8

def measure(ch):
    ad = spi.xfer2( [ (start | sgl | ch | msbf), dummy] )
    ad_int = ( ((ad[0] & 0x3) <<8) + ad[1] )
    val = (( ((ad[0] & 0x3) <<8) + ad[1] ) * 3.3) / 1023
    print("ch: %d rddata ad[0]: %x, ad[1]: %x, ad: %4d, calval: %f" % (ch>>4, ad[0], ad[1],( ((ad[0] & 0x3) << 8) | ad[1]), val))

    rval = [val, ad_int]

#    return val
    return rval

try:
    while 1:
        [mes_ch0,bin_ch0]  = measure(ch0)
        [mes_ch1,bin_ch1] = measure(ch1)
        lux_ch0 = adcout_to_lux(bin_ch0)
        lux_ch1 = adcout_to_lux(bin_ch1)

        print("ch0 - %2.2f [V] ch1 - %2.2f [V]" % (mes_ch0 , mes_ch1))
        print("ch0 - %2.2f [LUX], %s ch1 - %2.2f [LUX] %s" % (lux_ch0, lux_lut(lux_ch0), lux_ch1, lux_lut(lux_ch1)))

        time.sleep(1)

except KeyboardInterrupt:
    pass

spi.close()
