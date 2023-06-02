# Everything in this module is from COMPUTATIONAL NUCLEAR ENGINEERING AND RADIOLOGICAL SCIENCE USING PYTHON by Ryan G. McClarre, ISBN  978-0-12-812253-2

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

def simpsons(f, a, b, pieces):
    """Find the integral of the function f between a and b
    using Simpson’s rule
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
    one_sixth = 1.0/6.0
    #initialize the left function evaluation
    fa = f(a)
    for i in range(pieces):
        #evaluate the function at the left end of the piece
        fb = f(a+(i+1)*h/pieces)
        fmid = f(0.5*(a+(i+1)*h/pieces+ a+i*h/pieces))
        integral += one_sixth*h/pieces*(fa + 4*fmid + fb)
        #now make the left function evaluation the right for the next step
        fa = fb
    return integral
