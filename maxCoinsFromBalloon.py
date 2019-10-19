def maxCoins(arr):
    
    n= len(arr)
    dp= [[0 for i in arr] for i in arr]
    
    print(dp)
    
    #dp[a][b] result for range a to b
    
    for l in reversed(range(n)):
        for r in range(l,n):
            for k in range(l,r+1):
                dp[l][r] = max(dp[l][r],
                                    arr[k]*(arr[l-1] if l-1>=0 else 1)*(arr[r+1] if r+1<n else 1)
                                    +(dp[l][k-1] if k-1>=l else 0 )+(dp[k+1][r] if k+1<=r else 0))
                                    
    
    return dp[0][n-1]

    
    
print(maxCoins([3,1,5,8]))