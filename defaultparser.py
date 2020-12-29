from actions import *

class DefaultParser: 
    
    def __init__(self):
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

        self.commands = ["click", "jump", "inter", "enter", "space", "back", "up","down","left","right","copy","paste","north","south","east","west","save","mouse"]

    def ingest(self, words): 
        #print(word.lower())
        for word in words.split(' '):
            if word != '':
                self.command_buffer.append(word.lower())
        print(self.command_buffer)
        if len(self.command_buffer) > 0: 
            self.evaluate()

    def evaluate(self):
            if self.command_buffer[0] == "command":
                self.state = "command"
                self.command_buffer = []
            elif self.command_buffer[0] == "text":
                self.state = "text"
                self.command_buffer = []
            else:
                if len(self.command_buffer) > 0:
                    if not self.stateless_command():
                        if self.state == "command":
                            self.evaluate_command()
                        elif self.state == "text":
                            self.evaluate_text()

    def stateless_command(self):
        if (self.command_buffer[0] == "click" or self.command_buffer[0] == "jump"):
            click()
            self.command_buffer = []
        elif (self.command_buffer[0] == "inter" or self.command_buffer[0] == "enter"):
            hitEnter()
            self.command_buffer = []
        elif self.command_buffer[0] == "space":
            hitSpace()
            self.command_buffer = []
        elif self.command_buffer[0] == "back":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    backspace(int(self.steps[self.command_buffer[1]])/10)
                    self.command_buffer = ["back"]
                else:
                    self.handle_invalid_command(self.command_buffer[1])
        else:
            return False

        return True

    def handle_invalid_command(self, val):
        if val == "text":
                self.state = "text"
                self.command_buffer = []
        elif val in self.commands:
            self.command_buffer = [val]
            if not self.stateless_command():
                self.evaluate_command()
        else:
            self.command_buffer = []

    def evaluate_command(self):
        if self.command_buffer[0] == "up":
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
                    self.handle_invalid_command(self.command_buffer[1])
        elif self.command_buffer[0] == "south":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(0,int(self.steps[self.command_buffer[1]]))
                    self.command_buffer = ["south"]
                else:
                    self.handle_invalid_command(self.command_buffer[1])
        elif self.command_buffer[0] == "east" or self.command_buffer[0] == "is":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(int(self.steps[self.command_buffer[1]]),0)
                    self.command_buffer = ["east"]
                else:
                    self.handle_invalid_command(self.command_buffer[1])
        elif self.command_buffer[0] == "west":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in self.steps:
                    moveMouse(-1*int(self.steps[self.command_buffer[1]]),0)
                    self.command_buffer = ["west"]
                else:
                    self.handle_invalid_command(self.command_buffer[1])
        elif self.command_buffer[0] == "mouse" or self.command_buffer[0] == "sir" or self.command_buffer[0] == "serf":
            if len(self.command_buffer) >= 2:
                if self.command_buffer[1] in ["up","down","left","right"]:
                    if len(self.command_buffer) >= 3: 
                        if self.command_buffer[2] in self.steps:
                            if self.command_buffer[1] == "up":
                                scrollUp(int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["mouse","up"]
                            if self.command_buffer[1] == "down":
                                scrollUp(-1*int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["mouse","down"]
                            if self.command_buffer[1] == "left":
                                scrollRight(-1*int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["mouse","left"]
                            if self.command_buffer[1] == "right":
                                scrollRight(int(self.steps[self.command_buffer[2]]))
                                self.command_buffer = ["mouse","right"]
                        else:
                            self.handle_invalid_command(self.command_buffer[2])
                else:
                    self.handle_invalid_command(self.command_buffer[1])
        else:
            self.command_buffer = []

    def insert_punctuation(self, text):
        text = text.replace("period",".")
        text = text.replace("colon",":")
        text = text.replace("dash","-")
        text = text.replace("comma",",").replace("coma",",")
        text = text.replace("pork","?")
        text = text.replace("dot",".")
        text = text.replace("hash","#")
        text = text.replace("sem",";")
        text = text.replace("corn",":")
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
                if self.command_buffer[i] in ["period","coma","comma","corn","pork", "hash","sim"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(self.command_buffer[i]) + ' ')
                elif self.command_buffer[i] in ["dot"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(self.command_buffer[i]))
                else:
                    writeToScreen(self.command_buffer[i] + ' ')

            self.command_buffer = []