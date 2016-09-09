import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path
from Prism_Draw_fun import draw_prism

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

t1_angles=[]
t_glassV=[]
n_prism=1.55
t1 = m.radians(50)  # base angle
t_l=m.pi/2+t1-m.radians(-20)
for i in frange(30,51,0.5):
    t1 =m.radians(i)  # base angle
    t1_angles.append(t1)
    t_lp = m.pi / 2 + t1 - t_l  # laser angle relative to norm to prism
    t_lp_in=m.asin(m.sin(t_lp)/n_prism)
    t_glass=t1-t_lp_in
    t_glassV.append(t_glass)
    print m.degrees(t1),m.degrees(t_lp), m.degrees(t_lp_in), m.degrees(t_glass)

print [x * 180/m.pi for x in t1_angles]
print [x * 180/m.pi for x in t_glassV]

plt.plot([x * 180/m.pi for x in t1_angles],[x * 180/m.pi for x in t_glassV],'-o')
plt.xlabel("prism base angle")
plt.ylabel("incident angle on gold substrate")
plt.text(30,42,"laser angle is 30")
plt.show()
