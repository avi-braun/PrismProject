import math as m, math
import numpy as np
# import matplotlib.pyplot as plt
import os.path
import time

t1d=50
ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'

name_of_file='pos_'+str(t1d)+'_.gwl'
completeName = os.path.join(ns_path,name_of_file)
f = file(completeName, "w")
f.close

t1=m.radians(t1d)
t2=m.radians(43)
h=6

slice=0.1
slice_n=h/slice
cont_h=0.1
cont_n=3
fill_h=0.4

base_lx=506
base_ly=50
x_start=0
x_end=x_start+base_lx
y_start=0
y_end=y_start+base_ly
dx_start=slice/m.tan(t1)
dx_end=slice/m.tan(t2)
print "x_end", x_end
print "x_start", x_start
f = open(completeName, "a")

tic = time.clock()
for i in range(0,int(slice_n)):
    for i in range(0, cont_n):
        xpos = []
        ypos = []
        zpos = []
        xypos = []
        x1 = x_start + i * cont_h
        x2 = x_end - i * cont_h
        y1 = y_start + i * cont_h
        y2 = y_end - i * cont_h

        xpos.extend((x1, x1, x2, x2, x1))
        ypos.extend((y1, y2, y2, y1, y1))
        zpos.extend((0, 0, 0, 0, 0))
        xypos = np.array([xpos, ypos, zpos]).transpose()

        np.savetxt(f, xypos, fmt='%.3f')
        f.write('write\n')
    # f.close()

    Lx_temp = x2 - x1
    x_center = x1 + (x2 - x1) / 2
    fill_n = int((base_lx - (cont_n - 1) * cont_h * 2) / fill_h)
    if fill_n % 2:  # ofd number of lines
        x1 = x_center - fill_h * (fill_n / 2 + 1)
    if not (fill_n % 2):  # even number of lines
        x1 = x_center - fill_h * (fill_n / 2 + 0.5)
    for i in range(0, int(fill_n)):
        x1 = x1 + fill_h
        xy = np.array([[x1, y1, 0], [x1, y2, 0]])
        # f = open(completeName, "a")
        np.savetxt(f, xy, fmt='%.3f')
        f.write('write\n')
    # f.close()
    # f.write('%d')% int(slice_n)
    f.write('AddZOffset ' +str(slice)[:4]+'\n')
    x_start+=dx_start
    x_end-=dx_end
    base_lx=x_end-x_start

    # print base_lx
    # print fill_n

f.close()
toc = time.clock()

print ('process time was: '+str(toc-tic)[:5]+' sec')
