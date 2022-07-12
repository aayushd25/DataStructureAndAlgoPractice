def factorial(n):
    if n == 0 or n == 1:
        return 1
    if ( not(n < 0) ) and ( n % 10 == 0):
        return n * factorial(n-1)
    else:
        return "Not valid"
print(factorial(10.6))
