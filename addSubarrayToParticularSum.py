def addSubarrayToParticularSum(arr,numb):
    if numb == 0:
        return 1 #one one such combiantion -empty subarray
    
    summ = 0
    
    if len(arr) == 0:
        return 0
    
    print("here"+str(sum(arr)))
    if sum(arr) == numb:
        summ = 1
    else:
        summ = addSubarrayToParticularSum(arr[1:],numb-arr[0]) + addSubarrayToParticularSum(arr[1:],numb)
    
    return summ   
    
    
print(addSubarrayToParticularSum([2,4,10,12,13,3],16))
#answer 2 -[2,4,10],[4,12]