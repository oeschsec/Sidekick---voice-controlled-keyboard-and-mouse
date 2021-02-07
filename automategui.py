import pyautogui

# failsafe can cause hanging
pyautogui.FAILSAFE = False


def writeToScreen(text):
    pyautogui.write(text)


def hotKeyPress(listOfKeys):
    pyautogui.hotkey(*listOfKeys)


def moveMouseTo(x, y):
    pyautogui.moveTo(x, y, 0.5)


def clickCurrent():
    pyautogui.click(pyautogui.position())


def doubleClickCurrent():
    pyautogui.click(pyautogui.position())
    pyautogui.click(pyautogui.position())


def tripleClickCurrent():
    pyautogui.click(pyautogui.position(),clicks=3)


def rightClickCurrent():
    pyautogui.rightClick(pyautogui.position())


def holdDownLeft():
    pyautogui.mouseDown()


def releaseLeftMouse():
    pyautogui.mouseUp()


def getPosition():
    return pyautogui.position()


def leftDragMouse(x, y):
    pyautogui.dragTo(x, y, 1, button="left")


def scrollVertical(y):
    pyautogui.scroll(y)


def scrollHorizontal(x):
    pyautogui.scroll(x)


def moveMouseRelative(x, y):
    pyautogui.moveRel(x, y)


def getScreenSize():
    return pyautogui.size()
