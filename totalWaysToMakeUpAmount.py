def minCoinUsed(denominations,sum):
    den= [[0]*(len(denominations)+1) for _ in range(sum+1)]
    
    #den[0][0] =1

    for i in range(1,sum+1):
        den[i][0]=0 
    
    for i in range(0,len(denominations)+1):
        den[0][i]=1
    
    #den[i][k] is no of ways to make up some i using first k coins from denominations
    for i in range(1,sum+1):  
        k=1  
        print("*********")  
        #print(i)            
        while(k<=len(denominations)):
            print(k) 
            for x in denominations[:k]:
                print(" i",i,"x",x)
                #print("x is",x)
                if i-x < 0:
                    continue 
                den[i][x]+=den[i-x][x]
                print("i",i,"x",x)
                #print(den[i])
            k+=1

    #for i in range        
    return den[sum]

print(minCoinUsed([2,3,5],2))
            
    