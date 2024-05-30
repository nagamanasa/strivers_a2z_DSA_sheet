#https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive/

def factorial(n):
    product = n
    if n < 1:
        return 1
    product = product * factorial(n-1)
    return product

print(factorial(3))