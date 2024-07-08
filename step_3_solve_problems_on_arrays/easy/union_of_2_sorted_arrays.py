#https://takeuforward.org/data-structure/union-of-two-sorted-arrays/

def union(num1, num2):
    
    s = set()
    for i in range(len(num1)):
        s.add(num1[i])
    for i in range(len(num2)):
        s.add(num2[i])
    
    return list(s)

num1 = [1,2,3,4,5]
num2 = [2,3,4,4,5]

num = union(num1,num2)
print(num)