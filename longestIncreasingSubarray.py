def longestIncreasingSubarray(arr):
    
    no = len(arr)  
    
    longestSubArr=[]
    
    #dp[i] = longestIncreasingSubarray till index i
    dp=[0 for i in range(len(arr))]
    
    dp[0] =1
    maxx=0
    tmax=1
    longestSubArr=[]
    
    for i in range(1,no):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] +1
            tmax += 1           
        else:
            if tmax > maxx:
                longestSubArr = arr[i-tmax:i]
            maxx=max(maxx,tmax)            
            tmax=1
            dp[i] =0
        print(maxx,tmax,i)
    
    if tmax > maxx:
        longestSubArr = arr[-tmax:]
        maxx=max(maxx,tmax)
    
    
        
    
    return maxx,longestSubArr

def longestNonDecreasningSubarray_NonContiguous(arr):
    
    no = len(arr)  
    
   
    
    #dp[i] = longestIncreasingSubarray till index i
    dp=[1 for i in range(len(arr))]
    
   
    
    for i in range(1,no):
        for j in range(0,i):
            if arr[i] >= arr[j]:
                dp[i] = max(dp[j]+1,dp[i])
        
    
    return dp,max(dp)


    


print(longestIncreasingSubarray([2,4,10,16,17,13,14,3,5,1,6,7,13,14,15]))
#answer 2 -[2,4,10],[4,12]
print(longestNonDecreasningSubarray_NonContiguous([-1,3,4,5,2,2,2,2,-1,-1,1,-1]))