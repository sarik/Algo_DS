com = set()
g=set()
aa=0
den = [[-1] *4 for _ in range(4)]
def findLongestCommonSubstring(str1,str2): 
    
    maxx = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            #helper(str1[i:],str2[j:],'')
            maxx = max(maxx,helperMax(i,j,str1[i:],str2[j:],''))
    
    return com,maxx

def helperMax(i,j,str1,str2,curr):
    if dp[i][j] != -1:
        return dp[i][j]
    
    if len(str1) == 0 or len(str2) == 0:
        if len(curr) != 0:
            com.add(curr)  
            #aa=max(aa,len(curr))
            #print(len(curr))
        dp[i][j]=len(curr)
        return len(curr)
    
    
    
    if(str1[0] == str2[0]):        
        dp[i][j] = helperMax(i,j,str1[1:],str2[1:],curr+str1[0]) 
        return dp[i][j]

    if(str1[0] != str2[0]):
        dp[i][j] = 0
        return 0         

def helper(str1,str2,curr):
    if len(str1) == 0 or len(str2) == 0:
        if len(curr) != 0:
            com.add(curr)    
            return
    
    if(str1[0] == str2[0]):        
        return helper(str1[1:],str2[1:],curr+str1[0])


        
    
    
print(findLongestCommonSubstring("ABAB","ABABA"))
    
    
    