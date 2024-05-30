#https://takeuforward.org/arrays/print-fibonacci-series-up-to-nth-term/

#O(2^n): 
# // Base Condition.
#             if(N <= 1){
                
#                 return N;
#             }
            
#             // Problem broken down into 2 functional calls
#             // and their results combined and returned.
#             int last = fibonacci(N-1);
#             int slast = fibonacci(N-2);
            
#             return last + slast;
            

#     }
#     public static void main(String[] args) {

#        // Here, let’s take the value of N to be 4.
#        int N = 4;
#        System.out.println(fibonacci(N));
#     }

def fibonacci(n, arr):
    # Extend the array size to n+1 if it is not long enough
    if len(arr) < n + 1:
        arr.extend([0] * (n + 1 - len(arr)))

    # Base cases: directly set in the array
    if n == 0:
        arr[0] = 0
        return 0
    elif n == 1:
        arr[1] = 1
        return 1

    # Only compute if not already done (avoid recomputation)
    if arr[n] == 0:
        arr[n] = fibonacci(n-1, arr) + fibonacci(n-2, arr)
    
    return arr[n]

# Example usage
arr = []
fibonacci(5, arr)
print(arr)