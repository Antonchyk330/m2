'''
А тепер перед Вами програма робота-маляра: 
програма запитує колір, яким треба намалювати лінію. 
Зараз робот вміє малювати тільки червону лінію, 
навчіть його малювати також синю (blue) і зелену (green) лінії.
'''

from turtle import *
turtle_color = input("Який колір використовувати, червоний, синій чи зелений?")
if turtle_color == "червоний":
    color("red")
elif turtle_color == "синій":
    color("blue")
else:
    color("green")
forward(100)
exitonclick()
