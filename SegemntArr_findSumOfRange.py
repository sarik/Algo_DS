def createSegmentTreeFromArray(arr):
    
    arrLength = len(arr)
    
    #segmentArr = [12345] * (2*arrLength-1)
    
    i=0
    while True:
        if 2**i >= arrLength:
            segmentArr = [12345]* (2**i * 2 -1)
            break
        i += 1
    
    
    helper(arr,segmentArr,0,arrLength-1,0)
    
    return segmentArr
    
#helper create segmentArr from arr where first index is arr,last index is high in original array
#and pos is position of child()  
def helper(arr,segmentArr,low,high,pos):
    #print(low,"::",high, "::" ,pos)
    
    if low == high:#means there is only one element in that range
        segmentArr[pos]=arr[low] #filling child at leaf nodes
        #print("segment at ",str(pos) , "filled with "+ str(arr[low]))
        return
    
    mid = int((high + low) /2)
    
    helper(arr,segmentArr,low,mid,2*pos+1) # we move on to next left child in the next branch
    #,in array child can be found at 2*k +1 and 2*pos +2 pos
    #note low high works on original array pos in segment tree array
    helper(arr,segmentArr,mid+1,high,2*pos+2)
    
    #since we already filled the left and right child recursively,we can use below    
    segmentArr[pos] = segmentArr[2*pos +1] + segmentArr[2*pos +2]

def findSumOfRange(segmentArr,ss,se,qs,qe,i):
    if qe < ss or qs > se:
        return 0
    
    if  qs <=ss and qe >= se:
        print(ss,"::",se,"::",i)
        return segmentArr[i]
    
    mid = int((ss + se)/2)
    
    return findSumOfRange(segmentArr,ss,mid,qs,qe,2*i+1) + findSumOfRange(segmentArr,mid+1,se,qs,qe,2*i+2)


    
    
    
print(createSegmentTreeFromArray([2]))    
print(createSegmentTreeFromArray([2,3,-1,5,-2,9]))

print(findSumOfRange(createSegmentTreeFromArray([2,3,-1,5,-2,9]),0,5,1,3,0))


