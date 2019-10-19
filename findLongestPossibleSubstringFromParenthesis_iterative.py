#find index of first ()) (()(()))
def findLongestPossibleSubstring(str):
    stack=[]
    #stack.append(str[0:1])
    noOfLefts=0
    noOfRights=0
    answer=0
    longest=0
    answerStack=[]
    #while len(stack)>0:
    for i in range(0,len(str)+1):
        #if len(stack) == 0 and str[i:i+1]==")":            
            #continue
        if str[i:i+1]=="(":
            noOfLefts +=1
            #print("left",noOfLefts)
            stack.append(str[i:i+1])
        if str[i:i+1]==")":
            noOfRights +=1
            #print("right",noOfRights)
            if noOfRights<= noOfLefts:
                stack.pop()                
                answer+=2
                print(answer)
                answerStack.append(answer)
                if i == len(str):
                    longest = answer
                if(len(stack)==0):                    
                    longest = max(longest,answer)
                    #answer=0
            else:
                print("here",i,noOfRights,noOfLefts)
                longest=max(longest,answer)
                answer=0
                stack=[]
                noOfLefts=0
                noOfRights=0
    return answerStack,longest


print(findLongestPossibleSubstring("()(()))))(((())))"))
