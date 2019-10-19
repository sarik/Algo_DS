def helper(str,fav):
    print(str)
    if str in fav:
        return 1
    answer =12345
    for i in range(0,len(fav)):
        if str[:i+1] in fav:
            answer = min(answer, 1+ helper(str[i+1:],fav)) 

    
    return answer
            

def minSpacesFromAPos(pos,str,fav):
    answer = 12345
    if pos == len(str):
        return 0
    for j in range(pos,len(str)+1):
        currString = str[pos:j+1]
        if currString in fav:
            #print(minSpacesFromAPos(j+1,str,fav))
            if minSpacesFromAPos(j+1,str,fav)!=None:
                answer=min(answer,minSpacesFromAPos(j+1,str,fav)+1)    
    return answer                    

        
    


fav=["i","am","out","here","noutof","of"]
str="iamoutofhere"

print(helper(str,fav))

print(minSpacesFromAPos(0,str,fav))