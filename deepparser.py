from actions import *

class CheetahParser: 
    
    def __init__(self):
        self.state = "command"
        self.command_buffer = []
        self.steps = {
            "one":10,
            "an":10,
            "on":10,
            "two":30,
            "to":30,
            "three":50,
            "four":100,
            "for":100,
            "five":300,
            "six":500,
            "seven":1000,
            "eight":1500,
            "at":1500
        }

    def ingest(self, words): 
        #print(word.lower())
        for word in words.split(' '):
            if word != '':
                self.command_buffer.append(word.lower())
        print(self.command_buffer)
        if len(self.command_buffer) > 0: 
            self.evaluate()

    def evaluate(self):
        if self.command_buffer[0] == "state" and len(self.command_buffer) >= 2:
            if self.command_buffer[1] == "command":
                self.state = "command"
                self.command_buffer = []
            elif self.command_buffer[1] == "text" or "tax" in self.command_buffer[1]:
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
        if (self.command_buffer[0] == "click" or self.command_buffer[0] == "quick" or self.command_buffer[0] == 'lick'):
            click()
            self.command_buffer = []
        elif (self.command_buffer[0] == "inter" or self.command_buffer[0] == "enter" or self.command_buffer[0] == "engage"):
            hitEnter()
            self.command_buffer = []
        elif self.command_buffer[0] == "space":
            hitSpace()
            self.command_buffer = []
        elif self.command_buffer[0] == "up":
            hotKeyPress(["up"])
            self.command_buffer = []
        elif self.command_buffer[0] == "down":
            hotKeyPress(["down"])
            self.command_buffer = []
        elif self.command_buffer[0] == "left":
            hotKeyPress(["left"])
            self.command_buffer = []
        elif self.command_buffer[0] == "right":
            hotKeyPress(["right"])
            self.command_buffer = []
        elif self.command_buffer[0] == "back":
            backspace(1)
            self.command_buffer = []
        elif self.command_buffer[0] == "copy":
            hotKeyPress(["ctrl","c"])
            self.command_buffer = []
        elif self.command_buffer[0] == "paste":
            hotKeyPress(["ctrl","v"])
            self.command_buffer = []
        elif self.command_buffer[0] == "save" or self.command_buffer[0] == "say":
            hotKeyPress(["ctrl","s"])
            self.command_buffer = []
        elif self.command_buffer[0] == "north":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(0,-1*int(self.steps[self.command_buffer[1]]))
                    self.command_buffer = ["north"]
                else:
                    self.command_buffer = []
        elif self.command_buffer[0] == "south":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(0,int(self.steps[self.command_buffer[1]]))
                    self.command_buffer = ["south"]
                else:
                    self.command_buffer = []
        elif self.command_buffer[0] == "east" or self.command_buffer[0] == "is":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(int(self.steps[self.command_buffer[1]]),0)
                    self.command_buffer = ["east"]
                else:
                    self.command_buffer = []
        elif self.command_buffer[0] == "west":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(-1*int(self.steps[self.command_buffer[1]]),0)
                    self.command_buffer = ["west"]
                else:
                    self.command_buffer = []
        elif self.command_buffer[0] == "surf" or self.command_buffer[0] == "sir" or self.command_buffer[0] == "serf":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in ["up","down","left","right"]:
                    if len(self.command_buffer) >= 3: 
                        if self.command_buffer[2] in self.steps:
                            if self.command_buffer[1] == "up":
                                scrollUp(int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["surf","up"]
                            if self.command_buffer[1] == "down":
                                scrollUp(-1*int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["surf","down"]
                            if self.command_buffer[1] == "left":
                                scrollRight(-1*int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["surf","left"]
                            if self.command_buffer[1] == "right":
                                scrollRight(int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["surf","right"]
                        else:
                            self.command_buffer = []
                else:
                    self.command_buffer = []
        else:
            self.command_buffer = []

    def insert_punctuation(self, text):
        text = text.replace("period",".")
        text = text.replace("colon",":")
        text = text.replace("dash","-")
        text = text.replace("comma",",").replace("com",",")
        text = text.replace("pork","?")
        text = text.replace("dot",".")
        text = text.replace("hash","#")
        return text

    def evaluate_text(self):
        if "cap" in self.command_buffer[0] or "chap" in self.command_buffer[0]:
            print("cappy")
            if len(self.command_buffer) >= 2:
                writeToScreen(self.command_buffer[1].capitalize() + ' ')
                if len(self.command_buffer) > 2:
                    self.command_buffer = self.command_buffer[2:]
                else:
                    self.command_buffer = []
        else:
            for i in range(0,len(self.command_buffer)):
                if self.command_buffer[i] in ["period","dash","comma","pork", "hash"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(self.command_buffer[i]) + ' ')
                elif self.command_buffer[i] in ["dot"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(self.command_buffer[i]))
                else:
                    writeToScreen(self.command_buffer[i] + ' ')

            self.command_buffer = []