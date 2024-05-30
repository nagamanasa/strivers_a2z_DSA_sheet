#https://takeuforward.org/recursion/print-name-n-times-using-recursion/

#O(n)
def print_name(i, n):
    if (i>n):
        return
    print("Naga Manasa Palaparthi")
    print_name(i+1, n)

print_name(1,5)
    