import math
def acos(theta_deg): return math.acos(math.radians(theta_deg))
def acosh(theta_deg): return math.acosh(math.radians(theta_deg))
def asin(theta_deg): return math.asin(math.radians(theta_deg))
def asinh(theta_deg): return math.asinh(math.radians(theta_deg))
def atan(theta_deg): return math.atan(math.radians(theta_deg))
def atan2(theta_deg): return math.atan2(math.radians(theta_deg))
def atanh(theta_deg): return math.atanh(math.radians(theta_deg))
def cos(theta_deg): return math.cos(math.radians(theta_deg))
def cosh(theta_deg): return math.cosh(math.radians(theta_deg))
def sin(theta_deg): return math.sin(math.radians(theta_deg))
def sinh(theta_deg): return math.sinh(math.radians(theta_deg))
def tan(theta_deg): return math.tan(math.radians(theta_deg))
def tanh(theta_deg): return math.tanh(math.radians(theta_deg))

def trapezoid(f, a, b, pieces):
    """Find the integral of the function f between a and b
    using pieces trapezoids
    Args:
    f: function to integrate
    a: lower bound of integral
    b: upper bound of integral
    pieces: number of pieces to chop [a,b] into
    Returns:
    estimate of integral
    """
    integral = 0
    h=b-a
    #initialize the left function evaluation
    fa = f(a)
    for i in range(pieces):
        #evaluate the function at the left end of the piece
        fb = f(a+(i+1)*h/pieces)
        integral += 0.5*h/pieces*(fa + fb)
        #now make the left function evaluation the right for the next step
        fa = fb
        return integral
