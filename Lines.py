
import matplotlib.pyplot as plt
import math as m

class line(object):
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.line=[p1,p2]
        self.A = (p1[1] - p2[1])
        self.B = (p2[0] - p1[0])
        self.C = (p1[0]*p2[1] - p2[0]*p1[1])

    def plot_line(self,lineC='r'):
        plt.plot([self.p1[0],self.p2[0]],[self.p1[1],self.p2[1]], lineC)  #


    def plot_lineC(self, col=[1,0,1],ls='-'):
        plt.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]],'-,',color=col,ls=ls)  #

def intersectionobj(L1, L2):  # intersection (x,y) of two lines
    # type: (object, object) -> object
    D  = L1.A * L2.B - L1.B * L2.A
    Dx = L1.C * L2.B - L1.B * L2.C
    Dy = L1.A * L2.C - L1.C * L2.A
    if D != 0:
        x = -Dx / D
        y = -Dy / D
        return x,y
    else:
        return False

def makeline(p1,p2y,t_h):
    p1=p1
    p2x=p1[0]+m.tan(t_h-m.pi/2)*(p1[1]-p2y)
    return ([p2x,p2y])


def angles(L1, L2):  # angle between two lines
        AxL1 = L1[0][0] - L1[1][0]  # x component line1
        AxL2 = L2[0][0] - L2[1][0]  # x component line2
        AyL1 = L1[0][1] - L1[1][1]  # y component line1
        AyL2 = L2[0][1] - L2[1][1]  # y component line2
        dotP = AxL1 * AxL2 + AyL1 * AyL2
        return float(m.acos(dotP / (m.hypot(AxL1, AyL1) * m.hypot(AxL2, AyL2))))




def snell(n1=1, n2=1.5, angle_in=0):  # return the angele between the line and the surface normal
    angle_out=m.asin(n1/n2*m.sin(angle_in))
    return float(angle_out)


























def intersection(L1, L2):
    # type: (object, object) -> object
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
