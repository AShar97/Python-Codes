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

a = eval(input('Polynomial a: '))
b = eval(input('Polynomial b: '))

#Ordinary multiplication of polynomial
c_o = omult(a,b)
print('c_o: ', c_o)

#FFT
size = (len(a)-1)+(len(b)-1)+1
'''
if (len(a) >= len(b)):
	key = len(a)
	b.extend([0] * (key-len(b)))
else:
	key = len(b)
	a.extend([0] * (key-len(a)))

i = 1
while key < i:
	i = i * 2
i = i * 2
'''
#i = 2 * key
i = 2**(math.ceil(math.log2(max(len(a), len(b)))) + 1)
print(i)

a.extend([0] * (i - len(a)))
b.extend([0] * (i - len(b)))

print(a)
print(b)

w = cmath.exp((2 * cmath.pi * 1j) / (i))
a1 = fft(a, w)
b1 = fft(b, w)

c1 = vmult(a1,b1)

#w1 = cmath.exp((-2 * cmath.pi * 1j) / (i))

c_fft = fft(c1, 1/w)[:size]
c_fft = [x/i for x in c_fft]

print('c_fft: ', c_fft)
