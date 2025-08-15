import pyautogui as pg
import time

print("program will run after 5 second")
time.sleep(5)
print("running")

for i in range(100):
    pg.write("I Love You")
    time.sleep(0.5)
    pg.press("Enter")
