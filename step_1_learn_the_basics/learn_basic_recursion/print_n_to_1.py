#https://takeuforward.org/recursion/print-n-to-1-using-recursion/

#O(n)
def print_n_to_1(i):
    if i < 1:
        return
    print(i)
    print_n_to_1(i-1)

print_n_to_1(5)