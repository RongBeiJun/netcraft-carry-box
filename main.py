# 截图整个桌面
from win32 import win32gui
import win32ui
import win32con
import win32api
import cv2
from PIL import Image
import pyautogui
import keyboard
import time
import numpy as np
pyautogui.PAUSE = 0.002

gps = cv2.imread("gps.png")
nx, ny = gps.shape[:2]
px, py = 0.0, 0.0
def check(cimg):
    xy = pyautogui.locateOnScreen(cimg, confidence=0.6)
    if xy :
        x,y = pyautogui.center(xy)
        print(x,y)
        return x,y
    else:
        x=65535
        y=65535
        print("chack faild")
        return x,y
def check_two():
    time.sleep(0.05)
    x,y=check("max.png")
    if x!=65535 :
        pyautogui.moveTo(x,y)
        pyautogui.click()
        pyautogui.click()
    # time.sleep(0.02)
    x,y=check("button.png")
    if x!=65535 :
        pyautogui.moveTo(x,y)
        pyautogui.click()
    pyautogui.moveTo(px,py)
    pass
def udlr_move(x):
    global px,py
    # if x.event_type == 'down' and x.name == "w":
    #     pyautogui.move(0,-ny)
    #     py=py-ny
    #     print("down w")

    # if x.event_type == 'down' and x.name == "a":
    #     pyautogui.move(-nx,0)
    #     px=px-nx
    #     print("down a")

    # if x.event_type == 'down' and x.name == "s":
    #     pyautogui.move(0,ny)
    #     py=py+ny
    #     print("down s")

    # if x.event_type == 'down' and x.name == "d":
    #     pyautogui.move(nx,0)
    #     px=px+nx
    #     print("down d")
    if x.event_type == 'down' and x.name == "tab":
        px,py=pyautogui.position()
        pyautogui.click()
        check_two()
        time.sleep(0.5)
    # if x.event_type == 'down' and x.name == "ctrl":
    #     x,y=check("point.png")
    #     if x!=65535 :
    #         pyautogui.moveTo(x,y)
    #         px,py=x,y
    if x.event_type == 'down' and x.name == "ctrl":
        px,py=pyautogui.position()
    pass
# def udlr_cw():
#     global px,py
#     pyautogui.move(0,-ny)
#     pyautogui.click()
#     py=py-ny
#     check_two()
#     print("down w")

#     pass
# def udlr_ca():
#     global px,py
#     pyautogui.move(-nx,0)
#     pyautogui.click()
#     px=px-nx
#     check_two()
#     print("down a")
#     pass    
# def udlr_cs():
#     global px,py
#     pyautogui.move(0,ny)
#     pyautogui.click()
#     py=py+ny
#     check_two()
#     print("down s")
#     pass
# def udlr_cd():
#     global px,py
#     pyautogui.move(nx,0)
#     pyautogui.click()
#     px=px+nx
#     check_two()
#     print("down d")
#     pass
if __name__=="__main__":
    win32api.MessageBox(0, "F6启动停止\nCtrl自定义鼠标点(先将鼠标移至点位)\nTab存箱", "Readme",win32con.MB_ICONASTERISK)
    keyboard.wait('f6')

    # x,y=check("point.png")
    # if x!=65535 :
    #     pyautogui.moveTo(x,y)
    #     px,py=x,y
    px,py=pyautogui.position()
    keyboard.hook(udlr_move)
    # keyboard.add_hotkey('shift+w',udlr_cw)
    # keyboard.add_hotkey('shift+a',udlr_ca)
    # keyboard.add_hotkey('shift+s',udlr_cs)
    # keyboard.add_hotkey('shift+d',udlr_cd)

    keyboard.wait('f6')
