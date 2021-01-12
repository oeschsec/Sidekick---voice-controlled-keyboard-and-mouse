from actions import *

class CommandParser: 
    
    def __init__(self, system, steps):
        self.os = system
        self.steps = steps

        self.stateless_commands = ["click","go","double","enter","space","back"]
        self.commands = ["up","down","left","right","copy","paste","north","south","east","west","save","scroll"]

    def stateless_command(self, command_buffer):
        if (command_buffer[0] == "click" or command_buffer[0] == "go"):
            click()
            command_buffer = []
        elif command_buffer[0] == "double":
            doubleclick()
            command_buffer = []
        elif (command_buffer[0] == "inter" or command_buffer[0] == "enter"):
            hitEnter()
            command_buffer = []
        elif command_buffer[0] == "space":
            hitSpace()
            command_buffer = []
        elif command_buffer[0] == "back":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    backspace(int(self.steps[command_buffer[1]])/10)
                    command_buffer = ["back"]
                else:
                    return [True, self.handle_invalid_command(command_buffer[1], command_buffer)]
        else:
            return [False, command_buffer]

        return [True, command_buffer]

    def handle_invalid_command(self, val, command_buffer):
        if val in self.commands or val in self.stateless_commands:
            command_buffer = [val]
            if not self.stateless_command(command_buffer)[0]:
                self.evaluate_command(command_buffer)
        else:
            command_buffer = []

        return command_buffer

    def evaluate_command(self, command_buffer):
        if command_buffer[0] == "up":
            hotKeyPress(["up"])
            command_buffer = []
        elif command_buffer[0] == "down":
            hotKeyPress(["down"])
            command_buffer = []
        elif command_buffer[0] == "left":
            hotKeyPress(["left"])
            command_buffer = []
        elif command_buffer[0] == "right":
            hotKeyPress(["right"])
            command_buffer = []
        elif command_buffer[0] == "copy":
            if self.os == "Darwin":
                hotKeyPress(["command","c"])            
            else:
                hotKeyPress(["ctrl","c"])        
            command_buffer = []
        elif command_buffer[0] == "paste":
            if self.os == "Darwin":
                hotKeyPress(["command","v"])            
            else:
                hotKeyPress(["ctrl","v"])
            command_buffer = []
        elif command_buffer[0] == "save" or command_buffer[0] == "say":
            if self.os == "Darwin":
                hotKeyPress(["command","s"])            
            else:
                hotKeyPress(["ctrl","s"])
            command_buffer = []
        elif command_buffer[0] == "north":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(0,-1*int(self.steps[command_buffer[1]]))
                    command_buffer = ["north"]
                else:
                    return self.handle_invalid_command(command_buffer[1], command_buffer)
        elif command_buffer[0] == "south":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(0,int(self.steps[command_buffer[1]]))
                    command_buffer = ["south"]
                else:
                    return self.handle_invalid_command(command_buffer[1], command_buffer)
        elif command_buffer[0] == "east" or command_buffer[0] == "is":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(int(self.steps[command_buffer[1]]),0)
                    command_buffer = ["east"]
                else:
                    return self.handle_invalid_command(command_buffer[1], command_buffer)
        elif command_buffer[0] == "west":
            if len(command_buffer) >= 2:
                if command_buffer[1] in self.steps:
                    moveMouse(-1*int(self.steps[command_buffer[1]]),0)
                    command_buffer = ["west"]
                else:
                    return self.handle_invalid_command(command_buffer[1], command_buffer)
        elif command_buffer[0] == "scroll" or command_buffer[0] == "surf":
            if len(command_buffer) >= 2:
                if command_buffer[1] in ["up","down","left","right"]:
                    if len(command_buffer) >= 3: 
                        if command_buffer[2] in self.steps:
                            if command_buffer[1] == "up":
                                scrollUp(int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll","up"]
                            if command_buffer[1] == "down":
                                scrollUp(-1*int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll","down"]
                            if command_buffer[1] == "left":
                                scrollRight(-1*int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll","left"]
                            if command_buffer[1] == "right":
                                scrollRight(int(self.steps[command_buffer[2]]))
                                command_buffer = ["scroll","right"]
                        else:
                            return self.handle_invalid_command(command_buffer[2], command_buffer)
                else:
                    return self.handle_invalid_command(command_buffer[1], command_buffer)
        else:
            command_buffer = []

        return command_buffer
