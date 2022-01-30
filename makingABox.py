
from operator import length_hint
from this import d
from vpython import *
from time import *
#tamaños
mRadius = .5
wallThickness = .1
roomWidth = 10
roomDepth = 10
roomHeight = 10
floor = box(pos=vector(0, - roomHeight / 2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth), opacity = 0.1)
ceiling = box(pos=vector(0, roomHeight / 2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth), opacity = 0.1)
leftWall = box(pos=vector(- roomWidth / 2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth), opacity = 0.1)
rigthWall = box(pos=vector( roomWidth / 2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth), opacity = 0.1)
backWall = box(pos=vector(0, 0, - roomDepth / 2), color=color.white, size=vector(roomWidth, roomHeight, wallThickness), opacity = 0.1)
frontWall = box(pos=vector(0, 0, roomDepth / 2), color=color.white, size=vector(roomWidth, roomHeight, wallThickness), opacity = 0.1)
marble = sphere(pos=vector(- (roomWidth / 2) + mRadius, 0,0), color=color.green, radius = mRadius
                , make_trail= True, trail_type = 'points', interval = .1, retain = 50)
#calculos de posicion
deltaX = (roomHeight / 2) / 10
deltaY =  - (roomHeight / 2) / 10
deltaZ = (roomHeight / 2) / 10
xPos = 0
yPos =  (roomHeight / 2) - mRadius
zPos = - (roomDepth / 2) + mRadius
while True:
    rate(10)
    xPos += deltaX
    yPos += deltaY
    zPos += deltaZ
    if xPos > (roomWidth / 2) - (mRadius + wallThickness)  or xPos  < - (roomWidth / 2) + (mRadius + wallThickness):
        #xPos *= -1 con esto literalmente hacemos q cuando atraviese la pared salga desde la pared contraria xD
        deltaX *= -1
        #con esto hacemos q vuelva hacia el otro lado
    if yPos > (roomHeight / 2) - (mRadius + wallThickness) or yPos < - (roomHeight / 2) + (mRadius + wallThickness):
        deltaY *= -1
    if zPos > (roomDepth / 2) - (mRadius + wallThickness) or zPos < - (roomDepth / 2) + (mRadius + wallThickness):
        deltaZ *= -1
    marble.pos = vector(xPos, yPos, zPos)