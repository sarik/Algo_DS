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
    while curr:
        print(curr.value)
        curr=curr.next
    return 0

def delFromLL(startNode,index):
    curr=startNode
    i=0;
    while(curr):
        if(i == index-1):
            curr.next=curr.next.next
        i+=1
        curr=curr.next
    return startNode

def reverseLL(startNode):
    #startNode.next=None
    curr=startNode
    prev=None      
    while(curr):
        #print(curr.value)
        #print(prev.value)
        temp=curr.next
        curr.next=prev
        #prev is now at curr node and curr at next.so checking if curr(next) is valid and if not return prev 
        # as it is at current node
        prev=curr
        curr=temp
    #print(prev.next)
    return prev      
     

#printLL(convertListToLL([1,2,3,4,5]))
printLL(reverseLL(convertListToLL([1,2,3,4,6])))
