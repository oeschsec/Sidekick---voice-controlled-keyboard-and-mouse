from actions import *

class TextParser: 
    
    def __init__(self, system, steps):
        self.os = system
        self.steps = steps
        self.space = " "
        self.tocap = ["i"]

    def evaluate_text(self, command_buffer): 
        if command_buffer[0] == "spaces":
            self.space = " "    
            command_buffer = []
        elif command_buffer[0] == "pack":
            self.space = ""
            command_buffer = []
        elif command_buffer[0] == "cap": # capitalize next word spoken
            if len(command_buffer) >= 2:
                writeToScreen(self.space + command_buffer[1].capitalize())
                if len(command_buffer) > 2:
                    command_buffer = command_buffer[2:]
                else: 
                    command_buffer = []
        else:
            for i in range(0,len(command_buffer)): 
                if command_buffer[i] in self.tocap:
                    writeToScreen(self.space + command_buffer[i].capitalize())   
                else: 
                    writeToScreen(self.space + command_buffer[i])

            command_buffer = []
            
        return command_buffer