#Given two integers N1 and N2, find their greatest common divisor.
#https://takeuforward.org/data-structure/find-gcd-of-two-numbers/

#O(n)
# def gcd_hcf(n1, n2)-> None:
#     gcd = 1
#     for i in range(1, min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             gcd = i
#     print(gcd)

#O(n): better approach
# def gcd_hcf(n1,n2)->int:
#     for i in range(min(n1,n2), 0, -1):
#         if n1%i==0 and n2%i==0:
#             return i
#     return 1

#O(n): eucledian algorithm-It operates on the principle that the GCD of two numbers remains the same even if the smaller number 
#is subtracted from the larger number.
def gcd_hcf(n1,n2):
    while n1>0 and n2>0:
        if n1>n2:
            n1 = n1-n2
        else:
            n2 = n2-n1
    print(max(n1,n2))

gcd_hcf(59,400)
