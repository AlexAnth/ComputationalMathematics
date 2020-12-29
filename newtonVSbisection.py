import numpy as np
import matplotlib.pyplot as plt

tol = 1e-6

#declare f
def f(x):
    return np.exp(x) - 2

#declare df
def df(x):
    return np.exp(x)

x = np.linspace( 0, 2, 100 )

#Plot f
plt.plot( x, f(x) )

#declare Newton
#x0 = 1.25
def Newton( x0 ):
    errors = []
    x_next = x0 - f(x0) / df(x0)
    errors.append( x_next-x0 )
    #or iterate for n_max=100 iterations
    while True:
        #break when tolerannce is met
        if np.abs( x_next - x0 ) < tol:
            break
        x0 = x_next
        x_next = x0 - f(x0) / df(x0)
        #store error
        errors.append( x_next-x0 )
    return x_next, errors

"""
x0 = 0.8
plt.plot( x0, f(x0), '^' )
x_final, errors = Newton( x0 )
print( 'from x0', x0, 'to x_final', x_final, 'with f', f(x_final))
plt.plot( x_final, f(x_final), '*' )
print( 'iterations', len( errors ) )
plt.grid()
#exit(0)
"""

def sign( x ):
    if x > 0:
        return 1
    return -1
#declare bisection
def bisection( lo, hi ):

    errors = [ hi-lo ]

    while True:
        #condition, break on tolerance
        if hi-lo < tol:
            break
        mid = lo + (hi-lo) / 2
        f_lo = f(lo)
        f_mid = f(mid)
        #f_hi = f(hi)
        #apo [lo,hi]
        #eite se
        #[ lo, mid ] <- f_lo * f_mid < 0
        #eite se
        #[ mid, hi ]
        if sign(f_lo) * sign(f_mid) < 0:
            hi = mid
        else:
            lo = mid
        errors.append( hi-lo )

    solution = lo + (hi-lo) / 2
    return solution, errors

a, b = 0, 2
x0 = a + (b-a) / 2
plt.plot( x0, f(x0), '^' )
x_final, errors = bisection( a,b )
print( 'from x0', x0, 'to x_final', x_final, 'with f', f(x_final))
plt.plot( x_final, f(x_final), '*' )
print( 'iterations', len( errors ) )
plt.grid()
plt.show()


"""
#plot bisections errors
x_val, b_errors = bisection( 0, 2 )
#plot newton errors
x2, n_errors = Newton( 20.5 )

#print bisection and newton solutions

print( 'bisection val' )
print( x_val )

print( 'newton val' )
print( x2 )

plt.plot( np.arange( len(n_errors) ), n_errors, label='newton' )
plt.plot( np.arange( len(b_errors) ), b_errors, label='bisection' )
plt.legend()
plt.grid()
plt.show()

"""