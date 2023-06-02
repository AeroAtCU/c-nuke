import math # math.cos is rads
import mcclarren
import mathd

print("Hi collin")

def linear_equation(x, m=1, b=0):
    y = m*x + b
    return y

def phi(x, k=0, D=1, summation_a=1):
    # dk is 'left out' because it's part of the integral
    # k in degrees
    numerator = mathd.cos(k*x)
    denominator = 2*math.pi*(D*k**2 + summation_a)
    phi_of_x = numerator / denominator

    return phi_of_x

def phi_solution(x):
    return 0.5*math.e**-x


# Just to make things shorter. See bottom for lambda explain
def trap_phi(k, a, b, pieces):
    return mcclarren.trapezoid(lambda x: phi(x, k), a, b, pieces)

# We should expect this to 'hone in' on a value as it adds more pieces
trap_vary_pieces = [trap_phi(0.1, -3, 3, pieces) for pieces in [1, 10, 50, 100, 256]]
for val in trap_vary_pieces: print (val)

print(trap_phi(0.1, 0, 1, 256))
print(phi_solution(1))

# return mcclarren.trapezoid(lambda x: phi(x, k=4), a=-3.0, b=3.0, pieces=1)
# Think of it like replacing this:
# `lambda x: phi(x, k=10)`
# with just `lambda`
# and then previously having this definition
# `def lambda(x): phi(x, k=10)`
# In fact don't think about it that way, it's equivalent
