# Sidekick (speech driven keyboard and mouse)
To avoid too much hand/wrist pain I decided to create a program that will convert voice to common keyboard actions - such as scrolling, mouse clicks, text input, etc. It is not intended to replace the keyboard and mouse, but rather to reduce their use, hence the name Sidekick. If you want to contribute please contact me. 

## Install

- Download the vosk-model-en-us-aspire-0.2 model folder from https://alphacephei.com/vosk/models, place in same directory as vosk_main.py, and rename the folder to 'model'
- pip install numpy vosk pyautogui pyaudio

#### On Mac

- brew install portaudio

#### On Ubuntu

- sudo apt-get install scrot python3-tk python3-dev (for pyautogui on Ubuntu)
- sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
- sudo apt-get install python3-pyaudio

## Usage

- python3 sidekick.py

## Approach

- I wanted to use a speech recognition library that worked out-of-the-box and did not require retraining
- I wanted it to work offline and be fully open source
- I decided to use Vosk for speech-to-text because it is a) offline (unlike services such as Google's API), b) more accurate than offline alternatives such as CMU's PocketSphinx, c) entirely open source, unlike picovoice. I initially tried to use python's SR library with google (see srmodule_old folder), but found it too slow and, as mentioned before, requiring internet. I originally used Mozilla's deepspeech, but for this specific application it was less ideal than Vosk using default models.

## Vosk Documentation

- https://medium.com/analytics-vidhya/offline-speech-recognition-made-easy-with-vosk-c61f7b720215
- https://github.com/alphacep/vosk-api/blob/master/python/example/test_text.py
- https://alphacephei.com/vosk/
