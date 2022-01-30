
from operator import length_hint
from vpython import *
from time import *
floor= box(pos=vector(0, -5, 0),color=color.white, length=10, height=.1, width=10)
ceiling= box(pos=vector(0, 5, 0), color=color.white, length=10, height=.1, width=10)
leftWall= box(pos=vector(-5, 0, 0), color=color.white, length= .1, height= 10, width=10, texture = 'barack_obama.jpg')
rigthWall= box(pos=vector(5, 0, 0), color=color.white, length= .1, height= 10, width=10)
backWall= box(pos=vector(0, 0, -5), color=color.white, length= 10, height= 10, width=.1)
marble = box(color=color.black, length = 3, height = 3, width = 3)
while True:
    pass