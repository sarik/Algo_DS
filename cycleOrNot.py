def cycleOrNot(arr):
    
    n=len(arr)
    last = n-1
    set=[]
    curr=0
    set.append(curr)
    
    for j in range(6):  
        i = arr[curr]
        #print("jump is",arr[curr])
        if curr + i >=n:
            curr= (curr+i-last-1)            
        elif curr +i < 0:
            curr = (last +1)- abs(curr - abs(i))
        else:            
            curr = curr + i
        print("index after jump",curr)
        if curr in set and j != 5:
            return False
        set.append(curr)
    
    return curr== 0
            
    
    
    
print(cycleOrNot([2,3,1,-4,-4,2]))