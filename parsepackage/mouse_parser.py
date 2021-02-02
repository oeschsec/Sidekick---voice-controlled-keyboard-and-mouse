from actions import *
import threading
import math

class MouseParser: 
    
    def __init__(self, system, steps):
        self.mouseStarted = False
        self.os = system
        self.steps = steps

        self.commands = ["stop","snail","slow","fast","medium","up","down","counter","clock","north","south","east","west","one","two","three","four","northeast","northwest","southeast","southwest"]

    def evaluate_mouse(self, command_buffer):
        if not self.mouseStarted:
            self.stopMouse = False
            self.magnitude = 5 # in pixels
            self.sleep = .2
            self.setMouseCoord(90)

        if len(command_buffer) > 0:
            if "stop" in command_buffer[0]:
                self.stopMouse = True
                command_buffer = []
                return [command_buffer,"command"]
            elif "snail" in command_buffer[0]:
                self.magnitude = 5
                self.sleep = .2
                self.setMouseCoord(self.currentangle)
            elif "slow" in command_buffer[0]:
                self.magnitude = 15
                self.sleep = .2
                self.setMouseCoord(self.currentangle)
            elif "fast" in command_buffer[0]:
                self.magnitude = 50
                self.sleep = .5
                self.setMouseCoord(self.currentangle)
            elif "medium" in command_buffer[0]:
                self.magnitude = 25
                self.sleep = .3
                self.setMouseCoord(self.currentangle)
            elif "up" in command_buffer[0] or "counter" in command_buffer[0]:
                self.setMouseCoord(self.currentangle + 15)
            elif "down" in command_buffer[0] or "clock" in command_buffer[0]:
                self.setMouseCoord(self.currentangle - 15)
            elif "north" in command_buffer[0]:
                self.setMouseCoord(90)
            elif "south" in command_buffer[0]:
                self.setMouseCoord(270)
            elif "east" in command_buffer[0]:
                self.setMouseCoord(0)
            elif "west" in command_buffer[0]:
                self.setMouseCoord(180)
            elif "northeast" in command_buffer[0] or "one" in command_buffer[0]:
                self.setMouseCoord(35)
            elif "northwest" in command_buffer[0] or "two" in command_buffer[0] or "too" in command_buffer[0]:
                self.setMouseCoord(135)
            elif "southwest" in command_buffer[0] or "three" in command_buffer[0]:
                self.setMouseCoord(225)
            elif "southeast" in command_buffer[0] or "four" in command_buffer[0]  or "for" in command_buffer[0]:
                self.setMouseCoord(315)

            command_buffer = []

            if not self.mouseStarted:
                self.startMouse() 

        return [command_buffer,"mouse"]


    def startMouse(self):
        thread = threading.Thread(target=self.mouse_thread)
        thread.daemon = True
        thread.start()
        self.mouseStarted = True

    def setMouseCoord(self,degrees):
        self.currentangle = degrees
        self.x = self.magnitude * math.cos(math.radians(degrees))
        self.y = -1*self.magnitude * math.sin(math.radians(degrees))

        #if self.os == "Darwin":
        #    self.y = -1*self.magnitude * math.sin(math.radians(degrees))
        #else:
        #    self.y = self.magnitude * math.sin(math.radians(degrees))    

    def mouse_thread(self):
        while True:
            if self.stopMouse:
                self.mouseStarted = False
                break
            else:
                moveMouse(self.x,self.y)
                time.sleep(self.sleep)

