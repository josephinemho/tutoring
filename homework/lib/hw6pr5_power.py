#
# hw7pr5.py - Intro to loops!
#
# Name:
#
def power(b,p):
    """Loop-based factorial function
       Argument: a numeric value: b, and a nonnegative integer: p
       Return value: the product of b**p
    """
    result = 1                 # starting value - like a base case
    for x in range(1,p+1):     # loop from 1 to p, inclusive
        result = result * b    # update the result by mult. by b
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
assert power(2,5) == 32
assert power(5,2) == 25