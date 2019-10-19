def CalPar(str):
    answer = 0
    
    if str == "()":
        return 1
    
    if len(str) == 0:
        return 0
    
    mid = giveMid(str)
    print(mid)
    
    middle = mid[0]
    if len(str) == 0:
        return 0
    elif middle == len(str)-1:
        answer =  2 * CalPar(str[1:-1])
    else:
        answer =  CalPar(str[0:middle+1])+ CalPar(str[middle+1:])
    
    return answer
    
    
    
def giveMid(str):
    
    stack=[]
    mid=[0 for i in str]
    
    stack.append(0)
    i=1
    
    while i != len(str):
        if str[i] == "(":
            stack.append(i)
        
        else:
            popped = stack.pop()
            mid[popped] = i
        
        i += 1
    
    return mid
            
        
    
print(CalPar("(())()()"))  

print(giveMid("(())((()))"))