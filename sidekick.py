from vosk import Model, KaldiRecognizer
import os
import json
from defaultparser import *

if not os.path.exists("model"):
    # tested with vosk-model-en-us-aspire-0.2
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio

parser = DefaultParser()
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000,exception_on_overflow = False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        #print(type(rec.Result()))
        res = json.loads(rec.Result())
        if res["text"] != "":
            for result in res["result"]:
                parser.ingest(result["word"])
    else:
        pass
        #print(rec.PartialResult())