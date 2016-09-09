from Prism_Draw import *
from Prism_analysis import analyse_prism
from utility_func import frangeV

ns_path = 'C:\Users\Avi Braun\Dropbox\LAB B014\NaNoscribe\Structures\Prism'
name_of_file='prismAnalysisdata_'+str(0)+'_.txt'
completeName = os.path.join(ns_path,name_of_file)
f = file(completeName, "w")
f.write('(l_0_t)\t(l_3_t)\t(t1)\t(t2)\tl_1p2\tl_3p2\tp_d[0]\n')
f.close
f = file(completeName, "a")

t1V=[]
t2V=[]
t_glassV=[]
l_0_tV=[]
end_baseV=[]
iV=frangeV(30,50.5,1)
Ly=50
# iV=[40, 50]
print('(l_0_t)\t(l_3_t)\t(t1)\t(t2)\tl_1p2\tl_3p2\tp_d[0]\n')

# cmap = get_cmap(len(iV))

count=0
height=80
start_l = height / 3
l_0_t = m.pi / 2 + m.radians(40)
for i in iV:
    if i==30:
        col=[1,0,0]
    elif i==50:
        col = [0, 0, 1]
    else:
        col=[0,1,0]
    # col = [1, 0, 0]
    t1 =m.radians(i)  # base angle
    [l_0_t,prism,gold_angle]= analyse_prism(n=1.55, t1=t1, t2=m.radians(50), height=height, base=250, sub_h=170,
                                            l_0_t = l_0_t,start_l=start_l,col=col)
    l_0_tV.append(l_0_t)
    t1V.append(t1)
    t2V.append(prism.t2)
    end_baseV.append(prism.p_d[0])
    t_glassV.append(gold_angle)

# iV=frange(30,50.5,0.5)
# cmap = get_cmap(len(iV))

count=1
start_l = height / 3+Ly*m.sin((t1))
for i in iV:
    if i==30:
        col=[1,0,0]
    elif i==50:
        col = [0, 0, 1]
    else:
        col=[0,1,0]
    # col = [1, 0, 0]
    t1 =m.radians(i)  # base angle
    [l_0_t,prism,gold_angle]= analyse_prism(n=1.55, t1=t1, t2=m.radians(50), height=height, base=250, sub_h=170,
                                            l_0_t = m.pi / 2 + m.radians(40),start_l=start_l,col=col,ls='--')

plt.grid(b=1,which='both')
plt.show()
plt.subplot(3, 1, 1)
plt.plot([x * 180/m.pi for x in t1V],[x * 180/m.pi for x in t_glassV],'-o')
plt.xlabel("prism base angle")
plt.ylabel("angle on gold ")
plt.title("laser angle=%.1f; prism Height=%.1f" % (m.degrees(l_0_t), height))
plt.grid()

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
# plt.show()

name_of_file = 'DynamicPrism_generic.gwl'
fname = os.path.join(ns_path, name_of_file)
fname_n = os.path.join(ns_path, 'DynamicPrism_RunFile.gwl')



# copy generic run file
with open(fname) as f:
    with open(fname_n, "w") as fn:
        for line in f:
            fn.write(line)
        j=0
        for i in iV:
            fn.write("include "+'30-40-1_'+'in_'+str(j)+'.gwl\n')
            fn.write('Zoffset 0\n')
            fn.write("include "+'30-40-1_'+'out_'+str(j)+'.gwl\n')
            fn.write('Zoffset 0\n')
            j+=1

# add lines for writing prisms:


