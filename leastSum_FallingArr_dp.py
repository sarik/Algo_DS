def leastSum_FallingArr(input):
    #dp=[[0]*(len(input[0])) for _ in range(len(input))]
    #dp[i][k] least sum till input[i][k]
    
    if len(input) == 1:
        return min(input[0])
    
    dp=input
    count=0
    for i in range(1,len(input)):
        for j in range(len(input[0])):
            count+=1
            if j+1 >= len(input[0]):
                dp[i][j] = dp[i][j] + min(dp[i-1][j],dp[i-1][j-1])
            elif j-1 < 0 :
                dp[i][j] = dp[i][j] + min(dp[i-1][j],dp[i-1][j+1])
            else:
                dp[i][j] = dp[i][j] + min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
                
    print(count)
    return min(dp[len(input)-1]) 
    
input=[
       [1,2,3],
       [5,4,6],
       [11,8,9]]

print(leastSum_FallingArr(input))