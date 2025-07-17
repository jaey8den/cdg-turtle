import math
from mods import common

def MT(pen, wd, reps, layer): # Space between grouped stitches
    return

def MR(pen, wd):
    r = 0.2 * wd
    pen.goto(0, -r)
    pen.down()
    pen.circle(r)

def SLST(pen, wd):
    r = 0.02 * wd
    pen.fd(r)
    pen.down()
    pen.circle(r)

def CH(pen, reps, wd):
    chainRadius = (0.8 * wd/reps) * math.cos(math.radians(45))
    pen.rt(45)
    pen.down()
    for i in range(reps):   
        pen.circle(chainRadius, 90)
        pen.rt(90)
    pen.rt(180)
    for i in range(reps):
        pen.circle(chainRadius, 90)
        pen.rt(90)

def SC(pen, wd, reps, layer):
    pen.fd(0.5 * wd)
    pen.rt(45)
    pen.fd(10)
    pen.rt(180)
    pen.down()
    pen.fd(20)
    pen.up()
    pen.rt(180)
    pen.fd(10)
    pen.rt(90)
    pen.fd(10)
    pen.rt(180)
    pen.down()
    pen.fd(20)

def HDC(pen, wd, reps, layer):
    stickLength = common.CalcStickLength(wd)
    crossLength = common.CalcCrossLength(2 * math.pi * (0.2 * wd + layer * wd)/reps, 1, 0.8) # Ensure sum of cross length is smaller than layer circumference
    pen.rt(180)
    common.DrawHDC(pen, stickLength, crossLength)

def DC(pen, wd, reps, layer):
    stickLength = common.CalcStickLength(wd)
    crossLength = common.CalcCrossLength(2 * math.pi * (0.2 * wd + layer * wd)/reps, 1, 0.8) # Ensure sum of cross length is smaller than layer circumference
    pen.fd(stickLength)
    pen.rt(180)
    common.DrawDC(pen, stickLength, crossLength)

def TR(pen, wd, reps, layer):
    stickLength = common.CalcStickLength(wd)
    crossLength = common.CalcCrossLength(2 * math.pi * (0.2 * wd + layer * wd)/reps, 1, 0.8) # Ensure sum of cross length is smaller than layer circumference
    pen.fd(stickLength)
    pen.rt(180)
    common.DrawTR(pen, stickLength, crossLength)

def V(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    angle = math.degrees(angle)
    pen.fd(stickLength)
    pen.rt(180 - angle/2)
    # left stick
    pen.down()
    pen.fd(stickLength)
    pen.up()
    pen.rt(180)
    pen.fd(stickLength)
    pen.lt(180 - angle)
    # right stick
    pen.down()
    pen.fd(stickLength)

def A(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    angle = math.degrees(angle)
    pen.lt(angle/2)
    # left stick
    pen.down()
    pen.fd(stickLength)
    pen.up()
    pen.rt(180)
    pen.fd(stickLength)
    pen.lt(180 - angle)
    # right stick
    pen.down()
    pen.fd(stickLength)

def TA(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 2, 0.8) # Length of cross
    angle = math.degrees(angle)
    # left stick
    pen.lt(angle/2) 
    common.DrawNoCap(pen, stickLength, crossLength)
    # right stick
    pen.rt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)

def HDC3TOG(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 3, 0.7) # Length of cross
    angle = math.degrees(angle)
    # left stick
    pen.lt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)
    # middle stick
    common.DrawNoCap(pen, stickLength, crossLength)   
    # right stick
    pen.rt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)

def FA(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 2, 0.8) # Length of cross
    angle = math.degrees(angle)
    # cap
    pen.lt(90)
    pen.fd(min(20, baseLength)/2)
    pen.rt(180)
    pen.down()
    pen.fd(min(20, baseLength))
    pen.up()
    # left stick
    pen.rt(180)
    pen.fd(min(20, baseLength)/2)
    pen.rt(90)
    pen.lt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)
    # right stick
    pen.rt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)

def DC3TOG(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 3, 0.8) # Length of cross
    angle = math.degrees(angle)
    # cap
    pen.lt(90)
    pen.fd(min(20, baseLength)/2)
    pen.rt(180)
    pen.down()
    pen.fd(min(20, baseLength))
    pen.up()
    # left stick
    pen.rt(180)
    pen.fd(min(20, baseLength)/2)
    pen.rt(90)
    pen.lt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)
    # middle stick
    common.DrawNoCap(pen, stickLength, crossLength)
    # right stick
    pen.rt(angle/2)
    common.DrawNoCap(pen, stickLength, crossLength)

def FP(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    pen.rt(90)
    pen.circle(baseLength/2, -90)
    pen.down()
    pen.circle(baseLength/2, 180) # Draw half circle

def BP(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    pen.lt(90)
    pen.fd(baseLength/2)
    pen.lt(90)
    pen.down()
    pen.circle(baseLength/2, -180) # Draw other half circle    

def FV(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 2, 0.8) # Length of cross
    angle = math.degrees(angle)
    # left stick
    pen.fd(stickLength)
    pen.rt(180 - angle/2)
    common.DrawDC(pen, stickLength, crossLength)
    # right stick
    pen.lt(180 - angle/2)
    common.DrawDC(pen, stickLength, crossLength)

def TW(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 3) # Length of cross
    angle = math.degrees(angle)
    # left stick
    pen.fd(stickLength)
    pen.rt(180 - angle/2)
    common.DrawHDC(pen, stickLength, crossLength)
    # middle stick
    pen.rt(180)
    common.DrawHDC(pen, stickLength, crossLength)
    # right stick
    pen.lt(180 - angle/2)
    common.DrawHDC(pen, stickLength, crossLength)

def TV(pen, wd, reps, layer):
    baseLength = common.CalcBaseLength(wd, reps, layer) # Shared base length
    angle = common.CalcAngle(wd, baseLength) # Angle between sticks
    stickLength = common.CalcStickLength(wd, angle) # Length of stick
    crossLength = common.CalcCrossLength(baseLength, 2, 0.8) # Length of cross
    angle = math.degrees(angle)
    pen.fd(stickLength)
    pen.rt(180 - angle/2)
    common.DrawHDC(pen, stickLength, crossLength)
    pen.lt(180 - angle/2)
    common.DrawHDC(pen, stickLength, crossLength)

pattern = {'MT':MT, 'SLST':SLST, 'CH':CH, 'SC':SC, 'HDC':HDC, 'DC':DC, 'TR':TR, 'V':V, 'A':A, 'TA':TA, 'HDC3TOG':HDC3TOG, 'FA':FA, 'DC3TOG':DC3TOG, 'FP':FP, 'BP':BP, 'FV':FV, 'TW':TW, 'TV':TV}