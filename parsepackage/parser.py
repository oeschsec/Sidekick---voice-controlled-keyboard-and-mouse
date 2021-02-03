from actions import *
import platform
from .mouse_parser import MouseParser 
from .text_parser import TextParser 
from .command_parser import CommandParser
from .alpha_parser import AlphaParser

class Parser: 
    
    def __init__(self):
        self.os = platform.system()
        self.state = "command"
        self.command_buffer = []

        self.stepmapping = {
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

        self.states = ["text","command","mouse","pause","alpha"]
        self.steps = ["one","two","three","four","five","six","seven","eight"]

        self.mouseParser = MouseParser(self.os, self.stepmapping)
        self.textParser = TextParser(self.os, self.stepmapping)
        self.commandParser = CommandParser(self.os, self.stepmapping)
        self.alphaParser = AlphaParser(self.os)

        # nontextcommands can be fed to a speech to text model to make it work more effectively for commands
        self.nontextcommands = list(set(self.states) | set(self.steps) | set(self.commandParser.commandlist) | set(self.mouseParser.commands) )
        self.alphavalues = self.alphaParser.keywords + self.states + self.commandParser.stateless_commands

    # ingest string that may contain multiple space delimited words, where each word is a sent to parser individually
    def ingest(self, words): 
        #print(word.lower())
        for word in words.split(' '):
            if word != '':
                self.command_buffer.append(word.lower())

        if len(self.command_buffer) > 0: 
            
            if self.state != "pause":
                print(self.command_buffer) # makes it easy to see current state of command_buffer

            self.evaluate()

    def evaluate(self):

            if self.state != "pause":
                # either set state or parse command
                if self.command_buffer[-1] == "command":
                    self.state = "command"
                    self.command_buffer = []
                elif self.command_buffer[-1] == "text":
                    self.state = "text"
                    self.command_buffer = []
                elif self.command_buffer[-1] == "alpha":
                    self.state = "alpha"
                    self.command_buffer = []
                elif self.command_buffer[-1] == "pause":
                    self.state = "pause"
                    self.command_buffer = []
                elif self.command_buffer[-1] == "mouse":
                    self.state = "mouse"
                    self.command_buffer = []
                    self.command_buffer, self.state = self.mouseParser.evaluate_mouse(self.command_buffer)
                else: # send command to appropriate parsing function
                    if len(self.command_buffer) > 0:
                        stateless, self.command_buffer = self.commandParser.stateless_command(self.command_buffer)
                        if not stateless:
                            if self.state == "command":
                                self.command_buffer = self.commandParser.evaluate_command(self.command_buffer)
                            elif self.state == "text":
                                self.command_buffer = self.textParser.evaluate_text(self.command_buffer)
                            elif self.state == "alpha":
                                self.command_buffer = self.alphaParser.evaluate_text(self.command_buffer)
                            elif self.state == "mouse":
                                self.command_buffer, self.state = self.mouseParser.evaluate_mouse(self.command_buffer)
            else:
                self.command_buffer = []
                #print("Sidekick is paused - say 'pause' again to continue")






