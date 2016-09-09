import math as m, math
import numpy as np
import matplotlib.pyplot as plt
import os.path

def draw_prism(prism_t_b1=30*m.pi/180, prism_t_b2=50*m.pi/180, prism_l_b1=400, prism_h=100):
# this function accept 4 parameters and plot the prisms accordingly
# 1. base angle t_b1; 2. base angle t_b2; 3. prism short base; 4. and prism height

# ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\8 Kings\Bridges'
# prism_t_b1=40*m.pi/180
# prism_t_b2=50*m.pi/180
# prism_l_b1=200
# prism_h=200

    prism_l_s1 = prism_h / m.sin(prism_t_b1)
    prism_l_s2 = prism_h / m.sin(prism_t_b2)
    prism_side_a = ([0,prism_h/m.tan(prism_t_b1)],[0,prism_h])
    prism_side_b = ([prism_side_a[0][1],prism_side_a[0][1]+prism_l_b1],[prism_h,prism_h])
    prism_side_c = ([prism_side_b[0][1], prism_side_b[0][1] +prism_h/m.tan(prism_t_b2)], [prism_h, 0])
    prism_side_d = ([prism_side_c[0][1], prism_side_a[0][0]], [0, 0])

    plt.plot()
    # print prism_side_d
    # print prism_side_c[0][1]

    prism_vortex_x=[prism_side_a[0][0],prism_side_b[0][0],prism_side_c[0][0],prism_side_d[0][0],prism_side_a[0][0]]
    prism_vortex_y=[prism_side_a[1][0],prism_side_b[1][0],prism_side_c[1][0],prism_side_d[1][0],prism_side_a[1][0]]

    h_subs=170
    subs_vortex_x=[-500,max(prism_vortex_x)+500, max(prism_vortex_x)+500, -500, -500]
    subs_vortex_y=[0,0, -h_subs, -h_subs, 0]

    plt.plot(prism_vortex_x,prism_vortex_y,'b') # substrate
    plt.plot(subs_vortex_x,subs_vortex_y,'b') # substrate
    plt.axes().set_aspect('equal', 'datalim')
    plt.grid()
    # plt.show()

    return prism_side_a, prism_side_b, prism_side_c, prism_side_d

# draw_prism(30*m.pi/180)