# get info from the pico
direction = False
question = False
def hear():
    #based on microphone
    if(inputFromMicroPhone):
        question = True
    else:
        question = False
while True():
    if(not direction):
        drive(1)
    else:
        drive(2)
    if(question):
        if(input == "come"):
            direction = True
        elif(input == "stop"):
            direction = False
        elif(input == "hi"):
            wave()
        else:
            rng = math.randirange(0, 1)
            if(rng == 1):
                say("yes")
            else:
                say("no")
def say(text):
    if(text == "no"):
        speaker.play(1)
    else:
        speaker.play(2)
def drive(w):
    if(w == 1):
        motor1.on
        motor2.on
        motor3.off
        motor4.off
    else:
        directions = lookForHuman()
        if(directions == "left"):
            motor1.on
            motor2.on
        elif(directions == "foward"):
            motor1.on
            motor2.on
            motor3.on
            motor4.on
        elif(directions == "right"):
            motor3.on
            motor4.on
        else:
            motor1.on
            motor2.on
def lookForHuman():
    #however the camera i get works this is just a guess
    if(human is on left side of screen):
        return("left")
    elif(human is on right side of screen):
        return("right")
    elif(human is foward):
        return("foward")
def wave():
    for i in range(15):
        servo.rotate(90)
        sleep(100)
        servo.rotate(0)
        sleep(100)
            