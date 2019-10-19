def threeNumSum(arr,sumReq):
    
    n= len(arr)
    j=0
    k=0
    
    powerSet=[]
    
    for i in range(n-1):
        first = arr[i]
        j=i+1
        k=n-1
        while (j<k):
            
            sum = first + arr[j] + arr[k]
            #print(first , arr[j] , arr[k],sum)
            
            if sum < sumReq:
                j = j+1
            if sum > sumReq:
                k= k-1
            if sum == sumReq:
                powerSet.append([first,arr[j],arr[k]]) 
                j = j+1
                k = k-1
            
    
    return powerSet
    

print(threeNumSum([-8,-6,1,2,3,5,6,12],0))