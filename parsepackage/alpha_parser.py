from actions import *
import string

class AlphaParser: 
    
    def __init__(self, system):
        self.os = system
        self.numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        self.punctuation = ["period","colon","dash","comma","question","dot","hash","semicolon","bang","cap","exclamation"]
        self.keywords = list(string.ascii_lowercase) + self.punctuation + self.numbers

    def word_to_int(self, word):
        mapping = { 
            'one': '1', 
            'two': '2', 
            'three': '3', 
            'four': '4', 
            'five': '5', 
            'six': '6', 
            'seven': '7', 
            'eight': '8', 
            'nine': '9'
        } 
        return mapping[word]

    def insert_punctuation(self, text):
        text = text.replace("period",".")
        text = text.replace("colon",":")
        text = text.replace("dash","-")
        text = text.replace("comma",",")
        text = text.replace("question","?")
        text = text.replace("dot",".")
        text = text.replace("hash","#")
        text = text.replace("semi",";")
        text = text.replace("bang","!").replace("exclamation","!")
        return text

    def evaluate_text(self, command_buffer):        
        if command_buffer[0] == "cap": # capitalize next word spoken
            if len(command_buffer) >= 2:
                writeToScreen(command_buffer[1].capitalize())
                if len(command_buffer) > 2:
                    command_buffer = command_buffer[2:]
                else:
                    command_buffer = []
        else:
            for i in range(0,len(command_buffer)): 
                # some punctuation includes backspace and space after - other does not
                if command_buffer[i] in self.punctuation:
                    writeToScreen(self.insert_punctuation(command_buffer[i]))
                elif command_buffer[i] in self.numbers:
                    writeToScreen(self.word_to_int(command_buffer[i]))
                else:
                    writeToScreen(command_buffer[i])

            command_buffer = []
        
        return command_buffer
