#https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2

def linear_search(num,k):
    for i in num:
        if i == k:
            return True
        else:
            return False

num = [1,2,3,4,5]
k = 5
print(linear_search(num,k))