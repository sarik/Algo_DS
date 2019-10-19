#question fav array [13,25,311,134,56]
#Given string 2531113425
#Put minimum spaces in string such that all segments are in fav array
#answer 25 311  13134 56 so no of spaces = 4

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

print(minSpacesFromAPos(0,"2531113425",["13","25","311","134","56","31113425"])-1)