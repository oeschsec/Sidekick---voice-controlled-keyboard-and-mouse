from actions import *
import platform
from .mouse_parser import MouseParser 
from .text_parser import TextParser 
from .command_parser import CommandParser

class Parser: 
    
    def __init__(self):
        self.os = platform.system()
        self.state = "command"
        self.command_buffer = []
        self.steps = {
            "one":10,
            "an":10,
            "on":10,
            "two":30,
            "to":30,
            "too":30,
            "three":50,
            "four":100,
            "for":100,
            "five":300,
            "six":500,
            "seven":1000,
            "eight":1500,
            "at":1500
        }

        self.mouseParser = MouseParser(self.os, self.steps)
        self.textParser = TextParser(self.os, self.steps)
        self.commandParser = CommandParser(self.os, self.steps)

    def ingest(self, words): 
        #print(word.lower())
        for word in words.split(' '):
            if word != '':
                self.command_buffer.append(word.lower())
        print(self.command_buffer)
        if len(self.command_buffer) > 0: 
            self.evaluate()

    def evaluate(self):
            if self.command_buffer[-1] == "command":
                self.state = "command"
                self.command_buffer = []
            elif self.command_buffer[-1] == "text":
                self.state = "text"
                self.command_buffer = []
            elif self.command_buffer[-1] == "mouse" or self.command_buffer[-1] == "miles":
                self.state = "mouse"
                self.command_buffer = []
                self.mouseParser.evaluate_mouse(self.command_buffer)
            else:
                if len(self.command_buffer) > 0:
                    stateless, self.command_buffer = self.commandParser.stateless_command(self.command_buffer)
                    if not stateless:
                        if self.state == "command":
                            self.command_buffer = self.commandParser.evaluate_command(self.command_buffer)
                        elif self.state == "text":
                            self.command_buffer = self.textParser.evaluate_text(self.command_buffer)
                        elif self.state == "mouse":
                            self.command_buffer = self.mouseParser.evaluate_mouse(self.command_buffer)






