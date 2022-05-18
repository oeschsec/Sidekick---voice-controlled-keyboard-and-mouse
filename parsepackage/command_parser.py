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
from screenshot import *
from overlay import overlay
import string
import threading
from os.path import exists

class CommandParser:
    def __init__(self, system, steps):
        self.os = system
        self.steps = steps 
        self.tempvar = ""
        self.stop_screenshot = [False]
        self.screenshot_started = False
        self.screen_size = (1920, 1080)
        self.keys = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','alt','delete','control','shift','tab','apple']

        self.keymapping = {
            "control" : "ctrl",
            "apple" : "command"
        }

        self.grid_horizontal = ['a','b','c','d','e','f','g','h','i','j','k']

        self.grid_vertical = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
        ]
        self.numbers = [
            "pod",
            "pup",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "hundred",
        ]
        self.stateless_commands = [
            "click",
            "go",
            "tab",
            "double",
            "enter",
            "space",
            "back",
        ]
        self.commands = [
            "undo",
            "hot",
            "ack",
            "lap",
            "nip",
            "switch",
            "cancel",
            "key",
            "next",
            "redo",
            "close",
            "find",
            "replace",
            "nab",
            "cab",
            "lab",
            "rab",
            "escape",
            "in",
            "out",
            "rick",
            "hold",
            "lock",
            "terminate",
            "release",
            "triple",
            "grid",
            "up",
            "down",
            "left",
            "right",
            "copy",
            "paste",
            "north",
            "south",
            "east",
            "west",
            "save",
            "scroll",
            "screenshot",
            "overlay",
        ]

        self.commandlist = (
            self.keys
            + self.grid_vertical
            + self.stateless_commands
            + self.commands
            + self.numbers
        )

    def word_to_int(self, word):
        mapping = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
            "eleven": "11",
            "twelve": "12",
            "thirteen": "13",
            "fourteen": "14",
            "fifteen": "15",
            "sixteen": "16",
            "seventeen": "17",
            "eighteen": "18",
            "nineteen": "19",
            "twenty": "20",
            "thirty": "30", 
            "forty": "40",
            "fifty": "50",
            "hundred": "100",
        }
        return mapping[word]

    # Maps key commands to actual button press
    def map_keys(self,val):
        if val in self.keymapping:
            return self.keymapping[val]
        else:
            return val

    # Stateless commands should return an empty buffer
    def stateless_command(self, command_buffer):
        if command_buffer[0] == "click" or command_buffer[0] == "go":
            click()
            command_buffer = []
        elif command_buffer[0] == "double":
            doubleclick()
            command_buffer = []
        elif command_buffer[0] == "inter" or command_buffer[0] == "enter":
            hitEnter()
            command_buffer = []
        elif command_buffer[0] == "tab":
            hitTab()
            command_buffer = []
        elif command_buffer[0] == "space":
            hitSpace()
            command_buffer = []
        elif command_buffer[0] == "ack":
            holdKeyDown("alt")
            click()
            keyUp("alt")
            command_buffer = []
        elif command_buffer[0] == "back":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.numbers:
                    backspace(int(self.word_to_int(command_buffer[1])))
                    command_buffer = []
                else:
                    return [
                        True,
                        self.handle_invalid_command(command_buffer[1], command_buffer),
                    ]
        else:
            return [False, command_buffer]

        return [True, command_buffer]

    def handle_invalid_command(self, val, command_buffer):
        if val in self.commands or val in self.stateless_commands:
            command_buffer = [val]
            stateless, command_buffer = self.stateless_command(command_buffer)
            if not stateless:
                command_buffer = self.evaluate_command(command_buffer)
        else:
            command_buffer = []

        return command_buffer

    def evaluate_command(self, command_buffer):
        if command_buffer[0] == "rick":
            rightclick()
            command_buffer = []
        elif command_buffer[0] == "lap":
            if self.os == "Darwin":
                hotKeyPress(["command", "left"])
            else:
                hotKeyPress(["alt", "left"])

            command_buffer = []
        elif command_buffer[0] == "nip":
            if self.os == "Darwin":
                hotKeyPress(["command", "right"])
            else:
                hotKeyPress(["alt", "right"])
                
            command_buffer = []
        elif command_buffer[0] == "pod":
            hotKeyPress(["pgdn"])
            command_buffer = []
        elif command_buffer[0] == "pup":
            hotKeyPress(["pgup"])
            command_buffer = []
        elif command_buffer[0] == "triple":
            tripleclick()
            command_buffer = []
        elif command_buffer[0] == "lock":
            if len(command_buffer) == 1:
                self.x, self.y = getPosition()
            elif len(command_buffer) >= 2:
                if command_buffer[1] == "release":
                    dragMouse(self.x, self.y)
                    command_buffer = []
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "up":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.numbers:
                    for i in range(int(self.word_to_int(command_buffer[1]))):
                        hotKeyPress(["up"])
                    command_buffer = []
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "down":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.numbers:
                    for i in range(int(self.word_to_int(command_buffer[1]))):
                        hotKeyPress(["down"])
                    command_buffer = []
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "left":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.numbers:
                    for i in range(int(self.word_to_int(command_buffer[1]))):
                        hotKeyPress(["left"])
                    command_buffer = []
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "right":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.numbers:
                    for i in range(int(self.word_to_int(command_buffer[1]))):
                        hotKeyPress(["right"])
                    command_buffer = []
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "copy":
            if self.os == "Darwin":
                hotKeyPress(["command", "c"])
            else:
                hotKeyPress(["ctrl", "c"])
            command_buffer = []
        elif command_buffer[0] == "in":
            if self.os == "Darwin":
                hotKeyPress(["command", "+"])
            else:
                hotKeyPress(["ctrl", "+"])
            command_buffer = []
        elif command_buffer[0] == "out":
            if self.os == "Darwin":
                hotKeyPress(["command", "-"])
            else:
                hotKeyPress(["ctrl", "-"])
            command_buffer = []
        elif command_buffer[0] == "paste":
            if self.os == "Darwin":
                hotKeyPress(["command", "v"])
            else:
                hotKeyPress(["ctrl", "v"])
            command_buffer = []
        elif command_buffer[0] == "close":
            if self.os == "Darwin":
                hotKeyPress(["command", "w"])
            else:
                hotKeyPress(["ctrl", "w"])
            command_buffer = []
        elif command_buffer[0] == "find":
            if self.os == "Darwin":
                hotKeyPress(["command", "f"])
            else:
                hotKeyPress(["ctrl", "f"])
            command_buffer = []
        elif command_buffer[0] == "undo":
            if self.os == "Darwin":
                hotKeyPress(["command", "z"])
            else:
                hotKeyPress(["ctrl", "z"])
            command_buffer = []
        elif command_buffer[0] == "redo":
            if self.os == "Darwin":
                hotKeyPress(["command", "shift","z"])
            else:
                hotKeyPress(["ctrl", "shift","z"])
            command_buffer = []
        elif command_buffer[0] == "replace":
            if self.os == "Darwin":
                hotKeyPress(["command", "shift", "h"])
            else:
                hotKeyPress(["ctrl", "h"])
            command_buffer = []
        elif command_buffer[0] == "nab":
            if self.os == "Darwin":
                hotKeyPress(["command", "t"])
            else:
                hotKeyPress(["ctrl", "t"])
            command_buffer = []
        elif command_buffer[0] == "cab":
            if self.os == "Darwin":
                hotKeyPress(["command", "shift", "t"])
            else:
                hotKeyPress(["ctrl","shift","t"])
            command_buffer = []
        elif command_buffer[0] == "lab":
            hotKeyPress(["ctrl", "shift","tab"])
            command_buffer = []
        elif command_buffer[0] == "rab":
            hotKeyPress(["ctrl", "tab"])
            command_buffer = []
        elif command_buffer[0] == "escape":
            hotKeyPress(["escape"])
            command_buffer = []
        elif command_buffer[0] == "terminate":
            hotKeyPress(["ctrl", "c"])
            command_buffer = []
        elif command_buffer[0] == "save" or command_buffer[0] == "say":
            if self.os == "Darwin":
                hotKeyPress(["command", "s"])
            else:
                hotKeyPress(["ctrl", "s"])
            command_buffer = []
        elif command_buffer[0] == "line": 
            hotKeyPress(["end"])
            hotKeyPress(["shift", "home"])
            command_buffer = []
        elif command_buffer[0] == "copy line": 
            hotKeyPress(["end"])
            hotKeyPress(["shift", "home"])
            if self.os == "Darwin":
                hotKeyPress(["command", "c"])
            else:
                hotKeyPress(["ctrl", "c"])
            command_buffer = []
        elif command_buffer[0] == "cut line": 
            hotKeyPress(["end"])
            hotKeyPress(["shift", "home"])
            if self.os == "Darwin":
                hotKeyPress(["command", "x"])
            else:
                hotKeyPress(["ctrl", "x"])
            command_buffer = []
        elif command_buffer[0] == "loop": 
            pyautogui.write("for (int i = 0; i < N; i++) {")
            hotKeyPress(["enter"])
            pyautogui.write("continue;")
            hotKeyPress(["enter"])
            pyautogui.write("}")
            hotKeyPress(["enter"])
            hotKeyPress(["up", "up", "end"])
            command_buffer = []
        elif command_buffer[0] == "switch":

            if self.os == "Darwin":
                holdKeyDown("command")
            else:
                holdKeyDown("alt")

            if len(command_buffer) == 1:
                hotKeyPress(["tab"])

            if len(command_buffer) >= 2:
                if command_buffer[1] == "next":
                    hotKeyPress(["tab"])
                    command_buffer = ["switch"]
                elif command_buffer[1] == "escape":
                    hotKeyPress(["escape"])
                    
                    if self.os == "Darwin":
                        keyUp("command")
                    else:
                        keyUp("alt")

                    command_buffer = []                    

                else:
                    if self.os == "Darwin":
                        keyUp("command")
                    else:
                        keyUp("alt")

                    command_buffer = []

        elif command_buffer[0] == "hold":

            if len(command_buffer) == 1:
                holdLeft()
                command_buffer = ["hold"]
            else:
                releaseLeft()
                command_buffer = []

        elif command_buffer[0] == "key":

            if len(command_buffer) >= 2:

                if command_buffer[1] in self.keys:
                    if self.tempvar != "":
                        keyUp(self.tempvar)
                    holdKeyDown(self.map_keys(command_buffer[1]))
                    self.tempvar = self.map_keys(command_buffer[1])
                    command_buffer = ["key"]

                else:
                    keyUp(self.tempvar)
                    self.tempvar = ""

                    command_buffer = []            

        elif command_buffer[0] == "hot":

            if command_buffer[-1] in self.keys or len(command_buffer) == 1:
                pass

            else:
                hot_keys = []
                for val in command_buffer:
                    if val != "hot":
                        hot_keys.append(self.map_keys(val))
                
                hotKeyPress(hot_keys)

                command_buffer = [] 

        elif command_buffer[0] == "north":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(0, -1 * int(self.steps[command_buffer[1]]))
                    command_buffer = ["north"]
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "south":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(0, int(self.steps[command_buffer[1]]))
                    command_buffer = ["south"]
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "east" or command_buffer[0] == "is":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(int(self.steps[command_buffer[1]]), 0)
                    command_buffer = ["east"]
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "west":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(-1 * int(self.steps[command_buffer[1]]), 0)
                    command_buffer = ["west"]
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "scroll" or command_buffer[0] == "surf":
            if len(command_buffer) >= 2:
                if command_buffer[1] in ["up", "down", "left", "right"]:
                    if len(command_buffer) >= 3:
                        if command_buffer[2] in self.steps:
                            if command_buffer[1] == "up":
                                scrollUp(int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll", "up"]
                            if command_buffer[1] == "down":
                                scrollUp(-1 * int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll", "down"]
                            if command_buffer[1] == "left":
                                scrollRight(-1 * int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll", "left"]
                            if command_buffer[1] == "right":
                                scrollRight(int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll", "right"]
                        else:
                            return self.handle_invalid_command(
                                command_buffer[2], command_buffer
                            )
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "grid":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.grid_horizontal:
                    if len(command_buffer) >= 3:
                        if command_buffer[2] in self.grid_vertical:
                            x, y = screenSize()
                            horizontal = string.ascii_lowercase.index(
                                command_buffer[1]
                            )  # 0 indexed
                            vertical = int(self.word_to_int(command_buffer[2])) - 1
                            xpoint = float(horizontal) * (x / 10.0)
                            ypoint = y - float(vertical) * (y / 10.0)

                            # add some buffer to keep mouse off the very edges of the screen / visible
                            if xpoint == x:
                                xpoint = xpoint - 20
                            elif xpoint == 0:
                                xpoint = xpoint + 20
                            if ypoint == y:
                                ypoint = ypoint - 20
                            elif ypoint == 0:
                                ypoint = ypoint + 20

                            moveMouseAbs(xpoint, ypoint)
                            command_buffer = ["grid"]
                        else:
                            return self.handle_invalid_command(
                                command_buffer[2], command_buffer
                            )
                else:
                    return self.handle_invalid_command(
                        command_buffer[1], command_buffer
                    )
        elif command_buffer[0] == "screenshot":
            if self.screenshot_started == False and self.stop_screenshot[0] == True:
                self.stop_screenshot[0] = False
            
            if self.screenshot_started == False:
                print(command_buffer)
                w = self.screen_size[0]
                h = self.screen_size[1]
                grid = "Images/{}x{}_grid.png".format(w,h)
                if not exists(grid):
                    create_gridlines(w, h)
                
                p = threading.Thread(target=take_screenshot, args=(w, h, grid, self.stop_screenshot))
                p.start()
                self.screenshot_started = True
            else:
                self.stop_screenshot[0] = True
                self.screenshot_started = False
            command_buffer=[]
        
        elif command_buffer[0] == "overlay":
            print("Showing grid overlay. Close the window manually to continue using Sidekick.")
            w = self.screen_size[0]
            h = self.screen_size[1]
            grid = "Images/{}x{}_grid.png".format(w,h)
            if not exists(grid):
                create_gridlines(w, h)           
            overlay(grid)
            command_buffer=[]

        else:
            command_buffer = []

        return command_buffer
