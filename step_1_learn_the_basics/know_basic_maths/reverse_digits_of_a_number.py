#Given an integer N return the reverse of the given number.
# https://takeuforward.org/maths/reverse-digits-of-a-number

#O(logn) - n is no of digits
def reverse_digits(n)->None:
    rev = 0
    while n>0:
        rem = n % 10
        rev = (rev*10) + rem
        n = n//10
    print(rev)

reverse_digits(100)