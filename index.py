import speech_recognition as sr # needs install via pip
import math # needed for the randirange feature

recognizer = sr.Recognizer() # init

def getAudio(): 
    with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio) # Uses google to recognize audio. Needs wifi connection to do so. 

    return text # might result in error if something comes up. 
    
# get info from the pico
direction = False
question = False


while True():
    
    if(not direction):
        # Move forward
    else:
        # Don't Move?
        
    try:
        input == getAudio()
        print(input)
    except Exception as Exc:
        print("Most likly nothing heard")
        
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
        # Speaker play sound
    else:
        # Speaker play higher sound.
        
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

            # here you are going to want moter 3 and 4 going in a -w direction.
        
        elif(directions == "foward"):
            motor1.on
            motor2.on
            motor3.on
            motor4.on

            
        elif(directions == "right"):
            motor3.on
            motor4.on

            # here you are going to want moter 1 and 2 move in a -w direction
        else:
            motor1.on
            motor2.on

            # as above, you are going to want moter 3 and 4 going in a -w direction. 

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
            
