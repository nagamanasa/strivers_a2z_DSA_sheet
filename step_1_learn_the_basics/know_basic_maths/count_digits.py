# Given an integer N, return the number of digits in N.
# https://takeuforward.org/data-structure/count-digits-in-a-number/

#method 1: O(n) - length of digits
# def count_digits(n) -> None:
    # string_n = str(n)
    # print(len(string_n))

# method 2: O(logn)
# def count_digits(n) -> None:
#     count = 0
#     while n>0:
#         count = count+1
#         n = n//10
#     print (count)

#method 3: O(1)
import math
def count_digits(n) -> None:
    count = int(math.log10(n) + 1)
    print(count)

count_digits(1233335)