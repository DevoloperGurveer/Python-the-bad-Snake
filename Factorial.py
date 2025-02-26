def factorial(x):
    '''this ais Recursice function use to find factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 0",factorial(0))
print("The factorial of 35",factorial(35))
print("The factorial of 69",factorial(69))
print("The factorial of 102",factorial(102))