import os
import speech_recognition as sr
import wolframalpha
import playsound
from gtts import gTTS
from selenium import webdriver

num = 1
shutdown = ["bye","nothing","sleep","shut up","exit"]

def winry_speaks(output):
    global num
    num += 1
    print("Winry : ",output)
    toSpeak = gTTS(text=output,lang="en-us",slow=False)
    file = str(num)+".mp3"
    toSpeak.save(file)

    playsound.playsound(file)
    os.remove(file)

def speech_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        #winry_speaks("What would you like me to do ? ")
        print("Speak....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=2)

    #winry_speaks("Okay, thats enough now.")

    try:
        winry_speaks("Gotcha ! ")
        text = r.recognize_google(audio,language="en-us")
        print("You :",text)
        print("Processing....")
        return text
    except:
        winry_speaks("I didn't quite get you, please repeat. ")
        return 0

def get_name():
    name = speech_to_text()
    if(name != 0):
        winry_speaks("Hello " + name )
        return name
    else:
        get_name()

def process_request(request):
    try:
        


if __name__=="__main__":

    winry_speaks("Hi my name is Winry, what is yours ? ")
    name = get_name()

    while(1):
        winry_speaks("What can i do for you today, "+name)
        request = speech_to_text()

        if(request == 0):
            winry_speaks("I didn't quite get you, please repeat. ")
            continue
        if(str(request.lower()) in shutdown):
            winry_speaks("Okay, I will "+str(request)+", "+name)
            break
        #print(request)
        process_request(request)
    





