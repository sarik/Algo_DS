def createSegmentTree(arr):
    
    n= len(arr)
    
    i=1
    segmentTree=[]
    
    while True:
        if 2**i >= n:
            segmentTree=[0]* (2**i * 2-1)
            break
        i+=1
        
    
    helper(arr,segmentTree,0,n-1,0)
    return segmentTree

def helper(arr,segmentTree,low,high,pos):
    
    mid = int((high+low)/2)
    
    if high == low:
        segmentTree[pos] = arr[low]
        return
    
    helper(arr,segmentTree,low,mid,2*pos+1)
    helper(arr,segmentTree,mid+1,high,2*pos+2)

    segmentTree[pos] = max(segmentTree[2*pos+1],segmentTree[2*pos+2])    
    
def maxRangeQuery(segmentTree,ss,se,qs,qe,pos):
    if qe < ss or qs > se:
        return -12345
    
    if qe >= se and qs <= ss:
        return segmentTree[pos]
    
    mid = int((ss+se)/2)
    
    left = maxRangeQuery(segmentTree,ss,mid,qs,qe,2*pos+1)
    right = maxRangeQuery(segmentTree,mid+1,se,qs,qe,2*pos+2)
    
    return max(left,right)
    
    

print(createSegmentTree([-1,2,4,3,0,19]))
segmentTree = createSegmentTree([-1,2,4,3,0,19])
print(maxRangeQuery(segmentTree,0,5,2,5,0))
            