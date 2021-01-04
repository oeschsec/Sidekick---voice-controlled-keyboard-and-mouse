import deepspeech
import numpy as np
import os
import pyaudio
import time
from defaultparser import *
import enchant
import math
import struct
import audioop

d = enchant.Dict("en_US") # using enchant to verify word is actually English before passing it to parser

# Configure deepspeech parameters and instantiate model
DEEPSPEECH_MODEL_DIR = './'
MODEL_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'graph.pbmm')
BEAM_WIDTH = 500
model = deepspeech.Model(MODEL_FILE_PATH)#, BEAM_WIDTH)
model.setBeamWidth(BEAM_WIDTH)

# Create a Streaming session
context = model.createStream()
parser = DefaultParser()

# Currently threshold is automatically set to 
# Test by uncommenting print(dB) in process_audio function and running program while remaining silent
threshold = 55 # decibels above which we record
threshold_buffer = 2 # dB above ambient noise required to process audio (too high and you have to talk loud, too low and may process too much ambient noise)

# Handle callback from PyAudio - feed audio data to deespeech model and send to parser
ambientvals = []
thresholdset = False # Set threshold once on start
lastlength = 0 # Ensures we only pull new words from intermediate decode (don't pass same thing to parser twice)
waittoflush = 0 # After threshold breached need to wait to flush several cycles or else model will not be able to decode speech
silentcount = 0 # Clear stream (if not already cleared) after silentcount reaches certain value
cleared = True # Periodically clear the stream and recreate for smoth operation
wait = False # Need to feed additional audio data so that intermediate decode returns meaningful result 
flush = False # Enough input data to flush (intermediateDecode) and safely use the resultant string
firstfeed = True # The stream needs to be fed multiple times on first feed to get result
def process_audio(in_data, frame_count, time_info, status):
    global lastlength
    global waittoflush 
    global wait
    global flush
    global context
    global silentcount
    global cleared 
    global firstfeed
    global thresholdset
    global threshold
    global ambientvals
    dB = 20 * math.log10(audioop.rms(in_data,2))
    #print(dB) #- check dB level of silence
    
    if not thresholdset:
        ambientvals.append(int(dB))

    if silentcount == 15 and not thresholdset:
        thresholdset = True
        threshold = max(ambientvals) + threshold_buffer
        print("Threshold is now set at " + str(threshold))
        print("The speech driven keyboard now awaits your command")

    data16 = np.frombuffer(in_data, dtype=np.int16)
    if dB < threshold and wait == False:
        silentcount += 1

    # After extended period of silence, clear the stream and recreate so that it doesn't start to consume undesirable amounts of memory
    if silentcount > 150 and cleared == False:
        context.freeStream()
        context = model.createStream()
        cleared = True
        firstfeed = True
        lastlength = 0 # reset 

    # if sound above threshold or we are waiting to flush 
    if dB > threshold or wait == True and thresholdset:
        silentcount = 0 # reset silent count whenever sound crosses threshold
        cleared = False 
        waittoflush += 1
        if dB > threshold:
            waittoflush = 0
            wait = True

        if waittoflush >= 10: # 10 was chosen because it worked - can be tweaked
            wait = False
            flush = True

        data16 = np.frombuffer(in_data, dtype=np.int16) # get our audio data into right format

        if firstfeed: # on first feed have to feed multiple times for model to process
            firstfeed = False
            for i in range(0,10):
                context.feedAudioContent(data16)
        else:
            context.feedAudioContent(data16)

        if flush:
            # running this twice helped with accuracy
            text = context.intermediateDecode()
            text = context.intermediateDecode()
            flush = False

            # now we decide which words to pass to the parser
            vals = text.split(' ')
            if len(vals) > 0 and text != '':
                diff = len(vals) - lastlength
                if diff > 0:
                    for word in vals[-diff:]:
                        if word != "" and word != None:
                            if word != "go" and word != "co" and d.check(word):
                                parser.ingest(word)
                        lastlength += 1
                text_so_far = text
          
    return (in_data, pyaudio.paContinue)

# PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1024

# Feed audio to deepspeech in a callback to PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE,
    stream_callback=process_audio
)

print("\nPlease wait silently for the threshold to be set based on ambient noise before use")
stream.start_stream()

try: 
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    # PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('\nThank you for using the speech driven keyboard. Have a nice day.')
    # DeepSpeech
    context.finishStream()