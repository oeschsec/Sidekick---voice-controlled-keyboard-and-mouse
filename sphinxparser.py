'''
Because the local sphinx parser is less accurate than google, can't use the same commands. 

Recommended to only use this class when Internet is not avaiable.
'''
from actions import *

def act_sphinx(text, words):
    if words[0].lower() == "click":
        click()
    elif words[0].lower() == "hit":
        if words[1] == "enter": 
            hitEnter()
    elif words[0] == "space":
        hitSpace()
    elif words[0].lower() == "backspace":
        if len(words) > 1:
            backspace(words[1])
        else:
            backspace(1)
    elif words[0].lower() == "scroll":
        if words[1] == "up":
            if len(words) > 2:
                if words[2] == "surf":
                    surfScrollUp(20)
                else:
                    scrollUp(20)
            else:
                scrollUp(10)
        elif words[1] == "down":
            if len(words) > 2:
                if words[2] == "surf":
                    surfScrollUp(-20)
                else:
                    scrollUp(-20)
            else:
                scrollUp(-10)
    else:
        writeToScreen(text)