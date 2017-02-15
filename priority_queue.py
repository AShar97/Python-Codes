from heap_2 import *
#import heap_2

class prq():
	def __init__(self, a):
		self.heap = a
		self.n = len(a)
		build_max_heap(self.heap, self.n)

	def maximum(self):
		return self.heap[0]

	def remove_maximum(self): #may include list.pop()
		if len(self.heap) < 1:
			raise Exception ("Heap underflow")
		else:
			self.heap[0], self.heap[self.n - 1] = self.heap[self.n - 1], self.heap[0]
			self.n -= 1
			max_heapify(self.heap, 0, self.n)
		return self.heap[self.n]

	def increase_key(self, i):
		while (i > 0 and self.heap[i] > self.heap[parent(i)]):
			#if (self.heap[i] > self.heap[parent(i)]):
			self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
			i = parent(i)

	def insert(self, x):
		if (self.n < len(self.heap)):
			self.heap[self.n] = x
		elif(self.n == len(self.heap)):
			self.heap.append(x)
		self.n += 1
		self.increase_key(self.n - 1)

	def print_heap(self):
		print(self.heap[:self.n])
'''
a = prq([1,2,3,4,5,6,7,8,9])

a.insert(0)
a.print_heap()

print(a.maximum())

a.insert(11)
a.print_heap()

build_max_heap(a.heap, a.n)
a.print_heap()

print(a.maximum())
a.remove_maximum()

a.print_heap()