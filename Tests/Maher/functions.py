import sys
import time

#from pythymiodw import ThymioReal

def forwardWithSpeed(distance, speed):
    v = speed * 0.0003
    speedc = speed * 1.07
    t = distance / (v * 100)
    m.wheels(speed, speedc)
    time.sleep(t)
    m.wheels(0, 0)

def forward(distance):
    t = distance / 3
    m.wheels(100, 107)
    time.sleep(t)
    m.wheels(0, 0)

m = ThymioReal()
m.quit()
