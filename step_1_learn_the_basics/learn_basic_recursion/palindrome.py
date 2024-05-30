#https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/

def palindrome(str,start,end):
    if start<end:
       if str[start] != str[end]:
           return "False"
       palindrome(str, start+1, end-1)
    return "True"
    

str1 = "akaddd"
print(palindrome(str1, 0, len(str1)-1))