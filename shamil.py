def merge(a, b):
    # write your code here
    # a and b are two sorted list
    # merge function will return a sorted list after merging a and b
    sorted_arr = []
    i, j = 0, 0
    count = 0
    while i < len(a) and j < len(b):
        
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            count += len(a) - i
            j += 1
            
    while i < len(a):
        sorted_arr.append(a[i])
        i += 1
    while j < len(b):
        sorted_arr.append(b[j])
        j += 1
        
    return sorted_arr, count
 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr)//2
        a1, c1 = mergeSort(arr[:mid])  # write the parameter 
        a2, c2 = mergeSort(arr[mid:])  # write the parameter
        
        arr1, count = merge(a1, a2)
        total = c1 + c2 + count
        return arr1,total
        #return merge(a1, a2)          # complete the merge function above 
 
 
N = int(input())
arr = list(map(int, input().split()))
 
sorted_arr, count = mergeSort(arr)
 
print (count)
print(*sorted_arr[:len(sorted_arr)])