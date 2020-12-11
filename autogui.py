import pyautogui

# this failsafe was causing pyautogui to hang on occasion
pyautogui.FAILSAFE = False

# confidence determines how similar image match needs to be. This loop might not be necessary,
# but it ensures that some button is found before proceeding (Mostly for windows, pyautogui seems
# to have problems on that platform that do not appear on CentOS)
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

def getConfidence(fullpath):
    try:
        conf = 1
        loc = None
        while(loc is None) and conf > 0:
            conf -= 0.1
            loc = pyautogui.locateOnScreen(fullpath, confidence=conf)
        return conf
    except Exception as e:
        log.error("Pyautogui error: " + str(e))
        return 0

def clickOnImage(fullpath):
    x, y = getImageCoord(fullpath)
    pyautogui.click(x, y)

def clickBetweenImages(image1, image2):
    x1, y1 = getImageCoord(image1)
    x2, y2 = getImageCoord(image2)
    mid = (x1+x2) / 2
    pyautogui.click(mid, y1)

def doubleClickBetweenImages(image1, image2):
    x1, y1 = getImageCoord(image1)
    x2, y2 = getImageCoord(image2)
    mid = (x1+x2) / 2
    pyautogui.click(mid, y1)
    pyautogui.click(mid, y1)

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
    pyautogui.move(x,y,1)

def clickCurrent(): 
    pyautogui.click(pyautogui.position())

def scrollVertical(y):
    pyautogui.scroll(y)

def scrollHorizontal(x):
    pyautogui.scroll(x)