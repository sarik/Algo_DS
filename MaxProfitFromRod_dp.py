def totalWays(coins,sum,profit):
    way=[[0]*(sum+1) for _ in range(len(coins)+1)]

    way[0][0]=0
    #way[1][1]=1    
     
    print(way)
    #way[i][j] = ways to make up amount j using den of coins i or lesser
    for i in range(len(coins)+1):
        for j in range(sum+1):
            if j < i:
                way[i][j]= way[i-1][j]
            if i-1 <0 or j-i <0:
                continue
            print(i,"::",j)
            way[i][j]=max(way[i-1][j], way[i][j-i]+profit[i])
    print(way)
    return way[len(coins)][sum]

print(totalWays([1,2],3,[0,2,5,7,8]))