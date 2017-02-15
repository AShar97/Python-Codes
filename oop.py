class Matrix(object):
	#Construction
	def __init__(self, h, w):
		if (h == 1):
			self.data = [0 for x in range(w)]
		elif (w == 1):
			self.data = [0 for x in range(h)]
		else:
			self.data = [[0 for x in range(w)] for y in range(h)]
		self.h = h
		self.w = w
	
	def __add__(self, mat):	# self + mat
#		if (self.h, self.w == mat.h, mat.w):
		ret = Matrix(self.h, self.w)
		for i in range(self.h):
			for j in range(self.w):
				ret.data[i][j] = (self.data[i][j] + mat.data[i][j])
		return ret
	
	def __mul__(self, mat):	# self * mat
		ret = Matrix(self.h, mat.w)
		for i in range(self.h):
			for j in range(mat.w):
				for k in range(self.w):
					ret.data[i][j] += (self.data[i][k] * mat.data[k][j])
		return ret

m1 = Matrix(2,2)
m2 = Matrix(2,2)
m1.data = [[1,2],[3,4]]
m2.data = [[5,6],[7,8]]

m_sum = Matrix(2,2)
m_sum = m1 + m2

print(m_sum.data)
'''
m3 = Matrix(2,1)
m4 = Matrix(1,2)
m3.data = [1,2]
m4.data = [1,2]
'''
m3 = Matrix(2,2)
m4 = Matrix(2,2)
m3.data = [[1,0],[0,1]]
m4.data = [[1,0],[0,1]]

m_product = Matrix(2,2)
m_product = m3 * m4

print(m_product.data)
