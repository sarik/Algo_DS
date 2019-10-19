#find no of ways such that in noOfRolls no of rolls, 
#number i doesnt occur consecutively more than arraywithmaxconsectiverollAllowed no of times
def diceRollProblem(noOfRolls,arraywithmaxconsectiverollAllowed):
    
    totalCombinations = 6 ** noOfRolls
    setsToNotConsider = 0
    
    for i in (arraywithmaxconsectiverollAllowed):
        if i  < noOfRolls:
            for z in range(i+1,noOfRolls+1): #to include last value
                setsToNotConsider = setsToNotConsider + (noOfRolls-z)+1 
                # if size is k,you can have k-l+1 combinations of consecutive l occurence in k
   
    return (totalCombinations-setsToNotConsider)          
            
    
    
print(diceRollProblem(3,[1,1,1,2,2,3]))