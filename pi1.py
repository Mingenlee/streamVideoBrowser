import time
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # At this point the image is available as stream.array
        print('Captured %dx%d image' % (stream.array.shape[1], stream.array.shape[0]))
        frame = stream.array
        cv2.imshow('image', frame)
        cv2.imwrite('/home/pi/wrk/images/1.png', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()