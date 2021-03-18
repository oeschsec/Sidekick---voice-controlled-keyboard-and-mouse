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
from automategui import *
import time


def hoverTaskBar():
    moveMouseTo(0, 0)


def openChrome():
    hoverTaskBar()


def click():
    clickCurrent()


def rightclick():
    rightClickCurrent()


def holdLeft():
    holdDownLeft()


def position():
    return getPosition()


def releaseLeft():
    releaseLeftMouse()


def doubleclick():
    doubleClickCurrent()


def holdKeyDown(key):
    holdKey(key)


def keyUp(key):
    releaseKey(key)


def dragMouse(x, y):
    leftDragMouse(x, y)


def tripleclick():
    tripleClickCurrent()


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
        hotKeyPress(["backspace"])


def hitEnter():
    hotKeyPress(["enter"])


def hitSpace():
    hotKeyPress(["space"])


def hitTab():
    hotKeyPress(["tab"])


def moveMouse(x, y):
    moveMouseRelative(x, y)


def moveMouseAbs(x, y):
    moveMouseTo(x, y)


def screenSize():
    return getScreenSize()
