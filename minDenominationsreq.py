def minCoinUsed(denominations,sum):
    den= [0]*(sum+1)
    den[0] =0
    if sum in denominations:
        return 1
    #den[i] is minimum no of coins required to make sum
    for i in range(1,sum+1):
        den[i]=1234
        print("********")
        for x in denominations:
            if i-x < 0:
                continue            
            den[i]=min(den[i],den[i-x]+1)
            print(den[i])
            
    return den[sum]

minCoinUsed([1,2,5],5)
            
    