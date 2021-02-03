from automategui import *
import time

def hoverTaskBar():
    moveMouseTo(0,0)

def openChrome():
    hoverTaskBar()

def click():
    clickCurrent()

def rightclick():
    rightClickCurrent()

def doubleclick():
    doubleClickCurrent()

def scrollUp(y):
    scrollVertical(y)

def surfScrollUp(y):
    for i in range(5): 
        scrollVertical(y)
        time.sleep(1)

def scrollRight(x): 
    scrollHorizontal(x)

def backspace(n):
    for i in range(int(n)):
        hotKeyPress(['backspace'])

def hitEnter():
    hotKeyPress(['enter'])

def hitSpace():
    hotKeyPress(['space'])

def hitTab():
    hotKeyPress(['tab'])

def moveMouse(x,y):
    moveMouseRelative(x,y)

def moveMouseAbs(x,y):
    moveMouseTo(x,y)

def screenSize():
    return getScreenSize()

    
