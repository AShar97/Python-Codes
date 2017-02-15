def parent(i):
	return (i - 1)//2

def left(i):
	return (2*i + 1)

def right(i):
	return (2*i + 2)

def max_heapify(a, i):
	l = left(i)
	r = right(i)
	largest = i
	if (l < len(a) and a[largest] < a[l]):
		largest = l
	if (r < len(a) and a[largest] < a[r]):
		largest = r
	if (largest != i):
		a[i],a[largest] = a[largest],a[i]
		max_heapify(a, largest)

def build_max_heap(a):
	for i in range(parent(len(a) - 1), -1, -1):
		max_heapify(a, i)

def heap_sort(a):
	build_max_heap(a)
	for i in range(len(a) - 1):
		a[0],a[len(a) - 1 - i] = a[len(a) - 1 - i],a[0]
#		{decrease size} len(a)--
	#	max_heapify(a[:(len(a) - 1 - i)],0)
		a_ = a[:(len(a) - 1 - i)]		
		max_heapify(a_,0)
		a[:(len(a) - 1 - i)] = a_
'''
a = [1,3,5,2,7,4,0]
heap_sort(a)
print(a)