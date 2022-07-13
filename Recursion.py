def factorial(n):
    if n == 0 or n == 1: #base case
        return 1
    if ( not(n < 0) ) and (int(n) == n) : #tests that n is positive and is integer
        return n * factorial(n-1)
    else:
        return "Not valid"