#https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers/

def sum(n)->int:
    fsum = n
    if n < 1:
        return 0
    fsum = fsum + sum(n-1)
    return fsum

print(sum(5))