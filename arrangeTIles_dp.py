 def numTilePossibilities(tiles: str) -> int:
        res=[]
        def rec(t,now,k):
            nonlocal res
            if k==1:
                for i in t:
                    res.append(now+i)
                return
            for i in range(len(t)):
                rec(t[:i]+t[i+1:],now+t[i],k-1)
        for i in range(1,len(tiles)+1):
            rec(tiles,'',i)
        return(len(set(res)))    
        
def numTilePossibilities2(tiles):
        res=set()
        
        #helper(t,curr,k) puts all possible values of length k possible 
        #from remaining tiles t,
        #curr is the value it already has,so empty for initial condition
        
        def helper(t,curr,k):
            if k==len(curr):
                res.add(curr)
                print(curr)
                return 
                # return so that the loop below doesn't continue 
                #when you meet the length requirement
            
            for i in range(len(t)):
                # call helper with everything but the current value
                helper(t[:i]+t[i+1:], curr+t[i], k)
                
        # start at size 1 and move until size len(tiles),
        #+1 because range doesn't include the endpoint
        for i in range(1,len(tiles)):
            helper(tiles,'',i)
            
        return((len(res))) 
    
def numTilePossibilities(tiles):
    #dp[n] - max combinaions you cn make from first n tiles
    dp =[0]*(len(tiles)+1)
    dp[0]=0
    dp[1]=1
    
    for i in range(2,len(tiles)+1):
        dp[i] = dp[i-1]
        if i-1 >=0:
            for j in range(0,i):               
                dp[i] += (dp[j] +1)
                
    
    return max(dp)

def numTilePossibilities1(tiles: str) -> int:    
        td = collections.defaultdict(int)
        for c in tiles:
            td[c] += 1
        print(td)
            
        def bt(active_keys=set(td.keys())):
            n = 0
            for key in active_keys:
                n += 1                    
                td[key] -= 1
                n = n+bt(active_keys) if td[key] else n+bt(active_keys-{key})
                td[key] += 1
            return n

        return bt()


print(numTilePossibilities2("AAABBC"))
