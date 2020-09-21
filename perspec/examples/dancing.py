from numpy import trace, sqrt, sin, cos
from tkinter import Tk, Canvas, ALL
from numpy.random import random

from space import *
poly = Cube()
node = poly.node
line = poly.line

dis = 8
siz = 500
dz = dis*1j*sz
node = list(map(lambda v: v + dz, node))

print(1j*sx)
print(-1j*sy)
print(1j*sz)

def plane(v):
    X = trace(sx*v/2j).real
    Y = trace(sy*v/2j).real
    Z = trace(sz*v/2j).real
    obs = 3
    x = obs*X/Z
    y = obs*Y/Z
    x = (1+x)*siz/2
    y = (1+y)*siz/2
    return x + 1j*y

def face(a,b,c):
    global colour
    p = (node[a]-node[b])*(node[a]-node[c])
    p -= id*trace(p).real/2
    p /= sqrt(-trace(p*p)/2)
    a2 = plane(node[a])
    b2 = plane(node[b])
    c2 = plane(node[c])
    s = set([a,b,c])
    for l,lyne in enumerate(line):
        e = lyne[0]
        d = lyne[1]
        if e in s and d in s:
            continue
        mp = (node[e] + node[d])/2
        lam = trace(node[a]*p)/trace(mp*p)
        if lam < 1:
            mp2 = plane(mp)
            if inside(mp2,a2,b2,c2) or inside(mp2,b2,a2,c2):
                colour[l] = "blue"

def manyfaces():
    for a in range(len(line)):
        for b in range(a):
            p = line[a]
            q = line[b]
            if p[0]==q[0]:
                face(p[0],p[1],q[1])
            elif p[0]==q[1]:
                face(p[0],p[1],q[0])
            elif p[1]==q[0]:
                face(p[1],p[0],q[1])
            elif p[1]==q[1]:
                face(p[1],p[0],q[0])

def draw():
    global node
    global colour
    global dz
    colour = len(line)*["cyan"]
    t = 0.1
    axis = (sx+sz)/sqrt(2.)
    ns = cos(t)*id + 1j*sin(t)*axis
    nsd = cos(t)*id - 1j*sin(t)*axis
    node = list(map(lambda v: ns*(v-dz)*nsd, node))
    dz += (random()-0.5)*.1j*sx + (random()-0.5)*.1j*sy + (random()-0.5)*.1j*sz
    node = list(map(lambda v: v+dz, node))
    manyfaces()
    canv.delete(ALL)
    for l in range(len(line)):
        i = line[l][0]
        f = line[l][1]
        wi = plane(node[i])
        wf = plane(node[f])
        sv = canv.create_line(wi.real,wi.imag,wf.real,wf.imag,fill=colour[l])
    canv.after(40,draw)


root = Tk()
canv = Canvas(root, width=500, height=500, background='black')
canv.pack()
draw()
root.mainloop()

