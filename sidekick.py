'''
Sidekick
Copyright (C) 2021 UT-Battelle - Created by Sean Oesch

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from errno import EHOSTDOWN
from black import wrap_stream_for_windows
from vosk import Model, KaldiRecognizer
import sys
import os
import json
import audioop
import string
import math
from parsepackage import *
from parsepackage.volume_parser import VolumeParser

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio
import json
import json

parser = parser.Parser() 

def listToList(words):
    wordlist = '['
    for word in words:
        wordlist = wordlist + "\"" + word + "\"" + ","
    wordlist = wordlist.strip(",") + "]"    
    return wordlist

def setRec(state,crec,trec,arec, prec):
    if state == "text":
        return trec
    elif state == "program":
        return prec
    elif state == "command" or state == "mouse" or state == "volume":
        return crec
    else:
        return arec 

def clearRec(crec,trec,arec,prec):
    crec.Result()
    trec.Result()
    arec.Result()
    prec.Result()

def stateSwap(nextstate,crec,trec,arec, prec):
    rec = setRec(nextstate,crec,trec,arec, prec)
    res = json.loads(rec.Result())
    swap = False
    if res["text"] != "":
        if swap:
            parser.ingest(res["text"]) 

        if res["text"] == nextstate:
            swap = True
    
    clearRec(crec,trec,arec,prec)

def ingest(currentstate,crec,trec,arec, prec):
    rec = setRec(currentstate,crec,trec,arec, prec)
    res = json.loads(rec.Result()) # this not only returns the most accurate result, but also flushes the list of words stored internally
    if res["text"] != "":
        for text in res["text"].split(" "):
            if text in ["text","alpha","command", "program"] and text != currentstate:
                parser.ingest(text)
                stateSwap(text,crec,trec,arec, prec)
            else:
                parser.ingest(text) 
    
    clearRec(crec,trec,arec, prec)

def load_config():
    f =open("sidekick.cfg")
    config = json.load(f)
    f.close()
    return config

config = load_config()

# Set the screen resolution for screenshots from config file
resolution = config['resolution'].split("x")
screen_size = (int(resolution[0]), int(resolution[1]))
print(screen_size)
parser.set_screen_size(screen_size)

# create wordlist for our command model so that commands will be more accurately detected
lower_buffer = 0
upper_buffer = 0
if len(sys.argv) >= 2:
    lower_buffer = sys.argv[1]

if len(sys.argv) >= 3: 
    upper_buffer = sys.argv[2]



commandwords = listToList(parser.nontextcommands)
alphavals = listToList(parser.alphavalues)

model = Model("model")
# the text recommender uses the standard model for transcription
textrec = KaldiRecognizer(model, 16000)
programrec = KaldiRecognizer(model, 16000)
# use wordlist in our command recommender
commandrec = KaldiRecognizer(model, 16000, commandwords)
alpharec = KaldiRecognizer(model, 16000, alphavals)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
parser.set_audio_stream(stream)
print("\nSidekick at your service. Please wait silently for the threshold to be set based on ambient noise before use.")

threshold_buffer = 1 # how many dB above ambient noise threshold will be set
thresholdset = False # whether or not threshold has been set
threshcount = 0 # count that determines when threshold is set
ambientvals = [] # Ambient noise level in dB is used to calculate appropriate threshold at which to send audio to vosk
wait = False # after threshold breached, need to process the next 5-10 audio samples through the model even if they don't breach threshold 
waittime = 0 # when to toggle wait from True to False 
while True:
    # read in audio data
    data = stream.read(4000,exception_on_overflow = False)

    # calculate decibels
    dB = 20 * math.log10(audioop.rms(data,2)+1)

    # we want to set threshold based on ambient noise prior to processing audio data
    if not thresholdset: 
        ambientvals.append(int(dB))
        threshcount += 1
        if threshcount >= 10:
            thresholdset = True
            print("Your sidekick now awaits your command.")
            threshold = sum(ambientvals) / len(ambientvals) + threshold_buffer
            print("Threshold is now set at " + str(round(threshold,2)) + " dB.")
            parser.set_threshold(threshold)
        

    # send audio data to model for processing when threshold breached and shortly afterward
    elif dB > threshold or wait == True:

        waittime += 1
        if dB > threshold:
            waittime = 0
            wait = True

        if waittime >= 8: # in my testing max wait time before word sent to parser was 6 - added a bit of buffer 
            wait = False

        trec = textrec.AcceptWaveform(data)
        prec = programrec.AcceptWaveform(data)
        crec = commandrec.AcceptWaveform(data)
        arec = alpharec.AcceptWaveform(data)
        if len(data) == 0:
            break
        print(parser.state)
        if parser.state == "text":
            if trec: # if this returns true model has determined best word candidate
                ingest(parser.state,commandrec,textrec,alpharec, programrec) 
            else: # if false only a partial result returned - not useful for this application
                pass
                #print(rec.PartialResult()) - partial result is faster, but not accurate enough for use
              
        elif parser.state == "program":
            if prec: # if this returns true model has determined best word candidate
                ingest(parser.state,commandrec,textrec,alpharec,programrec) 
            else: # if false only a partial result returned - not useful for this application
                pass

        elif parser.state == "alpha":
            if arec: # if this returns true model has determined best word candidate
                ingest(parser.state,commandrec,textrec,alpharec, programrec)                 
        
        elif parser.state == "volume":
            #ingest(parser.state,commandrec,textrec,alpharec,programrec) 
            if parser.volumeParser.volumeStarted == True:
                parser.dB = dB
                
                lower_threshold = threshold + float(lower_buffer)
                upper_threshold = 50 + float(upper_buffer)

                parser.volumeParser.thresh.append(lower_threshold)
                parser.volumeParser.thresh.append((upper_threshold-lower_threshold) + lower_threshold)
                parser.volumeParser.thresh.append(upper_threshold)

                parser.volumeParser.evaluate_volume(parser.command_buffer, parser.dB)
                ingest(parser.state,commandrec,textrec,alpharec, programrec)   
                
                if parser.volumeParser.stopVolume == True:
                    parser.state = "command"  

        elif parser.state == "horizontal":
            if parser.horizontalParser.volumeStarted == True:
                if dB < 35:
                    y = parser.horizontalParser.setVolumeCoord(180)
                elif dB >= 35:
                    parser.horizontalParser.setVolumeCoord(0)
                    command_buffer = []
                

        else:
            if crec: # if this returns true model has determined best word candidate
                ingest(parser.state,commandrec,textrec,alpharec, programrec) 


