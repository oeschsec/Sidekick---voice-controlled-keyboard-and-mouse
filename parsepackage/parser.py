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
import platform

from parsepackage.program_parser import ProgramParser
from .mouse_parser import MouseParser
from .text_parser import TextParser
from .command_parser import CommandParser
from .alpha_parser import AlphaParser
from .volume_parser import VolumeParser
from .horizontal_parser import HorizontalParser

class Parser:
    def __init__(self):
        self.os = platform.system()
        self.state = "command"
        self.command_buffer = []
        self.pause = False
        self.dB = 0

        self.stepmapping = {
            "one": 10,
            "an": 10,
            "on": 10,
            "two": 30,
            "to": 30,
            "too": 30,
            "three": 50,
            "four": 100,
            "for": 100,
            "five": 300,
            "six": 500,
            "seven": 1000,
            "eight": 1500,
            "at": 1500,
        }

        self.states = ["text", "command", "pause", "alpha", "volume", "horizontal", "mouse"] #mouse
        self.steps = ["one", "two", "three", "four", "five", "six", "seven", "eight"]

        self.mouseParser = MouseParser(self.os, self.stepmapping)
        self.textParser = TextParser(self.os, self.stepmapping)
        self.commandParser = CommandParser(self.os, self.stepmapping)
        self.programParser = ProgramParser(self.os)
        self.alphaParser = AlphaParser(self.os)
        self.volumeParser = VolumeParser(self.os, self.stepmapping)
        self.horizontalParser = HorizontalParser(self.os, self.stepmapping)

        # nontextcommands can be fed to a speech to text model to make it work more effectively for commands
        self.nontextcommands = list(
            set(self.states)
            | set(self.steps)
            | set(self.commandParser.commandlist)
            | set(self.mouseParser.commands)
        )
        self.alphavalues = (
            self.alphaParser.keywords
            + self.states
            + self.commandParser.stateless_commands
        )

    # ingest string that may contain multiple space delimited words, where each word is a sent to parser individually
    def set_threshold(self, threshold):
        self.volumeParser.set_threshold(threshold)
        self.horizontalParser.set_threshold(threshold)

    def set_audio_stream(self, stream):
        self.volumeParser.set_audio_stream(stream)
        self.horizontalParser.set_audio_stream(stream)

    def set_screen_size(self, screen_size):
        self.commandParser.screen_size = screen_size 


    def ingest(self, words):
        # print(word.lower())
        for word in words.split(" "):
            if word != "":
                self.command_buffer.append(word.lower())

        if len(self.command_buffer) > 0:

            if not self.pause:
                print(
                    self.command_buffer
                )  # makes it easy to see current state of command_buffer

            self.evaluate()

    def evaluate(self):
        print("evaluate")
        if self.pause:

            if self.command_buffer[0] == "time":
                if len(self.command_buffer) >= 2:
                    if self.command_buffer[1] == "to":
                        if len(self.command_buffer) >= 3:
                            if self.command_buffer[2] == "work":
                                self.state = "command"
                                self.pause = False
                                self.command_buffer = []
                                print("Sidekick is back in action")
            else:
                self.command_buffer = []

        else:
            # either set state or parse command
            if self.command_buffer[-1] == "pause":
                self.pause = True
                self.state = "text"  # this ensures 'pause' is not accidentally triggered by model with smaller search space
                print("Sidekick is taking a rest")
                self.command_buffer = []
            elif self.command_buffer[-1] == "command":
                self.state = "command"
                self.command_buffer = []
            elif self.command_buffer[-1] == "text":
                self.state = "text"
                self.command_buffer = []
            elif self.command_buffer[-1] == "code":
                self.state = "program"
                self.command_buffer = []
            elif self.command_buffer[-1] == "alpha":
                self.state = "alpha"
                self.command_buffer = []
            elif self.command_buffer[-1] == "mouse": 
                self.state = "mouse"
                self.command_buffer = []
                self.command_buffer, self.state = self.mouseParser.evaluate_mouse(
                    self.command_buffer
                )
            elif self.command_buffer[-1] == "volume":
                print("This was executed")
                self.state = "volume"
                self.command_buffer = []
                self.command_buffer, self.state = self.volumeParser.evaluate_volume(
                    self.command_buffer,
                    self.dB
                )
            elif self.command_buffer[-1] == "horizontal":
                self.state = "horizontal"
                self.command_buffer = []
                self.command_buffer, self.state = self.horizontalParser.evaluate_volume(
                    self.command_buffer
                )
            else:  # send command to appropriate parsing function
                if len(self.command_buffer) > 0:
                    (
                        stateless,
                        self.command_buffer,
                    ) = self.commandParser.stateless_command(self.command_buffer)
                    if not stateless:
                        if self.state == "command":
                            self.command_buffer = self.commandParser.evaluate_command(
                                self.command_buffer
                            )
                        elif self.state == "text":
                            self.command_buffer = self.textParser.evaluate_text(
                                self.command_buffer
                            )
                        elif self.state == "program":
                            self.command_buffer = self.programParser.evaluate_text(
                                self.command_buffer
                            )
                        elif self.state == "alpha":
                            self.command_buffer = self.alphaParser.evaluate_text(
                                self.command_buffer
                            )
                        elif self.state == "mouse":
                            (
                                self.command_buffer,
                                self.state,
                            ) = self.mouseParser.evaluate_mouse(self.command_buffer)
                        elif self.state == "volume":
                            (
                                self.command_buffer,
                                self.state,
                            ) = self.volumeParser.evaluate_volume(self.command_buffer, self.dB)
                        elif self.state == "horizontal":
                            (
                                self.command_buffer,
                                self.state,
                            ) = self.horizontalParser.evaluate_volume(self.command_buffer)        
        # stop mouse if state is switched before stopping
        if not self.mouseParser.stopMouse and self.state != "mouse":
            self.mouseParser.stopMouse = True
        if not self.volumeParser.stopVolume and self.state != "volume":
            self.volumeParser.stopVolume = True
        if not self.horizontalParser.stopVolume and self.state != "horizontal":
            self.horizontalParser.stopVolume = True
