import random as rand
import numpy as np
import matplotlib.pyplot as plot


#3 * x + 5
x = np.random.rand(100,1)
y_noise = x = np.random.rand(100,1)

y = (3 * x + 5) + y_noise





#1/n sum(y- y@)^2
#1/n sum(y - ax + b)^2

#-2/n sum x(y-y@)
#-2/n sum (y-y@)

a = 0
b = 0

rate = 0.1
count = 10000

a_errorList = []
b_errorList = []

n = len(x)
for i in range(count):
    _y = a * x + b
    
    a_error = (-2/n) * sum(x * (y-_y))
    a_errorList.append(a_error)
    a -= rate * a_error
    
    b_error = (-2/n) * sum((y - _y))
    b_errorList.append(b_error)
    b -= rate * b_error
    
    print (f"a : {a}  b : {b}")
    
    if -0.01 < a_error < 0.01 and -0.01 < b_error < 0.01:
        break
    
plot.plot(a_errorList)
plot.plot(b_errorList)
plot.show()