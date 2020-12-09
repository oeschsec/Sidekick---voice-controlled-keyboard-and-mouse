import speech_recognition as sr
import time
from actions import *

# Name of the microphone you want to use (print them below to get correct value)
#micName = "Webcam C110: USB Audio (hw:1,0)"
micName = "default"

# Higher sample results in better audio / translation, but can slow down translation significantly 
sampleRate = 8000 #16000 #44100
chunkSize = 512

# A list of audio cards and microphones
mic_list = sr.Microphone.list_microphone_names()

# Set value of microphone
for i, microphone_name in enumerate(mic_list):
    print(microphone_name)
    if microphone_name == micName:
        devID = i

def callback(r,audio):
    try:
        text = r.recognize_google(audio)
        #text = r.recognize_sphinx(audio)
        words = text.split(' ')
        if words[0].lower() == "click":
            click()
        elif words[0].lower() == "hit":
            if words[1] == "enter": 
                hitEnter()
        elif words[0].lower() == "backspace":
            if len(words) > 1:
                backspace(words[1])
            else:
                backspace(1)
        elif words[0].lower() == "scroll":
            if words[1] == "up":
                if len(words) > 2:
                    if words[2] == "surf":
                        surfScrollUp(20)
                    else:
                        scrollUp(20)
                else:
                    scrollUp(10)
            elif words[1] == "down":
                if len(words) > 2:
                    if words[2] == "surf":
                        surfScrollUp(-20)
                    else:
                        scrollUp(-20)
                else:
                    scrollUp(-10)
        elif words[0].lower() == "stop":
            stop_listening(wait_for_stop=False)
        else:
            writeToScreen(text)
    except sr.UnknownValueError:
        pass # when silent this is thrown, so no use printing an error constantly
        #print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except Exception as e: 
        print("Exception occured: " + str(e))

r = sr.Recognizer()
m =  sr.Microphone(device_index = devID, sample_rate = sampleRate, chunk_size = chunkSize)
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

while True:
    time.sleep(1)