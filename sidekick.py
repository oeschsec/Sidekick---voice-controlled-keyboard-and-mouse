from vosk import Model, KaldiRecognizer
import os
import json
from defaultparser import *
import audioop
import math
from parsepackage import *

if not os.path.exists("model"):
    # tested with vosk-model-en-us-aspire-0.2
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio

#wordlist = '["colon","mouse"]' # limit the words available to the model

parser = parser.Parser() # DefaultParser()
model = Model("model")
rec = KaldiRecognizer(model, 16000)
#rec = KaldiRecognizer(model, 16000, wordlist)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("\nSidekick at your service. Please wait silently for the threshold to be set based on ambient noise before use.")

threshold_buffer = 5 # how many dB above ambient noise threshold will be set
thresholdset = False # whether or not threshold has been set
threshcount = 0 # count that determines when threshold is set
ambientvals = [] # Ambient noise level in dB is used to calculate appropriate threshold at which to send audio to vosk
wait = False # after threshold breached, need to process the next 5-10 audio samples through the model even if they don't breach threshold 
waittime = 0 # when to toggle wait from True to False 
while True:
    # read in audio data
    data = stream.read(4000,exception_on_overflow = False)

    # calculate decibels
    dB = 20 * math.log10(audioop.rms(data,2))

    # we want to set threshold based on ambient noise prior to processing audio data
    if not thresholdset: 
        ambientvals.append(int(dB))
        threshcount += 1
        if threshcount >= 10:
            thresholdset = True
            print("Your sidekick now awaits your command.")
            threshold = sum(ambientvals) / len(ambientvals) + threshold_buffer
            print("Threshold is now set at " + str(round(threshold,2)) + " dB.")
    
    # send audio data to model for processing when threshold breached and shortly afterward
    elif dB > threshold or wait == True:

        waittime += 1
        if dB > threshold:
            waittime = 0
            wait = True

        if waittime >= 8: # in my testing max wait time before word sent to parser was 6 - added a bit of buffer 
            wait = False

        if len(data) == 0:
            break
        if rec.AcceptWaveform(data): # if this returns true model has determined best word candidate
            #print(type(rec.Result()))
            res = json.loads(rec.Result()) # this not only returns the most accurate result, but also flushes the list of words stored internally
            if res["text"] != "":
                for result in res["result"]:
                    #print(waittime)
                    parser.ingest(result["word"]) 
        else: # if false only a partial result returned - not useful for this application
            pass
            #print(rec.PartialResult()) - partial result is faster, but not accurate enough for use
