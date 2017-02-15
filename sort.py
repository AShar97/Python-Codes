#! /usr/bin/python3
import time
import random
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

size = int(input('Size? '))
a = []
b = []
for i in range(size):
	a.append(random.randint(0,1000))
	b.append(a[i])
timei = time.time()
insertsort(a)
timei = time.time() - timei

timem = time.time()
mergesort(b, 0, size-1)
timem = time.time() - timem
print('Time for insert sort = ', timei)
print(a)
print('Time for merge sort = ', timem)
print(b)
