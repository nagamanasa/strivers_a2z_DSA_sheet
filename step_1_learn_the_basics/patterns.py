#https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

def pattern1(n)->None:
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("\n")

def pattern2(n)->None:
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print("\n")

def pattern3(n)->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print("\n")

def pattern4(n)->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print("\n")

def pattern5(n)->None:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*", end="")
        print("\n")

def pattern6(n)->None:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end="")
        print("\n")

def pattern7(n)->None:
    for i in range(0,n):
        j = 0
        while j<n-i-1:
            print(" ", end="")
            j=j+1
        j = 0
        while j < 2*i+1:
            print("*", end="")
            j=j+1
        j = 0
        while j<n-i-1:
            print(" ", end="")
            j=j+1
        print("\n")


def pattern8(n)->None:
    for i in range(0,n):
        j = 0
        while j<i:
            print(" ", end="")
            j=j+1
        
        j = 0
        while j < (2*n)-(2*i +1):
            print("*", end="")
            j=j+1
        j = 0
        while j<i:
            print(" ", end="")
            j=j+1
        print("\n")

def pattern9(n)->None:
    pattern7(n)
    pattern8(n)

def pattern10(n)->None:
    for i in range(n+1):
        for j in range(0,i):
            print("*",end="")
        print("\n")
    for i in range(n-1,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print("\n")

def pattern11(n)->None:
    for i in range(n):
        if (i % 2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end="")
            if (start == 1):
                start = start - 1 
            else:
                start = start + 1
        print("\n")

def pattern12(n)->None:
    for i in range(1,n+1):
        j=0
        while j<i:
            print(j+1, end="")
            j = j+1

        j=0
        while j<(2*n)-(2*i):
            print(" ",end="")
            j = j+1
        
        j=0
        k = i
        while j<i:
            print(k, end="")
            j = j+1
            k = k-1
        print("\n")

def pattern13(n)->None:
    k = 1
    for i in range(1,n+1):
        for j in range(i):
            print(k,end="")
            k = k+1
        print("\n")

def pattern14(n)->None:
    for i in range(1,n+1): 
        k = 'A'
        for j in range(i):
            print(k,end="")
            k = chr(ord(k)+1)
        print("\n")

def pattern14(n)->None:
    for i in range(1,n+1): 
        k = 'A'
        for j in range(i):
            print(k,end="")
            k = chr(ord(k)+1)
        print("\n")

def pattern15(n)->None:
    for i in range(n,1,-1): 
        k = 'A'
        for j in range(i):
            print(k,end="")
            k = chr(ord(k)+1)
        print("\n")

def pattern16(n)->None:
    k = 'A'
    for i in range(1,n+1): 
        for j in range(i):
            print(k,end="")
        k = chr(ord(k)+1)
        print("\n")

def pattern17(n)->None:
    for i in range(0,n):
        j=0
        while j<n-i-1:
            print(" ",end="")
            j = j+1
        
        j=0
        k='A'
        k = chr(ord(k))
        while j<(2*i)+1:
            print(k,end="")
            if j>=i:
                k = chr(ord(k)-1)
            else:
                k = chr(ord(k)+1)
            j = j+1
        
        j=0
        while j<n-i-1:
            print(" ",end="")
            j = j+1
        print("\n")

def pattern18(n)->None:
    for i in range(1,n+1):
        k = 'F'
        k = chr(ord(k)-i)
        for j in range(i):
            print(k,end="")
            k = chr(ord(k)+1)
        print("\n")

def pattern19(n)->None:
    for i in range(0,n):
        j = 0
        while j<n-i:
            print("*", end="")
            j=j+1
        j = 0
        while j < 2*i:
            print(" ", end="")
            j=j+1
        j = 0
        while j<n-i:
            print("*", end="")
            j=j+1
        print("\n")
    for i in range(0,n):
        j = 0
        while j<=i:
            print("*", end="")
            j=j+1
        j = 0
        while j < (2*n)-(2*i)-2:
            print(" ", end="")
            j=j+1
        j = 0
        while j<=i:
            print("*", end="")
            j=j+1
        print("\n")

def pattern20(n)->None:
    for i in range(0,n):
        j = 0
        while j<=i:
            print("*", end="")
            j=j+1
        j = 0
        while j < (2*n)-(2*i)-2:
            print(" ", end="")
            j=j+1
        j = 0
        while j<=i:
            print("*", end="")
            j=j+1
        print("\n")
    for i in range(0,n):
        j = 0
        while j<n-i:
            print("*", end="")
            j=j+1
        j = 0
        while j < 2*i:
            print(" ", end="")
            j=j+1
        j = 0
        while j<n-i:
            print("*", end="")
            j=j+1
        print("\n")

def pattern21(n)->None:
    for i in range(0,n):
        for j in range(0,n):
            if (i==0 or i==(n-1)):
                print("*",end="")
            elif (i!=0 or i!=n-1) and (j==0 or j==n-1):
                print("*", end="")
            else:
                print(" ",end="")
        print("\n")

def pattern22(n)->None:
    # for i in range(0,(2*n)-1):
    #     for j in range(0,(2*n)-1):
            
    #     print("\n")
    return None
    

pattern1(5)
pattern2(5)
pattern3(5)
pattern4(5)
pattern5(5)
pattern6(5)
pattern7(5)
pattern8(5)
pattern9(5)
pattern10(5)
pattern11(5)
pattern12(5)
pattern13(5)
pattern14(5)
pattern15(5)
pattern16(5)
pattern17(4)
pattern18(5)
pattern19(5)
pattern20(5)
pattern21(4)
pattern22(4)
