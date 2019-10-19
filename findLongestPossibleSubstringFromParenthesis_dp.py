#find index of first ()) (()(()))
#dp[i] - length of longest valid string ending at ith inde
def findLongestPossibleSubstring(str):
    dp=(len(str)+1)*[0]
    maxLength=0
    #maxLength will be maximum possible at any iteration,hence need to be updated at each step
    dp[0]=0
    dp[1]=0
    for i in range(2,len(str)+1):
        #print(str[i-1:i-1+1])
        if(str[i-1:i-1+1] == ")"):
            #print(str[i:i+1],i)
            if str[i-2:i-2+1] == "(":
                #print(str[i-1:i-1+1],i)
                if i >=2:
                    dp[i]=dp[i-2]+2
                    #currLength+=2
            elif(str[i-1:i-1+1] == ")") and i-dp[i-1]>=0 and str[i-dp[i-1]-2:i-dp[i-1]-2+1] == "(":
               #dp[i-1] gives the start of valid substring
               #str[i-dp[i-1]-1:i-dp[i-1]-1+1] gives the char just before valid substring which should be "C"
               
               dp[i]=dp[i-1]+2
               #now we need to check if dp[i-dp[i-1]-2] >0 if yes we have to add it 
               if (i-dp[i-1]-2) > 0:
                   dp[i]=dp[i] + dp[i-dp[i-1]-2]
               
               maxLength=max(maxLength,dp[i])
    #print(dp)
    return max(dp)
            
    


print(findLongestPossibleSubstring("()()(())()()))"))

