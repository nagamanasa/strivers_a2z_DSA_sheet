#https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/

#O(n)
# def print_all_divisors(n)->None:
#     divisors = []
    
#     for i in range(n,0,-1):
#         if n%i == 0:
#             divisors.append(i)

#     print(divisors)

#O(n): We can optimise the previous approach by using the property that for any non-negative integer n, 
#if d is a divisor of n then n/d is also a divisor of n.
# def print_all_divisors(n)->None:
#     divisors = []
    
#     for i in range(n,0,-1):
#         if n%i == 0:
#             divisors.append(i)

#     print(divisors)

#O(logn): This property is symmetric about the square root of n by traversing just the first half we can avoid redundant iteration and computations improving the efficiency of the algorithm.
import math
def print_all_divisors(n)->None:
    divisors = []
    
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
        
        if i != n//i:
            divisors.append(n//i)

    print(divisors)

print_all_divisors(36)