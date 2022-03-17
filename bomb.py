
import random
import pyautogui as pg
import time


animal = ('Dog', 'Monkey', 'Cow', 'Buffalow' , 'Elephant', 'Donkey', 'Cat' )

time.sleep(1)

for i in range (5):
    a  = random.choice(animal)
    pg.write('You Are a ' + a + ' ')
    pg.write(r'\U0001f600')  #emoji
    pg.press('enter')
  