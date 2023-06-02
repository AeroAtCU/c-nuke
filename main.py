import math # math.cos is rads
import mathd

print("Hi collin")

''' Define some Functions '''

def linear_equation(x, m=1, b=0):
    y = m*x + b
    return y

def left_reimann_sum(f, interval = [0, 10]):
    for i in range(interval[0], interval[1]):
        print("iteration " + str(i) + ": f=" + str(f(i)))

    return 0


left_reimann_sum(lambda x: 2*x + 0)
print(mathd.sin(45))
