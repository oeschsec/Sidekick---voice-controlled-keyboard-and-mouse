'''
Copyright (C) 2021 The Sidekick Contributors

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
'''
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
