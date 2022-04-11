import re
import numpy as np
import cv2
import pyautogui
from PIL import Image, ImageDraw
import time


def get_pos(width):
    #There are 11 gridlines for x and y
    line_space = np.round_(width/11, 0)
    x_pos = []
    count = 0
    for i in range(1, 11):
        count += line_space 
        x_pos.append(count)
    return x_pos



#Set the resolution, probably want this to be changable 


#Create the gridlines
def create_gridlines(w, h):
    x_pos = get_pos(w)
    y_pos = get_pos(h)
    new_image = Image.new(mode='RGBA', size=(w, h), color=(255,255,255,0))
    for x in x_pos:
        draw = ImageDraw.Draw(new_image)
        #x = new_image.width / 2
        y0 = 0
        y1 = new_image.height
        line = ((x, y0), (x, y1))
        draw.line(line, fill="red", width=2)
        del draw

    for y in y_pos:
        draw = ImageDraw.Draw(new_image)
        #x = new_image.width / 2
        x0 = 0
        x1 = new_image.width
        line = ((x0, y), (x1, y))
        draw.line(line, fill="red", width=3)
        del draw
    new_image.save("Images/{}x{}_grid.png".format(w,h))
    return "Images/{}x{}_grid.png".format(w,h)



#https://www.geeksforgeeks.org/how-to-take-screenshots-using-python/
#https://www.geeksforgeeks.org/overlay-an-image-on-another-image-in-python/
#https://www.codegrepper.com/code-examples/python/display+image+python+small+screen

def take_screenshot(w, h, grid_file):
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)    
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    cv2.imwrite("Images/screenshot.png", image)
    im1 = Image.open("Images/screenshot.png").convert("RGBA")
    im2 = Image.open(grid_file).convert("RGBA")
    im1.paste(im2, (0,0), mask = im2)
    # Displaying the image
    im1.save("Images/tmp.png")
    im = cv2.imread("Images/tmp.png") 
    imS = cv2.resize(im, (w, h))                  
    cv2.imshow("output", imS)
    k = cv2.waitKey(1000)  
    cv2.destroyAllWindows()
    exit()