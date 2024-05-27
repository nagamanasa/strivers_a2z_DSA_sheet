#Check if a number is Palindrome or Not
# https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/

#method 1:O(logn)
def checkPalindrome(n):
    rev = 0
    temp = n
    while temp>0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp//10
    if n == rev:
        print("palindrome")
    else:
        print("not a palindrome")
    
checkPalindrome(1011)