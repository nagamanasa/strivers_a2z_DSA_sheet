#https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/

def armstrong(n):
    temp = n
    k = len(str(n))
    sum = 0

    while temp>0:
        sum = sum + ((temp%10)**k)
        temp = temp//10

    if sum==n:
        print("armstrong")
    else:
        print("not armstrong")
        
armstrong(15)