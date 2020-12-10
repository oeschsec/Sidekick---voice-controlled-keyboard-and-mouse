
from actions import *

def act_google(text, words):
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
    elif words[0].lower() == "north":
        moveMouse(0,-1*int(words[1]))
    elif words[0].lower() == "south":
        moveMouse(0,int(words[1]))
    elif words[0].lower() == "east":
        moveMouse(int(words[1]),0)
    elif words[0].lower() == "west":
        moveMouse(-1*int(words[1]),0)
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