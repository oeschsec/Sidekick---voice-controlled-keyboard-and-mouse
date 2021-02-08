# Sidekick (voice controlled keyboard and mouse)
To reduce hand/wrist pain from frequent computer use I decided to create a program that will convert voice to common keyboard/mouse actions in order to reduce clicks/keypresses. It is not intended to replace the keyboard and mouse, but rather to reduce their use, hence the name Sidekick. Sidekick handles transcription, mouse movement/click/wheel, and common commands. 

Sidekick is still very much a work in progress, but the sky is the limit. One of the more fun challenges has been controlling the mouse with only voice commands (see [user guide](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/userguide.md) for details). 

## Why use Sidekick?

Sidekick was created with the goal of being general purpose, lightweight, extensible, and easy to use. It works offline and cross-platform. While some other tools (listed below) specialize in voice coding and entirely replacing the keyboard and mouse in specific application contexts, Sidekick is intended to help rather than replace and to work across all applications.

Also, rather than focusing on macros to make things more efficient, Sidekick attempts to replicate regular workflows. I think this makes it simpler. But additional parsers could be added to go macro crazy if so desired. 

## Contributing

If you want to contribute, please first create an issue or send me an email describing your intended change and containing the following - "I hereby assign copyright in this code to the project, to be licensed under the same terms as the rest of the code”. This statement just makes it easier to enforce copyright if necessary and in no way impacts your rights or restricts the use of the code beyond the [AGPL license](https://github.com/oeschsec/Sidekick---voice-controlled-keyboard-and-mouse/blob/master/LICENSE). Wait for me to give you the greenlight, then use the [fork and pull model](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/forkandpull.md) to make your changes.

#### Things I would like to see

- community created parsers
- ways to optimize the speech recognition process
- new features or functionality

## Install

Download the vosk-model-en-us-daanzu-20200905-lgraph (129M) model folder from https://alphacephei.com/vosk/models, place in same directory as vosk_main.py, and rename the folder to 'model'. 

#### On Mac

- brew install portaudio
- pip install numpy vosk pyautogui pyaudio

#### On Ubuntu

- sudo apt-get install scrot python3-tk python3-dev (for pyautogui on Ubuntu)
- sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
- sudo apt-get install python3-pyaudio
- pip install numpy vosk pyautogui pyaudio

#### On Windows

- install Python 3.8 64-bit (https://www.python.org/downloads/windows/) - 3.9 is not supported on Windows yet (see Vosk docs)
- pip install numpy vosk pyautogui
- make sure that vosk is at least version 0.3.18 - run `pip install vosk --upgrade` if not sure
- pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl (download [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)) or appropriate version at time of install

## Usage

- python3 sidekick.py
- see the [user guide](https://github.com/oeschsec/speech-driven-keyboard/tree/master/docs/userguide.md) for instructions on use

## Approach

- I wanted to use a speech recognition library that worked out-of-the-box and did not require retraining
- I wanted it to work offline and be fully open source
- I decided to use Vosk for speech-to-text because it is a) offline (unlike services such as Google's API), b) more accurate than offline alternatives such as CMU's PocketSphinx, c) entirely open source, unlike picovoice. I initially tried to use python's SR library with google (see srmodule_old folder), but found it too slow and, as mentioned before, requiring internet. I also tried Mozilla's deepspeech, but for this specific application it was less ideal than Vosk due to a lack of out-of-the-box API functionality that I required and resource consumption. 
- I optimized accuracy by using multiple Vosk models for different states. And then made optimizations to help with the speed of switching states. 
- I used the smaller Vosk model because it was faster and responsiveness is important for this application. Also, the larger models do not currently support dynamic word mapping, which was important for my use case to increase accuracy, though models that are hybrid are planned per my understanding.

## Vosk Docs

- https://alphacephei.com/vosk/install (requirements for running vosk listed here)
- https://medium.com/analytics-vidhya/offline-speech-recognition-made-easy-with-vosk-c61f7b720215

## Related Projects & Articles 

I am aware of other interesting related projects. I highly recommend checking out each of the following resources if you're interested in this space.

- https://serenade.ai/ - code with voice app - focuses specifically on helping developers write code
- [dragonfly](https://github.com/dictation-toolbox/dragonfly)
- https://github.com/dictation-toolbox/natlink
- https://talonvoice.com/
- [Caster](https://caster.readthedocs.io/en/latest/)
- fun [video](https://www.youtube.com/watch?v=8SkdfdXWYaI) of a guy who hacked dragon to code back in 2013 - inspiration for a lot of voice coders

## Ideas / Notes

- faster speech recognition would help significantly (smaller vosk model helped)
- external usb sound card such as the Andrea PureAudio / Audix OM7 mic

## Copyright Notice

Copyright (C) 2021 The Sidekick Contributors

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.