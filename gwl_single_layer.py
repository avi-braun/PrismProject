import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path

#  this file generate single layer of the prism
r=1


ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'
name_of_file='pos_'+str(r)+'_.gwl'
completeName = os.path.join(ns_path,name_of_file)
f = file(completeName, "w")
f.close

base_lx=2.4
base_ly=20
x_start=0
x_end=x_start+base_lx
y_start=0
y_end=y_start+base_ly

cont_h=0.1
cont_n=3

fill_h=0.3
fill_n=int((base_lx-(cont_n-1)*cont_h*2)/fill_h)

# contours:
for i in range (0,cont_n):
    xpos = []
    ypos = []
    zpos = []
    xypos = []
    x1=x_start+i*cont_h
    x2=x_end-i*cont_h
    y1=y_start+i*cont_h
    y2=y_end-i*cont_h

    xpos.extend((x1,x1,x2,x2,x1))
    ypos.extend((y1,y2,y2,y1,y1))
    zpos.extend((0,0,0,0,0))
    xypos = np.array([xpos, ypos, zpos]).transpose()
    f=open(completeName, "a")
    np.savetxt(f, xypos, fmt='%.3f')
    f.write('write\n')
f.close()

Lx_temp=x2-x1

x_center = x1 + (x2 - x1) / 2
if fill_n % 2:  # ofd number of lines
    x1 = x_center - fill_h * (fill_n / 2+1)
    print 'odd'
if not(fill_n % 2):  # even number of lines
        x1 = x_center - fill_h * (fill_n / 2 + 0.5)
        print 'even'
for i in range (0,int(fill_n)):
    x1=x1+fill_h
    xy=np.array([[x1, y1, 0], [x1, y2, 0]])
    f = open(completeName, "a")
    np.savetxt(f, xy, fmt='%.3f')
    f.write('write\n')
f.close()
