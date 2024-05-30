#https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/

def hash2(arr):
    map = {}
    for i in range(len(arr)):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]]+=1
    
    # Sorting the dictionary by values in ascending order
    sorted_dict = sorted(map.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict[0])
    print(sorted_dict[-1])

    return

arr = [10,5,10,15,10,5]
hash2(arr)
