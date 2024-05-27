#https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/

#O(n)
# def prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             count+=1
#     if count == 2:
#         print("prime")
#     else:
#         print("not prime")
#     return

import math
def prime(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            count+=1
        if i != (n//i):
            count+=1
    if count == 2:
        print("prime")
    else:
        print("not prime")
    return

prime(5)