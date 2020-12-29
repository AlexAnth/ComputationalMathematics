import numpy as np
import matplotlib.pyplot as plt

x = [-5.5, -10, -5, -1, 0, 1, 5, 10]

m = {}


def fact(n):
    if n <= 1:
        return 1
    if n in m:
        return m[n]
    m[n] = n * fact(n - 1)
    return m[n]


def Taylor(x0, order=50):
    errors = np.zeros((order + 1, 1))
    expected = np.full((order + 1, 1), np.exp(x0))

    term = 1
    series_sum = 1

    for i in range(1, order):  ## each order:
        # construct term
        term = term * x0 / i
        # add term to series_sum
        series_sum += term
        # store error <- series  sum - expected
        errors[i] = np.abs(series_sum - expected[i])

    return series_sum, (errors, expected)


L = np.linspace(-2.5, 2.5, 20)

# plot np.exp(x)
# for each order i=0... calculate Taylor per point L and plot values
# plt.show()

for i in x:
    ans, errors = Taylor(i)
    print('x', i, 'ans :=', ans)

"""
cnt = 0
plt.figure( )
for i in x:
    cnt += 1
    plt.subplot( 2, 4, cnt )
    ans, errors = Taylor( i )
    
    plt.plot( np.arrange( len(errors[0]) ), errors[0]/errors[1] )#'absolute relative error' )
    plt.xlabel( 'order' )
    if i % 4 == 0:
        plt.ylabel( 'absolute relative error' )
    plt.title( 'x = ' + str(i) )
plt.show()"""

plt.plot(L, np.exp(L), label='exp')

for i in range(0, 4):
    # feed all points into Taylor function
    # get y-values
    # plot x, y
    # plt.plot( L, np.sin(L) )
    p = []
    for j in L:
        val = Taylor(j, order=i)[0]
        p.append(val)
    plt.plot(L, p, label='order=' + str(i))
plt.grid()
plt.legend()
plt.show()
