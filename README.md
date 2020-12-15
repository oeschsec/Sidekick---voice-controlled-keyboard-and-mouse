# speech-driven-keyboard-and-mouse
To avoid too much wrist pain I decided to create an app that will convert voice to common keyboard actions - such as scrolling, mouse clicks, text input, etc. If you want to contribute please contact me. 

- grab the latest version of the deepspeech pbmm file (https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3)

## Install

- pip install pyautogui
- sudo apt-get install scrot python3-tk python3-dev
- sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
- sudo apt-get install python3-pyaudio
- pip install SpeechRecognition
- pip install pyaudio

## For Offline Speech Recognition

In my testing pocketsphinx didn't work so well - very inaccurate. 

- sudo apt-get install swig
- sudo apt-get install libpulse-dev
- sudo apt-get install -y python-pocketsphinx
- python -m pip install --upgrade pip setuptools wheel
- pip install --upgrade pocketsphinx

