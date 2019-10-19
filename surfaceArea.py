def totalSurfaceArea(arr):
    area=0
    
    i=0
    j=1
    
    while(i<len(arr)-1):
        while(j< len(arr)):
            if arr[i] == 0:
                i += 1
                j+=1
                continue
            if arr[j] == 0:
                j +=1
                continue
            area += (j-i+1)* min(arr[j],arr[i])
            i=j
            j +=1
            

    return area

def waterArea(heights):
    maxes=[0 for height in heights]
    leftMax=0
   
    for i in range(len(heights)):
        height =heights[i]
        maxes[i]=leftMax
        leftMax= max(leftMax,height)
    
    rightMax=0

    print(maxes)

    for i in reversed(range(len(heights))):
        height=heights[i]
        minHeight=min(rightMax,maxes[i])
        if height <minHeight:
            maxes[i]=minHeight-height
        else:
            maxes[i]=0
        rightMax=max(rightMax,height)

    print(maxes)

    return sum(maxes)

arr=[0,8,0,0,5,0,0,10,0,0,1,1,0,3] 
print(totalSurfaceArea(arr))
print(waterArea(arr))


leftmax- [0, 0, 8, 8, 8, 8, 8,  8, 10, 10, 10, 10, 10, 10]
original [0, 8, 0, 0, 5, 0, 0, 10,  0,  0,  1,  1,  0,  3]

[0, 0, 8, 8, 3, 8, 8,  0,  3,  3,  2,  2,  3,  0]

