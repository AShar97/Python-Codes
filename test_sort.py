from time import time
from random import randint
import matplotlib.pyplot as plt

def insertsort(a):
	for j in range(1, len(a)):
		key = a[j]
		i = j - 1
		while i >= 0 and a[i] > key:
			a[i+1] = a[i]
			i = i - 1
		a[i+1] = key
def mergesort(a,p,q):
	if p < q:
		r = (p+q)//2
		mergesort(a, p, r)
		mergesort(a, r+1, q)
		merge(a, p, r, q)
def merge(a,p,r,q):
	f = a[p:r+1]
	s = a[r+1:q+1]
	f.append(float("inf"))
	s.append(float("inf"))
	i,j = 0,0
	for k in range(p,q+1):
		if f[i] <= s[j]:
			a[k] = f[i]
			i = i+1
		else:
			a[k] = s[j]
			j = j+1

# size = int(input('Size difference? '))
case = int(input('#Cases? '))
trial = int(input('#Trials? '))

time_i = []
time_m = []

for n in range(case+1):
#	timei, timem = 0, 0
	time_i.append(0)
	time_m.append(0)

	for m in range(trial):
		a = []
		b = []
		c = []
		d = []
		for i in range(n):
			key = randint(0,1000)
			a.append(key)
			b.append(key)
			c.append(key)
			d.append(key)
			del(key)

		timei1 = time()
		insertsort(a)
		timei1 = (time() - timei1)

		timem1 = time()
		mergesort(b, 0, n-1)
		timem1 = (time() - timem1)

		timem2 = time()
		mergesort(c, 0, n-1)
		timem2 = (time() - timem2)

		timei2 = time()
		insertsort(d)
		timei2 = (time() - timei2)

		time_i[n] += ((timei1+timei2)/(2*trial))
		time_m[n] += ((timem1+timem2)/(2*trial))

		del(timei1,timei2,timem1,timem2)

#	time_i.append((timei1+timei2)/(2*trial))
#	time_m.append((timem1+timem2)/(2*trial))
#	print('Length= ',n,' : Time(insert)= ',time_i[n],' ; Time (merge)= ',time_m[n])
plt.plot(time_i, 'r-')
plt.plot(time_m, 'b-')
plt.title('Time of Sorting\tR:Insert\tB:Merge')
plt.xlabel('Size')
plt.ylabel('Time')
plt.grid(True)
plt.show()
