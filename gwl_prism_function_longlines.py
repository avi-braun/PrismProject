import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path
import time


def create_prism_gwl(x1=0,x2=100,y1=0,y2=10.5,h=5,t1=m.radians(40),t2=m.radians(50),fill_h=0.3,cont_n=3,slice=0.1,
                                                                             cont_h=0.1,fileN='xx',fileP=''):
    ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'
    name_of_file='30-40-1_'+fileN+'.gwl'
    completeName = os.path.join(ns_path,name_of_file)
    f = file(completeName, "w")
    f.close
    t1d = m.degrees(t1)
    t1=t1
    t2=t2
    h=h
    slice=slice
    slice_n=h/slice
    cont_h=cont_h
    cont_n=cont_n
    fill_h=fill_h
    x_start=x1
    x_end=x2
    y_start=y1
    y_end=y2
    dx_start=slice/m.tan(t1)
    dx_end=slice/m.tan(t2)
    f = open(completeName, "a")

    for i in range(0, int(slice_n)):
        create_contours(cont_n, cont_h, x_start, x_end, y_start, y_end, file_handle=f)
        y_start_f =y_start+(cont_n-1)*cont_h
        y_end_f = y_end-(cont_n-1)*cont_h
        x_start_f =x_start+(cont_n-1)*cont_h
        x_end_f = x_end-(cont_n-1)*cont_h
        fill_space(cont_n, cont_h, slice, fill_h, x_start=x_start_f, x_end=x_end_f, y_start=y_start_f, y_end=y_end_f, dx_start=dx_start,
                   dx_end=dx_end, file_handle=f)

        x_start += dx_start
        x_end -= dx_end

        f.write('AddZOffset ' + str(slice)[:4] + '\n')
    f.close()


def create_contours(cont_n,cont_h,x_start,x_end,y_start,y_end,file_handle):
    for i in range(0, cont_n):
        xpos = []
        ypos = []
        zpos = []
        x1 = x_start + i * cont_h
        x2 = x_end - i * cont_h
        y1 = y_start + i * cont_h
        y2 = y_end - i * cont_h
        xpos.extend((x1, x1, x2, x2, x1))
        ypos.extend((y1, y2, y2, y1, y1))
        zpos.extend((0, 0, 0, 0, 0))
        xypos = np.array([xpos, ypos, zpos]).transpose()
        np.savetxt(file_handle, xypos, fmt='%.3f')
        file_handle.write('write\n')

def fill_space(cont_n,cont_h,slice,fill_h,x_start,x_end,y_start,y_end,dx_start,dx_end,file_handle):
    # direction=0
    y_center = y_start + (y_end - y_start) / 2
    fill_n = int((y_end - y_start ) / fill_h)
    if fill_n % 2:  # ofd number of lines
        y1 = y_center - fill_h * (fill_n / 2 + 1)
    if not (fill_n % 2):  # even number of lines
        y1 = y_center - fill_h * (fill_n / 2 + 0.5)
    for i in range(0, int(fill_n)):
        y1 = y1 + fill_h
        # if direction:
        x_start, x_end = x_end, x_start
            # direction=0
        xy = np.array([[x_start, y1, 0], [x_end, y1, 0]])
        np.savetxt(file_handle, xy, fmt='%.3f')
        file_handle.write('write\n')


tic = time.clock()
print 'started'
create_prism_gwl(x1=0, x2=338, y1=0, y2=50, h=60, t1=m.radians(40), t2=m.radians(48), fill_h=0.3, cont_n=3, slice=0.1, cont_h=0.1, fileN='test', fileP='')
# create_prism_gwl(x1=0, x2=100, y1=0, y2=10, h=40, t1=m.radians(40), t2=m.radians(48), fill_h=0.3, cont_n=3, slice=0.1, cont_h=0.1, fileN='test_short', fileP='')
#
toc = time.clock()
print "process time was:", str(toc-tic),"sec"
