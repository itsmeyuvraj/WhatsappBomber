
import random
import pyautogui as pg
import time

animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat' )


for i in range (1,1000):
    a  = random.choice(animal)
    pg.write('You Are a ' + a)
    pg.write('U+1F47F')  #emoji 
    pg.press('enter')
    time.sleep(10)
