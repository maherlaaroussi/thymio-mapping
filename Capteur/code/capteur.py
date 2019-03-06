#1erTerminal: sudo asebamedulla "ser:name=Thymio-II"
#2eme terminal: sudo python3 <programme>.py 

import sys
from pythymiodw import *
import time

r=ThymioReal()
"""
r.wheels(200,200)
time.sleep(3)
r.wheels(0,0)
"""
compter = 10
d=compter
m1=0
m2=0
m3=0
m4=0
m5=0
while(compter != 0):
    m1=m1+r.prox_horizontal[0]
    m2=m2+r.prox_horizontal[1]
    m3=m3+r.prox_horizontal[2]
    m4=m4+r.prox_horizontal[3]
    m5=m5+r.prox_horizontal[4]
    print(m1,m2,m3,m4,m5)
    time.sleep(0.5)
    compter = compter -1

print(m1/(d-1),m2/(d-1),m3/(d-1),m4/(d-1),m5/(d-1))

r.quit()
