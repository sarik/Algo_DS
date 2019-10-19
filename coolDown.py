def calCulateTotalTime(processArr,coolDown):
    
    lastOccurence = {}
    pos=0
    
    for i in processArr:
        if str(i) in lastOccurence:
            print("here for ",str(i))
            if coolDown - (pos - lastOccurence[str(i)]) >0:
                moretimeToWait = coolDown - (pos - lastOccurence[str(i)])
            else:
                moretimeToWait =1
            pos+=moretimeToWait
        else:
            pos +=1
        
        lastOccurence[str(i)] = pos
    
    return pos
        
    

print(calCulateTotalTime([1,1,2,1],2))