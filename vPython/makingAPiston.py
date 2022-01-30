from operator import length_hint
from vpython import *
import numpy as np
piston1 = cylinder(pos=vector(-5,0,0) , radius = 1, length = 3, color=color.red, opacity = .5)
while 1:
    for myLength in np.linspace(1, 6, 1000):
        rate(1000)
        piston1.length = myLength
    for myLength in np.linspace(6, 1, 1000):
        rate(1000)
        piston1.length = myLength