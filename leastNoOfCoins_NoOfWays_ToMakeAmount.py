def totalWays_NoRep(coins,sum):
    way=[[0]*(sum+1) for _ in range(len(coins)+1)]

    way[0][0]=1
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
            way[i][j]=way[i-1][j]+ way[i][j-i]
    print(way)
    return way[len(coins)][sum]

print(totalWays([1,2],5))

def totalWaysToMakeAmount(coins,sum):
    way=[0]*(sum+1)

    way[0]=1
    
    #w[k] - no of combinations to make up amount k
    
    for i in range(1,sum+1):
        
        for j in coins:
            if i-j >= 0:
                #print(i,i-j)
                way[i] = way[i]+ way[i-j]
    #way[i][j] = no of coins reuired to make up the amount
    return way[sum]
   

def leastNoOfCoinsToMakeAmount(coins,sum):
    way=[12345]*(sum+1)
    stack=[]
    way[0]=0
    #w[k] - least no of coins required to make up sum k
    for i in range(1,sum+1):        
        for j in coins:
            if i-j >= 0:               
                way[i] = min(way[i], way[i-j]+1)
                
    #way[i][j] = no of coins reuired to make up the amount
    print(stack)
    return way[sum]
   
    
#adding a zero before allowed coins
#print(totalWaysToMakeAmount([1,2,3],3))#(12,21,111,3)
print(leastNoOfCoinsToMakeAmount([1,2],4))
