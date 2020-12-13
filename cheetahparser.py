from actions import *

class CheetahParser: 
    
    def __init__(self):
        self.state = "command"
        self.command_buffer = []
        self.steps = {
            "one":10,
            "two":30,
            "three":50,
            "four":100,
            "five":300,
            "six":500,
            "seven":1000,
            "eight":1500
        }

    def ingest(self, words): 
        #print(word.lower())
        for word in words.split(' '):
            if word != '':
                self.command_buffer.append(word.lower())
        print(self.command_buffer)
        self.evaluate()

    def evaluate(self):
        if self.command_buffer[0] == "state" and len(self.command_buffer) == 2:
            if self.command_buffer[1] == "command":
                self.state = "command"
                self.command_buffer = []
            elif self.command_buffer[1] == "text" or self.command_buffer[1] == "taxed":
                self.state = "text"
                self.command_buffer = []
            else:
                self.command_buffer = []

        if len(self.command_buffer) > 0 and self.command_buffer[0] != "state":
            if self.state == "command":
                self.evaluate_command()
            elif self.state == "text":
                self.evaluate_text()

    def evaluate_command(self):
        if (self.command_buffer[0] == "click" or self.command_buffer[0] == "quick"):
            print("here")
            click()
            self.command_buffer = []
        elif (self.command_buffer[0] == "inter" or self.command_buffer[0] == "enter" or self.command_buffer[0] == "engage"):
            hitEnter()
            self.command_buffer = []
        elif self.command_buffer[0] == "space":
            hitSpace()
            self.command_buffer = []
        elif self.command_buffer[0] == "copy":
            hotKeyPress(["ctrl","c"])
            self.command_buffer = []
        elif self.command_buffer[0] == "paste":
            hotKeyPress(["ctrl","v"])
            self.command_buffer = []
        else:
            self.command_buffer = []

    def evaluate_text(self):
        writeToScreen(' '.join(self.command_buffer))
        self.command_buffer = []