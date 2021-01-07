# speech-driven-keyboard-and-mouse
To avoid too much hand/wrist pain I decided to create a program that will convert voice to common keyboard actions - such as scrolling, mouse clicks, text input, etc. It is not intended to replace the keyboard and mouse, but rather to reduce their use. If you want to contribute please contact me. Custom parsers and ways to make speech recognition of commands more accurate / efficient of particular interest, though I'm open to any way the tool can be improved.

## Install

Several of the following instructions are specific to Ubuntu (sudo apt-get intall...) Every library used should function cross-platform, but it has only been tested on Linux. See also requirements.txt file.

- grab the latest version of the deepspeech pbmm file (https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3) and include in main project directory
- pip install pyautogui
- sudo apt-get install scrot python3-tk python3-dev (for pyautogui on Ubuntu)
- sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
- sudo apt-get install python3-pyaudio
- pip install deepspeech
- pip install pyaudio
- pip install numpy pyenchant

#### On Mac

- brew install portaudio
- brew install enchant
- pip install numpy pyenchant deepspeech pyautogui pyaudio

## Approach

- I wanted to use a speech recognition library that worked out-of-the-box and did not require retraining
- I decided to use deepspeech from Mozilla for speech-to-text because it is a) offline (unlike services such as Google's API), b) more accurate than offline alternatives such as CMU's PocketSphinx, c) entirely open source, unlike picovoice. I initially tried to use python's SR library with google (see srmodule_old folder), but found it too slow and, as mentioned before, requiring internet.
- Because deepspeech was not intended for this application, I had to use some workarounds. They are certainly not perfect, and any suggestions for improvement welcome. 

## Usage


#### Usage Notes

- make sure the input volume of your mic is turned up 
- when first starting, wait just a second for the program to adapt to ambient noise levels (the threshold is set above the max value of ambient noise levels on program start)
- you may need to repeat the very first command twice for it to be processed
- occassionally the model will inaccurately interpret a word - just repeat a command if it doesn't work the first time
- When I used a microphone with too high of a sample rate (48 kHz) I had some issues with the program freezing after it ran for a while and taking longer to process input - works fine at 16 kHz. Didn't track down the root source of this issue, so may not be an issue for you. The default model was trained at 16 kHz, so that is ideal. I currently use a headset mic and it works great. 
- you may need to enunciate certain words more than you are used to in everyday speech for them to be interpreted by the model correctly - trial and error is the best way to tell which words the model struggles with - additional context makes the model more accurate, so it does better on a wider variety of words in text mode (hence command words should be chosen carefully)

