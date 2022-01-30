from vpython import *

#tamaños
mRadius = .5
wallThickness = .1
roomWidth = 100
roomDepth = 100
roomHeight = 100

class tele:

    floor = box(pos=vector(0, - roomHeight / 2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth), texture = 'DEMEN.jpg')
    ceiling = box(pos=vector(0, roomHeight / 2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth), texture = 'sorry.jpg')
    leftWall = box(pos=vector(- roomWidth / 2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth), texture = 'costadotele.jpg')
    rigthWall = box(pos=vector( roomWidth / 2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth), texture = 'costadotelederecha.jpg')
    backWall = box(pos=vector(0, 0, - roomDepth / 2), color=color.white, size=vector(roomWidth, roomHeight, wallThickness), texture = 'teleatras.jpg')
    frontWall = box(pos=vector(0, 0, roomDepth / 2), color=color.white, size=vector(roomWidth, roomHeight, wallThickness), texture = 'caratele.png')

class control:

    control = box(pos=vector(-60, -40, 100), color=color.white, size=vector(10, 30, 4), texture = 'control.png')