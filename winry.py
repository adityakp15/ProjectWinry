import os
import sys
import speech_recognition as sr
import wolframalpha
import playsound
from gtts import gTTS
from selenium import webdriver

wolfram_id = "3X5UQU-TK9ULVQTVE"
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
        audio = r.listen(source,phrase_time_limit=5)

    #winry_speaks("Okay, thats enough now.")

    try:
        winry_speaks("Gotcha ! ")
        text = r.recognize_google(audio,language="en-us")
        print("You :",text)
        print("Processing....")
        return text
    except:
        winry_speaks("I didn't quite get you, so i'll call you 0. ")
        return "0"

def get_name():
    name = speech_to_text()
    if(name != "0"):
        winry_speaks("Hello " + name )
        return name
    else:
        get_name()

def process_request(request,name):
    try:
        if("search" in request or "play" in request):
            search_web(request)
            return
        elif("calculate" in request.lower()):
            app_id =  wolfram_id
            client = wolframalpha.Client(app_id) 
  
            indx = request.lower().split().index('calculate') 
            query = request.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            winry_speaks("The answer is " + answer) 
            return
        else: 
            winry_speaks("I can search the web for you, Do you want to continue?") 
            ans = speech_to_text() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(request) 
            else: 
                return
    except : 
  
        winry_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = speech_to_text() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(request) 

def search_web(request):

    driver = webdriver.Firefox() 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'youtube' in request.lower(): 
        winry_speaks("Opening in youtube") 
        indx = request.lower().split().index('youtube') 
        query = request.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query)) 
        return
    elif 'wikipedia' in request.lower(): 
        winry_speaks("Opening Wikipedia") 
        indx = request.lower().split().index('wikipedia') 
        query = request.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
    else: 
        if 'google' in request: 
            indx = request.lower().split().index('google') 
            query = request.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q=" + '+'.join(query)) 
        elif 'search' in request: 
            indx = request.lower().split().index('google') 
            query = request.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q=" + '+'.join(query)) 
        else: 
            driver.get("https://www.google.com/search?q=" + '+'.join(request.split())) 
  
        return


if __name__=="__main__":

    winry_speaks("Hi my name is Winry, what is yours ? ")
    name = get_name()
    while(1):
        winry_speaks("What can i do for you today, "+name)
        request = speech_to_text()

        if(request == "0"):
            winry_speaks("I didn't quite get your name, please repeat. ")
            continue
        elif(str(request.lower()) in shutdown):
            winry_speaks("Goodbye, "+name)
            sys.exit()
        process_request(request,name)
    



