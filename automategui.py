import pyautogui

# failsafe cuases pyautogui to hang on occasion
pyautogui.FAILSAFE = False

def getImageCoord(fullpath):
    try:
        conf = 1
        loc = None
        while(loc is None):
            conf -= 0.1
            loc = pyautogui.locateOnScreen(fullpath, confidence=conf)

        point = pyautogui.center(loc)
        x, y = point
        return (x, y)
    except Exception as e:
        log.error("Pyautogui error: " + str(e))
        return None

def clickOnImage(fullpath):
    x, y = getImageCoord(fullpath)
    pyautogui.click(x, y)

def writeToScreen(text):
    pyautogui.write(text)

def doubleclickOnImage(fullpath):
    x, y = getImageCoord(fullpath)
    pyautogui.click(x, y)
    pyautogui.click(x, y)

def hotKeyPress(listOfKeys):
    pyautogui.hotkey(*listOfKeys)

def moveMouseTo(x,y): 
    pyautogui.moveTo(x,y,.5)

def clickCurrent(): 
    pyautogui.click(pyautogui.position())

def doubleClickCurrent(): 
    pyautogui.click(pyautogui.position())
    pyautogui.click(pyautogui.position())

def tripleClickCurrent(): 
    pyautogui.click(pyautogui.position())
    pyautogui.click(pyautogui.position())
    pyautogui.click(pyautogui.position())

def rightClickCurrent():
    pyautogui.rightClick(pyautogui.position())

def holdDownLeft():
    pyautogui.mouseDown(button='left')

def releaseLeftMouse():
    pyautogui.mouseUp(button='left')

def getPosition():
    return pyautogui.position()

def leftDragMouse(x,y):
    pyautogui.dragTo(x,y,1, button='left') 

def scrollVertical(y):
    pyautogui.scroll(y)

def scrollHorizontal(x):
    pyautogui.scroll(x)

def moveMouseRelative(x,y):
    pyautogui.moveRel(x,y)

def getScreenSize():
    return pyautogui.size()
