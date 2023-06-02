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

# print(mcclarren.trapezoid(phi(lambda x:x, k=10), a=-3.0, b=3.0, pieces=1)) # How not to use lambdas:
# replace 'lambda' with 'make a new temp function that takes one argument x. it's definition is:
print(mcclarren.trapezoid(lambda x: phi(x, k=10), a=-3.0, b=3.0, pieces=1))
print(mcclarren.trapezoid(lambda x: phi(x, k=1), a=-3.0, b=3.0, pieces=1))
print(mcclarren.trapezoid(lambda x: phi(x, k=2), a=-3.0, b=3.0, pieces=1))
print(mcclarren.trapezoid(lambda x: phi(x, k=4), a=-3.0, b=3.0, pieces=1))


# Think of it like replacing this:
# lambda x: phi(x, k=10)
# with just `lambda`
# and then previously having this definition
# def lambda(x): phi(x, k=10)
