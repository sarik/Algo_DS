#to form string with input i 
#at every step we try to make all possible strings with an input string 
#and a character to be added.so input string comes from 
#removing those character from original string

com = set()
def allTilesCombinates(input):
    
    length = len(input)
    
    for i in range(1,length+1):
        
        helper(input,'',i)
    return len(com)
 
#helper-takes all char from a string and put it with current string till length is k
#def- helper takes a new substring curr and gives all the strings possible with the combination
#of new substring and the given string
    
#taking a k variable so we know when that length has reached
def helper(input,curr,k):
    if len(curr) == k:
        com.add(curr)
        return
    
    for i in range(len(input)):
        helper(input[:i]+input[i+1:],curr+input[i],k)
  
def convertArrToString(arr):
    st=""
    for i in arr:
        st = st + str(i)
    return st
      
def powerset(input):
    ps=[[]]
    all=set()
    
    for ele in input:
        for i in range(len(ps)):
            ps.append(ps[i]+[ele])
            ps.append([ele]+ps[i])
        
    for i in ps:
        conv = convertArrToString(i)
        all.add(conv)
        
    return len(ps),len(all)
            
        
#print(powerset("AAABBC"))
#print(allTilesCombinates("AAABBC"))
print(allTilesCombinates("AC"))