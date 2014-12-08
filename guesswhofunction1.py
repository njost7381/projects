#this file contains all the functions required for guess who
import picamera,time
#Gets a picture of the user
def getPicture (name) :
    

        
    check=False
    while check == False:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024,768)
            camera.start_preview()

            time.sleep(2)
            camera.capture("{0}.jpeg")
            camera.stop_preview()
        correct=input("Your picture is called {0}.jpeg, is that correct?".format(name))
        if correct.lower () =="y" :
            check = True


