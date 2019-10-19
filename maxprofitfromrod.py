def minCoinUsed(denominations,sum):
    profit=[2,5,7,8]
    den= [[0]*(len(denominations)+1) for _ in range(sum+1)]
    print(den)
    
    #den[0][0] =1

    for i in range(1,sum+1):
        den[i][0]=0 
    
    #for i in range(0,len(denominations)+1):
        #den[0][i]=1
    
    #den[i][k] is no of ways to make up profit i using first k pieces from denominations
    for i in range(1,sum+1):  
        k=1  
        print("*********")  
        #print(i)            
        while(k<=len(denominations)):
            #print(k) 
            for x in denominations[:k]:
                #print(" i",i,"x",x)
                #print("x is",x)
                if i-x < 0:
                    continue 
                den[i][x]+=den[i-x][x]
                den[i][x] = max(den[i][x],den[i-x][x]+profit[x])
                #print("i",i,"x",x)
                #print(den[i])
            k+=1

    #for i in range        
    return den[4][sum]

print(minCoinUsed([1,2,3,4],2))
            
    