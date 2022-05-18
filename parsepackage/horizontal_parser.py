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
from actions import *
import threading
import math
import audioop



class HorizontalParser:
    def __init__(self, system, steps):
        self.volumeStarted = False
        self.os = system
        self.steps = steps
        self.stopVolume = True

        self.commands = [
            "stop",
            "snail",
            "slow",
            "fast",
            "medium",
            "up",
            "down",
            "counter",
            "clock",
            "north",
            "south",
            "east",
            "west",
            "one",
            "two",
            "three",
            "four",
            "northeast",
            "northwest",
            "southeast",
            "southwest",
        ]
    def set_threshold(self, threshold):
        self.threshold = threshold
        
        self.midpoint = (self.threshold + 55) /2
    
    def set_audio_stream(self, stream):
        self.stream = stream

    def evaluate_volume(self, command_buffer):
        if not self.volumeStarted:
            
            self.stopVolume = False
            self.magnitude = 5  # in pixels
            self.sleep = 0.2
            self.setVolumeCoord(90)
        
        data = self.stream.read(4000,exception_on_overflow = False)
        # calculate decibels
        dB = 20 * math.log10(audioop.rms(data,2)+1)

       # if len(command_buffer) > 0:     
        """print("Volume " + str(dB))
        if dB < 45:
            print("MOM")
            self.setVolumeCoord(self.currentangle + 15)
        elif dB >= 45:
            print("WOW")
            self.setVolumeCoord(self.currentangle - 15)"""
        command_buffer = []

        if not self.volumeStarted:
            self.startVolume()

        return [command_buffer, "volume"]

    def startVolume(self):
        thread = threading.Thread(target=self.volume_thread)
        thread.daemon = True
        thread.start()
        self.volumeStarted = True

    def setVolumeCoord(self, degrees):
        print("start")
        self.currentangle = degrees
        self.x = self.magnitude * math.cos(math.radians(degrees))
        print(self.x)
        self.y = -1 * self.magnitude * math.sin(math.radians(degrees))
        print(self.y)
        return

    def volume_thread(self):
        while True:
            if self.stopVolume:
                self.volumeStarted = False
                break
            else:
                moveMouse(self.x, self.y)
                time.sleep(self.sleep)
