
import pyautogui
import time
from tkinter import *
import keyboard

pyautogui.PAUSE = 0


def loco():
    while keyboard.is_pressed('l') == False:
        time.sleep(3.0)
        pyautogui.dragTo(926, 982, button='left')
        time.sleep(.5)
        pyautogui.click()
        time.sleep(5.0)
        pyautogui.dragTo(796, 915, button='left')
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(1)
        pyautogui.dragTo(964, 810, button='left')
        time.sleep(1.0)
        pyautogui.click()

        pyautogui.dragTo(1135, 921, button='left')
        time.sleep(0.5)
        pyautogui.doubleClick()
        pyautogui.dragTo(964, 810, button='left')
        time.sleep(5)
        pyautogui.dragTo(950, 12, button='left')
        time.sleep(20)



def macro():
    while keyboard.is_pressed('l') == False:
        time.sleep(3)
        pyautogui.keyDown('w')
        time.sleep(.5)
        pyautogui.keyUp('w')
        time.sleep(.5)
        pyautogui.keyDown('a')
        time.sleep(.5)
        pyautogui.keyUp('a')
        time.sleep(.5)
        pyautogui.keyDown('s')
        time.sleep(.5)
        pyautogui.keyUp('s')
        time.sleep(.5)
        pyautogui.keyDown('d')
        time.sleep(.5)
        pyautogui.keyUp('d')



def tkinterd():
    root = Tk()
    # root.iconbitmap('E:\Anser_cygnoides (1).ico')
    root.geometry("600x400")
    root.configure(bg='black')
    launcha = Button(root, text="Start", command=loco and macro,  bg='green')
    launcha.place(x=300, y=200)
    #macrod = Button(root, text="Macro", command=macro, bg='red')
    #macrod.place(x=400, y=200)
    root.title("AfK in your sleep")
    root.mainloop()
tkinterd()

"Yours truly nkcells"