
import numpy as np


# y = ax + b

# fitness_a = 1/n sum( x(y - _y) )
# fitness_b = 1/n sum(y - _y)


def mainFunc(a,b,x):
    return a * x + b

def fitness_a(a,b,data_x,data_y):
    error = 0
    current_y = mainFunc(a,b,data_x)
    error = 1/len(current_y) * sum(data_x*(data_y - current_y))
    return error

def fitness_b(a,b,data_x,data_y):
    error = 0
    current_y = mainFunc(a,b,data_x)
    error = 1/len(current_y) * sum((data_y - current_y))
    return error



x = np.random.rand(20,1)
y = mainFunc(5,7,x)

