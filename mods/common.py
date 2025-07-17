import math

def CalcBaseLength(wd, reps, layer):
    radius = 0.2 * wd + (layer - 1) * wd + 0.2 * wd # Added the buffer between layers for larger angle
    return math.sqrt(2 * math.pow(radius, 2) * (1 - math.cos(2 * math.pi / reps)))

def CalcAngle(wd, baseLength):
    return 2 * math.atan(0.5 * baseLength / (0.8 * wd))

def CalcStickLength(wd, angle=0):
    return 0.8 * wd / math.cos(angle/2)

def CalcCrossLength(baseLength, reps, multiplier=1):
    return min(20, multiplier * baseLength / reps )

def DrawHDC(pen, stickLength, crossLength):
    # draw stick
    pen.down()
    pen.fd(stickLength)
    pen.up()
    # draw cap
    pen.rt(90)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    # return the starting pos
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.rt(90)
    pen.fd(stickLength)
    pen.setheading(pen.towards(0, 0))

def DrawDC(pen, stickLength, crossLength):
    # draw stick
    pen.down()
    pen.fd(stickLength)
    pen.up()
    # draw cap
    pen.rt(90)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    # draw cross
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.rt(90)
    pen.fd(stickLength/2)
    pen.rt(50)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    # return the starting pos
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.lt(50)
    pen.fd(stickLength/2)
    pen.setheading(pen.towards(0, 0))

def DrawNoCap(pen, stickLength, crossLength):
    # draw stick
    pen.down()
    pen.fd(stickLength)
    pen.up()
    # draw cross
    pen.rt(180)
    pen.fd(stickLength * 0.35)
    pen.rt(90)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    # return the starting pos
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.lt(90)
    pen.fd(stickLength * 0.65)
    pen.setheading(pen.towards(0, 0))

def DrawTR(pen, stickLength, crossLength):
    pen.down()
    pen.fd(stickLength)
    pen.up()
    # draw cap
    pen.rt(90)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    # draw crosses
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.rt(90)
    pen.fd(stickLength * 0.45)
    pen.rt(50)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.lt(50)
    pen.fd(stickLength * 0.1)
    pen.rt(50)
    pen.fd(crossLength/2)
    pen.rt(180)
    pen.down()
    pen.fd(crossLength)
    pen.up()   
    # return the starting pos
    pen.rt(180)
    pen.fd(crossLength/2)
    pen.lt(50)
    pen.fd(stickLength * 0.45)
    pen.setheading(pen.towards(0, 0))