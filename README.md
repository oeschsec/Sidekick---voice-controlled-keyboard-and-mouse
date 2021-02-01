# Sidekick (speech driven keyboard and mouse)
To reduce hand/wrist pain from frequent computer use I decided to create a program that will convert voice to common keyboard/mouse actions in order to reduce clicks/keypresses. It is not intended to replace the keyboard and mouse, but rather to reduce their use, hence the name Sidekick. Sidekick handles transcription, mouse movement/click/wheel, and common commands. 

Sidekick is still very much a work in progress, but the sky is the limit. One of the more fun challenges has been controlling the mouse with only voice commands (see [user guide](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/userguide.md) for details). 

## Contributing

If you want to contribute, please first create an issue or send me an email and wait for me to give you the greenlight. Then use the [fork and pull model](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/forkandpull.md) to make your changes. 

## Install

- Download the vosk-model-en-us-daanzu-20200905-lgraph (129M) model folder from https://alphacephei.com/vosk/models, place in same directory as vosk_main.py, and rename the folder to 'model'. I used the smaller model because it was faster and responsiveness is important for this application. 
- pip install numpy vosk pyautogui pyaudio

#### On Mac

- brew install portaudio

#### On Ubuntu

- sudo apt-get install scrot python3-tk python3-dev (for pyautogui on Ubuntu)
- sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
- sudo apt-get install python3-pyaudio

## Usage

- python3 sidekick.py
- see the [user guide](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/userguide.md) for instructions on use

## Approach

- I wanted to use a speech recognition library that worked out-of-the-box and did not require retraining
- I wanted it to work offline and be fully open source
- I decided to use Vosk for speech-to-text because it is a) offline (unlike services such as Google's API), b) more accurate than offline alternatives such as CMU's PocketSphinx, c) entirely open source, unlike picovoice. I initially tried to use python's SR library with google (see srmodule_old folder), but found it too slow and, as mentioned before, requiring internet. I originally used Mozilla's deepspeech, but for this specific application it was less ideal than Vosk using default models.

## Vosk Documentation

- https://alphacephei.com/vosk/install (requirements for running vosk listed here)
- https://medium.com/analytics-vidhya/offline-speech-recognition-made-easy-with-vosk-c61f7b720215
- https://github.com/alphacep/vosk-api/blob/master/python/example/test_text.py
- https://alphacephei.com/vosk/
- https://alphacephei.com/vosk/adaptation#updating-the-language-model - update the language model to more heavily weight certain words

## Ideas / Notes

- faster speech recognition would help significantly (smaller vosk model helped)
- when in text mode, minimize the command words that still function
- if mouse started and you switch modes, the thread just keeps running - need to fix
- external usb sound card such as the Andrea PureAudio

## Related Projects & Articles 

I am aware of other interesting projects in this space. The benefit of this approach is that it is lightweight, fully open source, and does not require integration with dragon. 

- [dragonfly](https://github.com/dictation-toolbox/dragonfly), but for this application wanted to minimize dependencies and keep it simple
- https://github.com/dictation-toolbox/natlink
- https://talonvoice.com/
- [Caster](https://caster.readthedocs.io/en/latest/)
- fun [video](https://www.youtube.com/watch?v=8SkdfdXWYaI) of a guy who hacked dragon to code 
- https://medium.com/bambuu/state-of-voice-coding-2017-3d2ff41c5015
