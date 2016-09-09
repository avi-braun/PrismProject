import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path
import time
from gwl_prism_function_longlines import create_prism_gwl
from io import StringIO

import main_geometry

ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'
name_of_file = 'prismAnalysisdata_' + str(0) + '_.txt'
completeName = os.path.join(ns_path, name_of_file)

main_geometry

datanp=np.loadtxt(completeName,skiprows=1,delimiter=',')
print datanp

Ly=10
for i in range(0,len(datanp)/2,1):

    prism1_x2=datanp[len(datanp)/2+i][4]+70
    t1=m.radians(datanp[i][2])
# t2=m.radians(np.max(datanp[:,2]))
    t2=m.radians(datanp[i][3])
    create_prism_gwl(x1=0, x2=prism1_x2, y1=i*Ly, y2=(i+1)*Ly, h=55, t1=t1, t2=m.pi/2*0.8, fill_h=0.3, cont_n=3, slice=0.1, cont_h=0.1, fileN='in_'+str(i), fileP='')
    prism2_x1=datanp[i][5]-50
    prism2_x2=datanp[i][6]
    create_prism_gwl(x1=prism2_x1, x2=prism2_x2, y1=i*Ly, y2=(i+1)*Ly, h=60, t1=m.pi/2-t2, t2=t2, fill_h=0.3, cont_n=3, slice=0.1, cont_h=0.1, fileN='out_'+str(i), fileP='')


tic = time.clock()
toc = time.clock()
print "process time was:", str(toc-tic),"sec"

