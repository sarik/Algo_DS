class LinkedListNode:
    def __init__(self,startValue):
        self.value=startValue
        self.next=None

def convertListToLL(list):
    startNode=LinkedListNode(list[0])
    node=startNode
    for i in list[1:]:
        currNode=LinkedListNode(i)
        node.next=currNode
        node=node.next
    return startNode

def printLL(startNode):
    curr=startNode
    for i in range(20):
        print(curr.value)
        curr=curr.next
    return 0

def changeTailToPoint(startNode,index):
    curr=startNode
    pointedTo = None
    
    for i in range(index):        
        curr=curr.next
    pointedTo = curr
    curr=startNode
    
    prev=None
    while curr:
        #print(curr.value)
        prev=curr
        curr=curr.next
    prev.next= pointedTo
    
    return startNode


myLL = convertListToLL([1,2,3,4,6])
changeTailToPoint(myLL,2)
printLL(myLL)