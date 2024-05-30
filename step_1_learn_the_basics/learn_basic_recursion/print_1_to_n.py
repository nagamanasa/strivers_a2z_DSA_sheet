#https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/

#O(n)
def print_1_to_n(i,n):
    if (i>n):
        return
    print (i)
    print_1_to_n(i+1,n)

print_1_to_n(1,5)