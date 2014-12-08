import RPi.GPIO as GP , time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

def da():
    GP.output(11,GP.HIGH)
    time.sleep(1)
    GP.output(11,GP.LOW)
    time.sleep(0.5)
def dt():
    GP.output(11,GP.HIGH)
    time.sleep(0.5)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

def morse(letter) :
    if letter=='a':
            dt()
            da()
            print("a")
    elif letter =="b":
            da()
            dt()
            dt()
            dt()
    elif letter=="c":
            da()
            dt()
            da()
            dt()
    elif letter=="d":
            da()
            dt()
            dt()
    elif letter=="e":
            dt()
    elif letter=="f":
            dt()
            dt()
            da()
            dt()
    elif letter=="g":
            da()
            da()
            dt()
    elif letter=="h":
            dt()
            dt()
            dt()
            dt()
    elif letter=="i":
            dt()
            dt()
    elif letter=="j":
            dt()
            da()
            da()
            da()
    elif letter=="k":
            da()
            dt()
            da()
    elif letter=="l":
            dt()
            da()
            dt()
            dt()
    elif letter=="m":
            da()
            da()
    elif letter=="n":
            da()
            dt()
    elif letter=="o":
            da()
            da()
            da()
    elif letter=="p":
            dt()
            da()
            da()
            dt()
    elif letter=="q":
            da()
            da()
            dt()
            da()
    elif letter=="r":
            dt()
            da()
            dt()
    elif letter=="s":
            dt()
            dt()
            dt()
    elif letter=="t":
            da()
    elif letter=="u":
            dt()
            dt()
            da()
    elif letter=="v":
            dt()
            dt()
            dt()
            da()
    elif letter=="w":
            dt()
            da()
            da()
    elif letter=="x":
            da()
            dt()
            dt()
            da()
    elif letter=="y":
            da()
            dt()
            da()
            da()
    elif letter=="z":
            da()
            da()
            dt()
            dt()
letter = input ("what letter do you want to flash?")
morse(letter)
    
