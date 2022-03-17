
import random

import pyautogui as pg

import time



animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat' )

time.sleep(10)


for i in range (1,1000):

    a  = random.choice(animal)

    pg.write('You Are a ' + a)

    pg.press('enter')
