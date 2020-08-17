import os
import speech_recognition as sr
import wolframalpha
import playsound
from gtts import gTTS
from selenium import webdriver

wolfram_id = "3X5UQU-TK9ULVQTVE"
request = "calculate lcm of 456 and 28"
app_id =  wolfram_id
client = wolframalpha.Client(app_id) 
indx = request.lower().split().index('calculate') 
query = request.split()[indx + 1:] 
res = client.query(' '.join(query)) 
answer = next(res.results).text 
print(answer)