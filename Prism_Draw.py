import math as m
import numpy as np
import matplotlib.pyplot as plt
import os.path

class Prism(object):
    def __init__(self, n=1.5, base=400, height=100, t1=m.radians(30), t2=m.radians(30),col=[0,0,0]):
        self.n = n
        self.base1 = base
        self.h = height
        self.t1=t1
        self.t2=t2
        self.p_a = [0, 0]
        self.p_b = [self.p_a[0] + self.h/ m.tan(self.t1), self.h]
        self.p_c = [self.p_b[0] + self.base1, self.p_b[1]]
        self.p_d = [self.p_c[0] + self.h / m.tan(self.t2), self.p_a[1]]

    def plot_prism(self,col=[0,0,0]):
        xV=[self.p_a[0],self.p_b[0],self.p_c[0],self.p_d[0],self.p_a[0]]
        yV = [self.p_a[1], self.p_b[1], self.p_c[1], self.p_d[1], self.p_a[1]]

        plt.plot(xV,yV,'-',color=col)
        plt.axes().set_aspect('equal', 'datalim')
        plt.grid()

def plot_substrate(h=170):
    p_a=[-100,-h]
    p_b=[-100,0]
    p_c=[1000,0]
    p_d=(1000,-h)
    xV = [p_a[0], p_b[0], p_c[0], p_d[0], p_a[0]]
    yV = [p_a[1], p_b[1], p_c[1], p_d[1], p_a[1]]
    plt.plot(xV, yV, 'k')

