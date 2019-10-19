#n2 complexity
def jumpArray(arr):
      
    n=len(arr)
    dp=[12345]*len(arr)
    #dp[k]- reach end from kth pos
    dp[n-1]=0
    
    for i in reversed(range(0,n-2+1)):#+1 since last index is excluded in range
        #print("i",i)
        for j in range(i+1,i+arr[i]+1):
            if j<n:
                dp[i] = min(dp[i],dp[j]+1)
    
    return dp[0]

    
    
    
print(jumpArray([2,3,1,1,2,1]))

        
