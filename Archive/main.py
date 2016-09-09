import math as m
import numpy as np
import matplotlib.pyplot as plt
import os.path

from utility_func import frange,frangeV
from Prism_Draw import *
from Lines import line, intersectionobj, angles, snell, makeline
from Prism_analysis import analyse_prism
from utility_func import get_cmap


t1V=[]
t2V=[]
t_glassV=[]
l_0_tV=[]
end_baseV=[]
print "(l_0_t), (prismB.t1),(prismB.t2),(l_3_t),p_d[0],l_1p2,l_3p2"
iV=frangeV(30,50.5,10)

# cmap = get_cmap(len(iV))

count=0
height=60
sub_h=300
start_l = height / 3
for i in iV:
    if i==30:
        col=[1,0,0]
    elif i==50:
        col = [0, 0, 1]
    else:
        col=[0,1,0]
    # col = [1, 0, 0]
    t1 =m.radians(i)  # base angle
    [l_0_t,prism,gold_angle]= analyse_prism(n=1.55, t1=t1, t2=m.radians(50), height=height, base=250, sub_h=sub_h,
                                            l_0_t = m.pi / 2 + m.radians(40),start_l=start_l,col=col)
    l_0_tV.append(l_0_t)
    t1V.append(t1)
    t2V.append(prism.t2)
    end_baseV.append(prism.p_d[0])
    t_glassV.append(gold_angle)

start_l = 100+height/2+100  # position of laser end point (x=y)

# iV=frange(30,50.5,0.5)
# cmap = get_cmap(len(iV))

count=1
start_l = height / 2+15
for i in iV:
    if i==30:
        col=[1,0,0]
    elif i==50:
        col = [0, 0, 1]
    else:
        col=[0,1,0]
    # col = [1, 0, 0]
    t1 =m.radians(i)  # base angle
    [l_0_t,prism,gold_angle]= analyse_prism(n=1.55, t1=t1, t2=m.radians(50), height=height, base=250, sub_h=sub_h,
                                            l_0_t = m.pi / 2 + m.radians(40),start_l=start_l,col=col,ls='--')
    # l_0_tV.append(l_0_t)
    # t1V.append(t1)
    # t2V.append(prism.t2)
    # # end_baseV.append(prism.p_d[0])
    # t_glassV.append(gold_angle)



# [laser_In_t,prism_t1,prism_t2,prism_base_end, gold_angle]= analyse_prism(n=1.55, t1=t1, t2=m.radians(50), height=120, base=250, sub_h=170,l_0_t = m.pi / 2 + m.radians(40))
# print laser_In_t,prism_t1,prism_t2,prism_base_end, gold_angle

# return (l_0_t, prismB.t1, prismB.t2, prismB.p_d[0], l_3_t)
plt.grid()
plt.show()

plt.subplot(3, 1, 1)
plt.grid()

plt.plot([x * 180/m.pi for x in t1V],[x * 180/m.pi for x in t_glassV],'-o')
plt.xlabel("prism base angle")
plt.ylabel("angle on gold ")
# plt.text(30,42,"laser angle is 30")
plt.subplot(3, 1, 2)
plt.plot([x * 180/m.pi for x in t1V],[x * 180/m.pi for x in t2V],'-o')
plt.xlabel("prism base angle")
plt.ylabel("base angle 2")
plt.grid()

plt.subplot(3, 1, 3)

plt.plot([x * 180/m.pi for x in t1V],end_baseV,'-o')
plt.xlabel("prism base angle")
plt.ylabel(" base length  [um]")
plt.grid()

plt.show()