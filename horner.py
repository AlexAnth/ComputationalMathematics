import numpy as np

a = np.array( [ [ 3, 0, -2, 0, 1, 0 ] ] ).T
x0 = -2

def horner( a, x0 ):
	#create array b
	b = np.zeros_like(a)
	#print(b)
	b[0] = a[0]
	
	for i in range(1,a.shape[0]):
		b[i] = b[i-1]*x0 + a[i]
	return b[-1]

print( horner( a, x0 ) )