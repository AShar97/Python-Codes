from time import time
from random import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
import math

def vmult(a,b):
	c = []
	for i in range(len(a)):
		c.append(a[i]*b[i])
	return c

def omult(a,b):
	c = [0] * ((len(a)-1)+(len(b)-1)+1)
	for i in range(len(a)):
		for j in range(len(b)):
			c[i+j] = c[i+j] + (a[i]*b[j])
	return c

def fft(a,w):
	if (len(a) == 1):
		return a
	s = fft(a[::2],(w*w))
	s1 = fft(a[1::2],(w*w))
	r = [0] * (len(a))
	for j in range(int(len(a)/2)):
		r[j] = s[j] + ((w**j)*s1[j])
		r[j+int(len(a)/2)] = s[j] - ((w**j)*s1[j])
	return r

def fftmult(a,b):
    size = (len(a)-1)+(len(b)-1)+1
    i = 2**(math.ceil(math.log2(max(len(a),len(b)))) + 1)
    a.extend([0] * (i - len(a)))
    b.extend([0] * (i - len(b)))

    w = cmath.exp((2 * cmath.pi * 1j) / i)

    c = fft(vmult(fft(a, w),fft(b, w)), 1/w)[:size]
    c = [x/i for x in c]
    return c

l = int(input('Max-degree : ')) + 1

t_o = [x[:] for x in [[0] * l] * l]
t_fft = [x[:] for x in [[0] * l] * l]
for i in range(1,l):
    for j in range(1,l):
        a = []
        b = []
        for m in range(i):
            a.append(random())
        for n in range(j):
            b.append(random())

        #Ordinary multiplication of polynomial
        t_o[i][j] = time()
        c_o = omult(a,b)
        t_o[i][j] = time() - t_o[i][j]

        #FFT multiplication of polynomial
        t_fft[i][j] = time()
        c_fft = fftmult(a,b)
        t_fft[i][j] = time() - t_fft[i][j]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [x[:] for x in [[0] * l] * l]
Y = [x[:] for x in [[0] * l] * l]
for i in range(l):
    for j in range(l):
        X[i][j] = i
        Y[i][j] = j

Z = t_o
Axes3D.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
Z = t_ttf
Axes3D.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
plt.title('Time of Multiplying')
plt.tight_layout()
plt.show()
'''
#X, Y, Z = axes3d.get_test_data(0.05)
print(X)
print(Y)
#print(Z)
'''
print(t_o)
print('\n\n\n\n\n\n')
print(t_fft)
