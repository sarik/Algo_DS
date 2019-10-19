def convertArrToString(arr):
    st=""
    for i in arr:
        st = st + str(i)
    return st

def powerSet(arr):
    setall =set()
    print(setall)
    
    helper(setall,[],arr,0)
    
    return setall

def helper(setall,prev,arr,index):
    if len(prev) == 3 or index >2:
        setall.add(convertArrToString(prev))
        return
    including = prev + [arr[index]]
    excluding = prev
    
    setall.add(convertArrToString(including))
    setall.add(convertArrToString(excluding))
    helper(setall,including,arr,index+1)
    helper(setall,excluding,arr,index+1)

def powerSet_Short_Org(arr):
    
    powerset=[[]]
    
    for ele in arr:
        for i in range(len(powerset)):
            currentSubset= powerset[i]
            powerset.append(currentSubset+[ele])
    return powerset

def powerSet_Short(arr):
    
    powerset=[[]]
    
    for ele in arr:
        for i in range(len(powerset)):   
                     
            powerset.append(powerset[i]+[ele])
    return powerset
        
    
    

print(powerSet_Short([1,2,3]))