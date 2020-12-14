import Globals as g
        
def CheckOnOff():
    return g.onoff
        
def TurnOnOff():
    g.onoff = not g.onoff

def TempUp():
    if CheckOnOff():
        if g.temp < 28 and g.temp > 18:
            g.temp += 1

def TempDown():
    if CheckOnOff():
        if g.temp < 28 and g.temp > 18:
            g.temp -= 1

def FanSpeed():
    if CheckOnOff():
        g.fanlevel += 1
        
        if g.fanlevel > 4:
            g.fanlevel = 1

def PowerChill():
    if CheckOnOff():
        g.temp = 18
        g.fanlevel = 4

def Display():
    if CheckOnOff():
        print('Temperatur suhu:', g.temp)
        print('Level kipas:', g.fanlevel)