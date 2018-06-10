import pyautogui
from time import sleep
from msvcrt import getch

def keypress():
    return ord(getch())

print("Warning: do not run it from idle, directly run it or run it from terminal.")

ins = raw_input("press enter and place your mouse within 3 secs...")
print("You press ", ins)

if ins == "":
    sleep(3)
    x,y = pyautogui.position()
    print("Click position =",x,y)

while True:
    print("Clicking started, press ESC to escape")
    if keypress() == 27:
        break
    pyautogui.click(x,y)
