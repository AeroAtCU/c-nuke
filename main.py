import math # math.cos is rads
import mcclarren
import mathd

print("Hi")

def linear_equation(x, m=1, b=0):
    y = m*x + b
    return y

# Also referred to as f(x)
def phi_integrand(x, k=1, D=1, summation_a=1):
    # dk is 'left out' because it's part of the integral
    # k and x in rads
    numerator = math.cos(k*x)
    denominator = 2*math.pi*(D*k**2 + summation_a)
    phi_integrand = numerator / denominator

    return phi_integrand

def phi_estimate(x, L=3, pieces=256, est_algorithm="trapezoid", k=1):
    '''
    x: obvious
    L: the integral is evaluated between [-L, L]
    pieces: number of dx's
    k: thing inside the cos, in rads (?), I think it's the 'wave number'
    '''

    if "trap" in est_algorithm.lower():
        return mcclarren.trapezoid(lambda x: phi_integrand(x, k=k, D=1, summation_a=1), -L, L, pieces) + 0
    if "simp" in est_algorithm.lower():
        return mcclarren.simpsons(lambda x: phi_integrand(x, k=k, D=1, summation_a=1), -L, L, pieces) + 0

    raise Exception("Attempting to use an un-implmented integration est_algorithm")

def phi_solution(x):
    return 0.5*math.e**-x

# We should expect this to 'hone in' on a value as it adds more pieces (hint: it doesn't idk why)
print("Varying pieces...")
trap_vary_pieces = [phi_estimate(1, L=100000000, pieces=pieces, est_algorithm="trap", k=1) for pieces in [0, 1, 10, 50, 100, 256]]
for val in trap_vary_pieces: print (val)

print("Varying k...")
trap_vary_k = [phi_estimate(1, L=100000000, pieces=10000, est_algorithm="trap", k=k) for k in [0, 1, 2, 3, 5, 10, 100, 1000]]
for val in trap_vary_k: print (val)

print("Varying L...")
trap_vary_L = [phi_estimate(1, L=L, pieces=10000, est_algorithm="trap", k=1) for L in [10, 100, 1000, 10000, 100000, 1000000, 1000000000]]
for val in trap_vary_L: print (val)

# print("x=1, Trap estimate:" + str(phi_estimate(1, L=100000000, pieces=10000, est_algorithm="trap", k=1)))
# print("x=1, Simp estimate:" + str(phi_estimate(1, est_algorithm="simp")))
print("x=1 Exact Solution:" + str(phi_solution(1)))

# return mcclarren.trapezoid(lambda x: phi(x, k=4), a=-3.0, b=3.0, pieces=1)
# Think of it like replacing this:
# `lambda x: phi(x, k=10)`
# with just `lambda`
# and then previously having this definition
# `def lambda(x): phi(x, k=10)`
# In fact don't think about it that way, it's equivalent
