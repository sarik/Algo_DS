def totalWays(coins,sum):
    way=[[0]*(sum+1) for _ in range(len(coins))]

    way[0][0]=1
    #way[1][1]=1    
     
    print(way)
    #way[i][j] = ways to make up amount j using den of coins i or lesser
    for i in range(len(coins)):
        for j in range(sum+1):
            if j < i:
                way[i][j]= way[i-1][j]
            if i-1 <0 or j-i <0:
                continue
            print(i,"::",j)
            way[i][j]=way[i-1][j]+ way[i][j-coins[i]]
    print(way)
    return way[len(coins)-1][sum]

#adding a zero before allowed coins
print(totalWays([0,1,3,12],20))
