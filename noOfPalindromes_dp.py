
def countNoOfPalindromeSubstrings(str):   
    dp=[[-2]*len(str) for _ in range(len(str))]
    answer=0
    
    #n**2 loops to get all the substrings
    for i in range(0,len(str)):
        for j in range(0,i+1):
            
            answer += ifIJisPal(j,i,str,dp)
    
    return answer

#check whet
def ifIJisPal(j,i,str,dp):
    print(i,"::",j)    
    
    if dp[i][j] != -2:
        return dp[i][j]

    
    if(i == j):
        dp[i][j]=1
        return 1
    
    #replacing the commented section below to handle condition with substring with len2
    if (j > i):
        dp[i][j]=1
        return 1
    
#    if(i == j+1):
#        if str[i] == str[j]:
#            dp[i][j]=1
#            return 1        
#        else:
#            dp[i][j]=0
#            return 0
        
    if str[j] != str[i]:
        dp[i][j]=0
        return 0
    else:
        return ifIJisPal(j+1,i-1,str,dp)
    
print(countNoOfPalindromeSubstrings("ABBA"))