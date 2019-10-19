def maxValue_Knapsack(items,capacity):
    
    dp = [[0] * (capacity+1) for i in range(len(items)+1)]
    
    weight = [0]+[i[1] for i in items]
    values = [0]+[i[0] for i in items]
    
    dp[0][0] = 0
    
    #dp[i][j] - max possible value to make up capacity j using first i items  or less
    for i in range(1,len(items)+1):
        
        for j in range(capacity+1):
            if j < weight[i] and i-1>=0:
                dp[i][j] = dp[i-1][j]
            else:
                #if j-weight[i] >= 0 and i-1>=0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+  values[i])
    
    return [dp[len(items)][capacity],dp[-1][-1]]
    
    
    

print(maxValue_Knapsack([[1,2],[4,3],[5,6],[6,7]],10))

import numpy as np


