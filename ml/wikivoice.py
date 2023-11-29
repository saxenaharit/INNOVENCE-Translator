import pyttsx3
import wikipedia
import re
import long_responses as long
import speech_recognition as sr
from playsound import playsound
import pyttsx3
import gtts 
import os





def voiceq():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio=r.listen(source)
        try:
            speech_text=r.recognize_google(audio)
            print(speech_text)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print("Could not request result from google")
    engine=pyttsx3.init()
    voicw=pyttsx3.init()
    speech_text=speech_text+'?'
    #speech_text=input("Seach Anything")
    result=wikipedia.summary(speech_text,sentences=20)
    print (result)
    #engine.say(get_response(get_response(speech_text)))
         #speaks the response
    text=result
    sound=gtts.gTTS(text,lang="en")
    sound.save("welcomew.mp3")
    playsound("welcomew.mp3")
    #print('Bot:  ' + get_response(speech_text))
   # os.remove("welcomew.mp3")


voiceq()


 