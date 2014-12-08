#this file contains all the functions required for guess who
import picamera,time
#Gets a picture of the user

def getPicture(name) :
    try:
        check=False
        while check == False:
            with picamera.PiCamera() as camera:
                camera.resolution = (1024,768)
                camera.start_preview()

                time.sleep(2)
                filename = "{0}.jpeg".format(name)
                camera.capture(filename)
                camera.stop_preview()
            correct=input("Is this picture good?")
            if correct.lower () =="y" :
                check = True
            response = ""
            while not(response in["y"]):
                respone = input
                
    except picamera.exc.PiCameraMMALError:
        print("camera  not detected, please reconnect and restart")
        filename=""
    return filename

def getCharProfile() :
    name = ""
    name = input("What is your name?")
    filename = getPicture(name)
    hair = ""
    while not(hair in ["black","brown","blonde","ginger"]):
        hair = input("what is your hair colour?")
    glasses = ""
    while not(glasses in["yes","no","y","n"]):
        glasses = input("do you have glasses?")
    gender = ""
    while not(gender in["male","female","m","f","other"]):
        gender = input("Are you male, female or other?")
    hat = ""
    while not(hat in["yes","no","y","n"]):
        hat = input("are you wearing a hat?")
    eyecolour =""
    while not(eyecolour in["blue","green","red","brown"]):
        eyecolour = input("what is your eye colour?")
    return[name,hair,glasses,gender,hat,eyecolour]

                    


