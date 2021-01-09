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

def doubleClickOnImage(fullpath):
    x, y = getImageCoord(fullpath)
    pyautogui.click(x, y)
    pyautogui.click(x, y)

def hotKeyPress(listOfKeys):
    pyautogui.hotkey(*listOfKeys)

def moveMouseTo(x,y): 
    pyautogui.moveTo(x,y)

def moveMouse(x,y):
    pyautogui.move(x,y,.3)

def clickCurrent(): 
    pyautogui.click(pyautogui.position())

def doubleClickCurrent():
    pyautogui.doubleClick(pyautogui.position())

def scrollVertical(y):
    pyautogui.scroll(y)

def scrollHorizontal(x):
    pyautogui.scroll(x)

def moveMouseRelative(x,y):
    pyautogui.moveRel(x,y)