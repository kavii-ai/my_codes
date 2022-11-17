import pyautogui as pg
import time
import random,string
count =1
while count <=51:
    pg.click(477,692)
    time.sleep(0.1)
    pg.write("woah this is week1!!") 
    # time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
    count +=1
