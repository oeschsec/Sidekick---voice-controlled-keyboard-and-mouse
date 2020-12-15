#!/bin/bash

trap ctrl_c INT

function ctrl_c() {
      #kill $! # last process started in background
      kill $(pgrep -f 'python3 deepspeech_main.py')
      exit 1
}

while true; do
    python3 deepspeech_main.py &
    sleep 45
    kill $(pgrep -f 'python3 deepspeech_main.py')
done