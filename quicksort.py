def partition(arr,low,high):
    
    print(high,low)
    piv = ((high+low)//2)
    
    
    
    pivot = arr[piv]
    arr[high] ,arr[piv] = arr[piv],arr[high]
    
    lessThanPivotTracker = low-1
    
    for j in range(low,high):
        if arr[j] <= pivot:
            lessThanPivotTracker +=  1
            arr[j] ,arr[lessThanPivotTracker] = arr[lessThanPivotTracker],arr[j]
    
    #print(arr)
    
    arr[high] ,arr[lessThanPivotTracker+1] = arr[lessThanPivotTracker+1],arr[high]
    
    #print(pivot,arr,lessThanPivotTracker+1)
    
    return lessThanPivotTracker+1
    

def quicksort(arr,low,high):
    
    if low<high:    
        mid = partition(arr,low,high)
        quicksort(arr,low,mid-1)
        quicksort(arr,mid+1,high)
            
    
    return arr
    

print(quicksort([7,21,33,9,11,23,12,43,64,34],0,9))


