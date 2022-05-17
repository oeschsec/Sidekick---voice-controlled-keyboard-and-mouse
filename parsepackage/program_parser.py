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
from click import command
from actions import *
import string


class ProgramParser:
    def __init__(self, system):
        self.os = system
        self.numbers = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        self.punctuation = [
            "ren",
            "len",
            "rack",
            "equals",
            "lack",
            "period",
            "colon",
            "dash",
            "comma",
            "underscore",
            "question",
            "dot",
            "hash",
            "semicolon",
            "bang",
            "cap",
            "exclamation",
            "quote",
            "single",
            "if",
            "while", 
            "for", 
            "and", 
            "or",
            "mod"
        ]
        self.keywords = list(string.ascii_lowercase) + self.punctuation + self.numbers

    def word_to_int(self, word):
        mapping = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        return mapping[word]

    def insert_punctuation(self, text):
        if text == "period":
            text = text.replace("period", ".")
        elif text == "equals":
            text = text.replace("equals", "==")
        elif text == "ren":
            text = text.replace("ren", ")")
        elif text == "len":
            text = text.replace("len", "(")
        elif text == "lack":
            text = text.replace("lack", "[")
        elif text == "rack":
            text = text.replace("rack", "]")
        elif text == "colon":
            text = text.replace("colon", ":")
        elif text == "dash":
            text = text.replace("dash", "-")
        elif text == "comma":
            text = text.replace("comma", ",")
        elif text == "question":
            text = text.replace("question", "?")
        elif text == "dot":
            text = text.replace("dot", ".")
        elif text == "quote":
            text = text.replace("quote", '"')
        elif text == "hash":
            text = text.replace("hash", "#")
        elif text == "single":
            text = text.replace("single", "'")
        elif text == "underscore":
            text = text.replace("underscore", "_")
        elif text == "semicolon":
            text = text.replace("semicolon", ";")
        elif text == "bang" or text == "exclamation":
            text = text.replace("bang", "!").replace("exclamation", "!")
        elif text == "if":
            text = text.replace("if", "if ():\n")
        elif text == "while":
            text = text.replace("while", "while ():\n")
        elif text == "for":
            text = text.replace("for", "for ():\n")
        elif text == "and":
            text = text.replace("and", "&&")
        elif text == "or":
            text = text.replace("or", "||")
        elif text == "mod":
            text = text.replace("mod", "%")
        elif text == "assign":
            text = text.replace("assign", "==")
        elif text == "same":
            text = text.replace("same", "===")

        return text

    def evaluate_text(self, command_buffer):
        if command_buffer[0] == "cap":  # capitalize next word spoken
            if len(command_buffer) >= 2:
                writeToScreen(command_buffer[1].capitalize())
                if len(command_buffer) > 2:
                    command_buffer = command_buffer[2:]
                else:
                    command_buffer = []
        else:
            for i in range(0, len(command_buffer)):
                # some punctuation includes backspace and space after - other does not
                if command_buffer[i] in self.punctuation:
                    writeToScreen(self.insert_punctuation(command_buffer[i]))
                elif command_buffer[i] in self.numbers:
                    writeToScreen(self.word_to_int(command_buffer[i]))
                else:
                    writeToScreen(command_buffer[i])

            command_buffer = []

        return command_buffer