import picamera
import time

with picamera.PiCamera() as camera:
    res = (int)(input('Select Resolution: 1:320x240, 2:640x480, 3:1024x768'))

    if res is 3:
        camera.resolution = (1024, 768)
    elif res is 2:
        camera.resolution = (640, 480)
    elif res is 1:
        camera.resolution = (320, 240)
    else:
        camera.resolution = (1024, 768)

    eff = (int)(input('Select Effect: 1:None, 2:oilpaint, 3:negative'))

    if eff is 3:
        camera.image_effect = 'negative'
    elif eff is 2:
        camera.image_effect = 'oilpaint'
    else:
        camera.image_effect = 'none'

    filename = input("Enter Filename")

    tm = time.localtime()

    camera.start_preview()
    time.sleep(3)
    camera.stop_preview()
    camera.capture(filename+(str)(tm.tm_year)+'_'+(str)(tm.tm_mon)+'_'+(str)(tm.tm_mday)+'_'+(str)(tm.tm_hour)+'_'+(str)(tm.tm_min)+'_'+(str)(tm.tm_sec)+".jpg")
    #camera.capture(filename+".jpg")
