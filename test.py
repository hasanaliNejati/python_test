import random as rand
import numpy as np
import matplotlib.pyplot as plot


#3 * x + 5
x = np.random.rand(1000,1)
y = 3 * x + 5



#1/n sum(y- y@)^2
#1/n sum(y - ax + b)^2

#-2/n sum x(y-y@)
#-2/n sum (y-y@)

a = 0
b = 0

rate = 0.5
count = 10000

a_error = []
b_error = []

n = len(x)
for i in range(count):
    _y = a * x + b
    
    a_error.append((-2/n) * sum(x * (y-_y)))
    a -= rate * a_error[i]
    b_error.append((-2/n) * sum((y - _y)))
    b -= rate * b_error[i]
    
    print (f"a : {a}  b : {b}")
    
    if -0.01 < a_error[i] < 0.01 and -0.01 < b_error[i] < 0.01:
        break
    
plot.plot(a_error)
plot.plot(b_error)
plot.show()