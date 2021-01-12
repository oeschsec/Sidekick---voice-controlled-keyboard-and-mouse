from actions import *

class TextParser: 
    
    def __init__(self, system, steps):
        self.os = system
        self.steps = steps

    def insert_punctuation(self, text):
        text = text.replace("period",".")
        text = text.replace("colon",":").replace("colin",":")
        text = text.replace("dash","-")
        text = text.replace("comma",",").replace("coma",",")
        text = text.replace("q","?")
        text = text.replace("dot",".")
        text = text.replace("hash","#")
        text = text.replace("semi",";")
        return text

    def evaluate_text(self, command_buffer):        
        if "cap" in command_buffer[0]:
            if len(command_buffer) >= 2:
                writeToScreen(command_buffer[1].capitalize() + ' ')
                if len(command_buffer) > 2:
                    command_buffer = command_buffer[2:]
                else:
                    command_buffer = []
        else:
            for i in range(0,len(command_buffer)):
                if command_buffer[i] in ["period","coma","comma","colon","colin","q","semi"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(command_buffer[i]) + ' ')
                elif command_buffer[i] in ["hash", "dash"]:
                    writeToScreen(self.insert_punctuation(command_buffer[i]))
                elif command_buffer[i] in ["dot"]:
                    backspace(1)
                    writeToScreen(self.insert_punctuation(command_buffer[i]))
                else:
                    writeToScreen(command_buffer[i] + ' ')

            command_buffer = []
            return command_buffer