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

    rot = (int)(input('Select Rotation: 1:90, 2:180, 3:270, else:No rotation'))

    if rot is 3:
        camera.rotation = 270
    elif rot is 2:
        camera.rotation = 180
    elif rot is 1:
        camera.rotation = 90

    filename = input("Enter Filename")
    
#    camera.start_preview()
#    time.sleep(1)
#    camera.stop_preview()
#    camera.capture(filename+".jpg")

    camera.start_preview()
    camera.start_recording(output = filename + '.h264')
    camera.wait_recording(5)
    camera.stop_preview()
    camera.stop_recording()
