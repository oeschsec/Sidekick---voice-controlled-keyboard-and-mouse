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


class TextParser:
    def __init__(self, system, steps):
        self.os = system
        self.steps = steps
        self.space = " "
        self.tocap = ["i"]

    def evaluate_text(self, command_buffer):
        if command_buffer[0] == "underscore":
            self.space = "_"
            command_buffer = []
        elif command_buffer[0] == "pack":
            self.space = ""
            command_buffer = []
        elif command_buffer[0] == "cap":  # capitalize next word spoken
            if len(command_buffer) >= 2:
                writeToScreen(self.space + command_buffer[1].capitalize())
                if len(command_buffer) > 2:
                    command_buffer = command_buffer[2:]
                else:
                    command_buffer = []

                if self.space != " ":
                    self.space = " "
        else:
            for i in range(0, len(command_buffer)):
                if command_buffer[i] in self.tocap:
                    writeToScreen(self.space + command_buffer[i].capitalize())
                else:
                    writeToScreen(self.space + command_buffer[i])

            if self.space != " ":
                self.space = " "

            command_buffer = []

        return command_buffer
