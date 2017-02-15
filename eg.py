def left(i):
	return (2*i+1)
def right(i):
	return (2*i+2)

def max_heapify(a,i):
	l=left(i)
	r=right(i)
	largest=i
	if l<len(a) and a[i]<a[l]:
		largest=l

	if r<len(a) and a[largest]<a[r]:
		largest=r

	if(largest!=i):
		a[i],a[largest]=a[largest],a[i]
		max_heapify(a,largest)

def build_max_heap(a):
	for i in range((len(a)//2)-1,-1,-1):
		max_heapify(a,i)

def heap_sort(a):
	build_max_heap(a)
	for i in range(len(a)-1):
		a[0],a[len(a)-1-i]=a[len(a)-1-i],a[0]
		b=list()
		b=a[0:len(a)-1-i]
		
		max_heapify(b,0)
		a[0:len(a)-1-i]=b

	return a

a = [1,3,5,2,7,4,0]
r = heap_sort(a)
print(r)