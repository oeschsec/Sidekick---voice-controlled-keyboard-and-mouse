
from actions import *

def act_google(text, words):
    if words[0].lower() == "click" and len(words) == 1:
        click()
    elif words[0].lower() == "hit" and len(words) == 2:
        if words[1] == "enter": 
            hitEnter()
    elif words[0] == "space" and len(words) == 1:
        hitSpace()
    elif words[0].lower() == "backspace" and (len(words) == 1 or len(words) == 2):
        if len(words) > 1:
            backspace(words[1])
        else:
            backspace(1)
    elif words[0].lower() == "north" and len(words) == 2:
        moveMouse(0,-1*int(words[1]))
    elif words[0].lower() == "south" and len(words) == 2:
        moveMouse(0,int(words[1]))
    elif words[0].lower() == "east" and len(words) == 2:
        moveMouse(int(words[1]),0)
    elif words[0].lower() == "west" and len(words) == 2:
        moveMouse(-1*int(words[1]),0)
    elif words[0].lower() == "scroll" and (len(words) == 2 or len(words) == 3):
        if words[1] == "up":
            if len(words) > 2:
                if words[2] == "surf":
                    surfScrollUp(20)
                elif words[2] == "big": 
                    surfScrollUp(50)
                elif words[2] == "huge": 
                    surfScrollUp(200)
                else:
                    scrollUp(20)
            else:
                scrollUp(10)
        elif words[1] == "down":
            if len(words) > 2:
                if words[2] == "surf":
                    surfScrollUp(-20)
                elif words[2] == "big":
                    surfScrollUp(-50)
                elif words[2] == "huge":
                    surfScrollUp(-200)
                else:
                    scrollUp(-20)
            else:
                scrollUp(-10)
    else:
        writeToScreen(text)