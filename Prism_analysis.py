import os.path

from Lines import line, intersectionobj, angles, snell, makeline
from Prism_Draw import *


def analyse_prism(n=1.55, t1=m.radians(50), t2=m.radians(50), height=120, base=250, sub_h = 340,
                  l_0_t = m.pi / 2 + m.radians(30),start_l = 0,col=[0,0,0],ls='-'):
    ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'
    name_of_file = 'prismAnalysisdata_' + str(0) + '_.txt'
    completeName = os.path.join(ns_path, name_of_file)
    f = file(completeName, "a")
    # f.write("(l_0_t), (prismB.t1),(prismB.t2),(l_3_t),p_d[0],l_1p2,l_3p2\n")

    # define prisms parameters:
    prismA = Prism(n=n, t1=t1, t2=t2, height=height, base=base)
    side_ab = line(prismA.p_a, prismA.p_b)  # side a of the prism
    side_ad = line(prismA.p_a, prismA.p_d)  # side d of the prism

    plot_substrate(h=sub_h)
    # define and plot laser line in air:
    laser_w = 10  # laser width
    # l_0_t = m.pi / 2 + m.radians(30)  # laser angle relative to the x axis
    # print "laser angel:", m.degrees(l_0_t)
    l_0p1 = [start_l, start_l]
    l_0p2 = makeline(l_0p1, 200, l_0_t)
    l_0 = line(l_0p2, l_0p1)  # laser line in air
    # l_0.plot_line(lineC='-r')  # full line
    inter_l_0_prism = (intersectionobj(l_0, side_ab))  # find intersection of laser and side a
    l_0 = line(l_0p2, [inter_l_0_prism[0], inter_l_0_prism[1]])  # redefine the laser line
    # l_0.plot_line(lineC='k')  # plot line until intersection
    l_0.plot_lineC(col=col,ls=ls)  # plot line until intersection

    # laser line in prism:
    l_0_prism_t = angles(l_0.line, side_ab.line) - m.pi / 2  # find angle between normal to side a and laser
    # print "l_0_prism_t:", m.degrees(l_0_prism_t)
    l_1_prism_t = snell(n1=1, n2=prismA.n, angle_in=l_0_prism_t)
    l_1_t = l_0_t + l_0_prism_t - l_1_prism_t
    # print "l_1_prism_t:", m.degrees(l_1_prism_t)
    # print "l_1_t:", m.degrees(l_1_t)
    l_1p1 = l_0.p2
    l_1p2 = makeline(l_1p1, 0, l_1_t)
    l_1 = line(l_1p1, l_1p2)  # laser line object in prism
    # l_1.plot_line(lineC='-k')  # full line
    l_1.plot_lineC(col=col,ls=ls)  # full line


    # laser line in glass:
    l_1_prism_t = angles(l_1.line, side_ad.line) - m.pi / 2  # find angle between normal to side a and laser
    # print "l_1_prism_t:", m.degrees(l_1_prism_t)
    l_2_glass_t = snell(n2=1.5, n1=prismA.n, angle_in=l_1_prism_t)
    l_2_t = l_1_t + l_1_prism_t - l_2_glass_t
    # print "l_2_glass_t:", m.degrees(l_2_glass_t)
    # print "l_2_t:", m.degrees(l_2_t)
    l_2p1 = l_1.p2
    l_2p2 = makeline(l_2p1, -sub_h, l_2_t)
    l_2 = line(l_2p1, l_2p2)  # laser line object in prism
    # l_2.plot_line(lineC='-k')  # full line
    l_2.plot_lineC(col=col,ls=ls)  # full line


    # laser line in glass2:
    l_3_t = m.pi-l_2_t
    # print "l_2_glass_t:", m.degrees(l_2_glass_t)
    # print "l_3_t:", m.degrees(l_3_t)
    l_3p1 = l_2.p2
    l_3p2 = makeline(l_3p1, 0, l_3_t)
    l_3 = line(l_3p1, l_3p2)  # laser line object in prism
    # l_3.plot_line(lineC='-k')  # full line
    l_3.plot_lineC(col=col,ls=ls)  # full line
    # print "l_3p2", (l_3p2)

    # laser line in prism2:
    l_3_glass_t = angles(l_3.line, side_ad.line) - m.pi / 2  # find angle between normal to side a and laser
    # print "l_3_glass_t:", m.degrees(l_3_glass_t)
    l_4_prism_t = snell(n1=1.5, n2=prismA.n, angle_in=l_3_glass_t)
    l_4_t = l_3_t - l_3_glass_t + l_4_prism_t
    # print "l_4_prism_t:", m.degrees(l_4_prism_t)
    # print "l_4_t:", m.degrees(l_4_t)
    l_4p1 = l_3.p2
    l_4p2 = makeline(l_4p1, 200, l_4_t)
    l_4 = line(l_4p1, l_4p2)  # laser line object in prism
    # l_4.plot_line(lineC='-k')  # full line
    l_4.plot_lineC(col=col,ls=ls)  # full line

    prismB = Prism(n=n, t1=t1, t2=m.pi/2-l_4_t, height=height, base=l_3p2[0]-side_ab.p2[0]+20,col=col)
    if ls=='-':
        prismB.plot_prism(col=col)
    side_ab = line(prismB.p_a, prismB.p_b)  # side a of the prism
    side_ad = line(prismB.p_a, prismB.p_d)  # side d of the prism

    plt.axis((-100, side_ad.p2[0]+50, -200, 250))
    plt.title("laser angle=%.1f; prism Height=%.1f"  %( m.degrees(l_0_t), prismB.h))
    plt.grid

    # print m.degrees(l_0_t),m.degrees(l_3_t),m.degrees(prismB.t1),m.degrees(prismB.t2),l_1p2[0],l_3p2[0],prismB.p_d[0]
    if ls!='t-':
         np.savetxt(f, [[m.degrees(l_0_t),m.degrees(l_3_t),m.degrees(prismB.t1),m.degrees(prismB.t2),l_1p2[0],l_3p2[0],prismB.p_d[0]]], fmt='%.3f',delimiter=',')

    return(l_0_t,prismB, l_3_t)

