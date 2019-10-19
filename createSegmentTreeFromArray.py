def createSegmentTreeFromArray(arr):
    
    arrLength = len(arr)
    
    segmentArr = 0
    
    i=0
    
    #note if leave nodes are N max nodes will 2**h * 2- 1 = 2*N -1(since 2**h is N(leaves))
    #therefore space complexity to create segment tree is O(n)
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
    print(low,"::",high, "::" ,pos)
    
    if low == high:
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


def getRangeSum(arr,segment,ss,se,qs,qe,index):
    mid = int((ss + se)/2)
    if qe < ss or qs > se:
        return 0
    elif qs <= ss and qe >=se:
        return segment[index]
    else:
        return getRangeSum(arr,segment,ss,mid,qs,qe,2*index+1) + getRangeSum(arr,segment,mid+1,se,qs,qe,2*index+2)
    
    
    
print(createSegmentTreeFromArray([-1,2,4,0,7]))
print(getRangeSum([-1,2,4,0,7],createSegmentTreeFromArray([-1,2,4,0,7]),0,4,1,4,0))


