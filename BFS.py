all = set()

visited = {}


#bfs
def implementingTree(str):

    #helper(str,'',len(str))

    for  i in range(len(str)+1):
        helper(str,'',i)

    

        
        

            

def helper(str,curr,i):
    if len(curr) == i:
        print(curr)
        all.add(curr)
    #if len(curr) > i:
        #return
    
    #print(curr)
    #all.add(curr)
    
    for ii in range(len(str)):
        helper(str[:ii]+ str[ii+1:],curr+ str[ii],i)
    

    
implementingTree("ABBA")
print(len(all))
print(all)

