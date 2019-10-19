def partition(low,high,arr):
    
    pivot = int((low+high)/2)
    print(pivot)
    
    arr[high],arr[pivot] = arr[pivot],arr[high]
    
    pivot = arr[high]
    
    
    lessValuesTracker = -1
    print(arr)
    
    for j in range(low,high-1):
        if arr[j] <= pivot:
            
            lessValuesTracker += 1
            print(lessValuesTracker,j)
            arr[j],arr[lessValuesTracker] = arr[lessValuesTracker],arr[j]    
    
    
    arr[high],arr[lessValuesTracker+1] = arr[lessValuesTracker+1],arr[high]
    return arr


print(partition(0,5,[2,11,4,1,45,32]))
            
        