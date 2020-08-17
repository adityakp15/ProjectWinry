import os
import speech_recognition as sr
import wolframalpha
import playsound
from gtts import gTTS
from selenium import webdriver

def search_web(request):

    driver = webdriver.Firefox() 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'youtube' in request.lower(): 
  
        indx = request.lower().split().index('youtube') 
        print(indx)
        query = request.split()[indx + 1:] 
        print(query)
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        print("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
  
    elif 'wikipedia' in request.lower(): 
  
        indx = request.lower().split().index('wikipedia') 
        query = request.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
  
    else: 
  
        if 'google' in request: 
  
            indx = request.lower().split().index('google') 
            query = request.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in request: 
  
            indx = request.lower().split().index('google') 
            query = request.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(request.split())) 
  
        return

request = "youtube messi"

search_web(request)

