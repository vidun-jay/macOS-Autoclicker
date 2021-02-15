#!/usr/bin/env python
__author__ = "Vidun Jayakody"
__copyright__ = "Copyright 2021 Vidun Jayakody. All rights reserved."
__date__ = '13/02/2021'
__version__ = "1.0"

# imports
from sys import breakpointhook
from tkinter import *
import tkinter as tk
import threading
import pyautogui
import time

# sets the 'stop' state to False by default
stopPressed = False

# create GUI
root = tk.Tk()
root.title("Vidun's Autoclicker")
root.minsize(300,100)
root.geometry("300x100+450+250")

# start function
def start():
    time.sleep(3) # 3 second count down before it starts

    # loop that clicks where the mouse currently is and waits 1 second
    while stopPressed == False:
        pyautogui.click(x=None, y=None)
        time.sleep(1)
        
# function that calls start() as a background process        
def startDaemon():

    global stopPressed # referencing the global variable, not creating a new local one'
    stopPressed = False # when the start button is pressed again, reset stopPressed to False again

    th = threading.Thread(target=start)
    th.daemon = True
    th.start()

# if the stop button is pressed, set stopPressed = to True, stopping the loop
def stop():
    global stopPressed
    stopPressed = True

# makes start button
startAutoClicker = Button(root, padx=50, text='clikc', pady=10, command=startDaemon)
startAutoClicker.pack(side=LEFT, padx=10, pady=10)

# makes stop button
stopAutoClicker = Button(root, padx=50, text='no', pady=10, command=stop)
stopAutoClicker.pack(side=RIGHT, padx=10, pady=10)

root.mainloop()