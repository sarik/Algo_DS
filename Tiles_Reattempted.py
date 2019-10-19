allC = set()

    
def countTiles(tiles):
    all = set()
    n=len(tiles)
    
    for i in range(1,n+1):
        helper(tiles,'',i)
    
    
    
    return all
 
def helper(input,curr,k):
    if len(curr) == k:
        
        print(curr)
        return
    
    for i in range(len(input)):
        helper(input[:i]+input[i+1:],curr+input[i],k)


print(countTiles("AC"))
