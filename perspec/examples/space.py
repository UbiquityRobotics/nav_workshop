from numpy import matrix

id = matrix([[1,0],[0,1]])
sx = matrix([[0,1],[1,0]])
sy = matrix([[0,-1j],[1j,0]])
sz = matrix([[1,0],[0,-1]])

def cross(a,b):
    return a.real*b.imag - a.imag*b.real

def inside(k,a,b,c):
    m = (a+b)/2
    beta = cross(k-a,k-m) / cross(c-a,k-m)
    gamma = cross(k-a,c-a) / cross(c-a,k-m)
    return gamma > 0 and beta > 0 and beta < 1

class Tetrahedron:
    node = [1j*(sx+sy+sz),1j*(-sx-sy+sz),1j*(-sx+sy-sz),1j*(sx-sy-sz)]
    line = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]

class Cube:
    node = [1j*(sx+sy+sz),1j*(sx-sy+sz),1j*(-sx-sy+sz),1j*(-sx+sy+sz),
            1j*(sx+sy-sz),1j*(sx-sy-sz),1j*(-sx-sy-sz),1j*(-sx+sy-sz)]
    line = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],
            [0,4],[1,5],[2,6],[3,7]]


