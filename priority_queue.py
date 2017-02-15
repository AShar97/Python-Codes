from heap_2.py import *

class prq():
	def __init__(self, a):
		self.heap = a
	#	self.n = len(a) - 1
		build_max_heap(self.heap)

	def insert(self, x):
		self.heap.append(x)
		self.increase_key(self.n)
		#self.n += 1

	def maximum(self):
		return self.heap[0]

	def remove_maximum(self):
		if len(self.heap) < 1:
			raise EXCEPTION ("Heap underflow")
		else:
			self.heap[0], self.heap[self.n] = self.heap[self.n], self.heap[0]
		#	self.n -= 1
			max_heapify(self.heap, 0)

	def increase_key(self, i):
		while (i >= 0):
			if (self.heap[i] > self.heap[parent(i)]):
				self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
			i = parent(i)

	def print_heap(self):
		print(self.heap[:self.n])

a = prq([1,2,3,4,5,6,7,8,9])

a.insert(0)

print(a.maximum())

a.insert(11)

print(a.maximum())
a.remove_maximum()

a.print_heap()