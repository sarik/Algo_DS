def validSubstring(str):
    count = 0
    for i in str:
        if count < 0:
            return 0
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1

    return count == 0


def allMinRemovalBrackets(str):

    stack = []
    curr = str
    found = False
    stack.append(curr)

    while(len(stack) > 0):
        popped = stack.pop()
        print(popped)

        # if(validSubstring(popped)):
        # found=True
        # print(popped)
        # break

        if(len(popped)) > 0:
            for i in range(len(popped)):
                if popped[i] == "(" or popped[i] == ")":
                    stack = [popped[:i]+popped[i+1:]] + stack


def allTiles(str):
    stack = []
    all = set()
    visited = {}
   
    curr = str
    found = False
    stack.append(curr)

    while(len(stack) > 0):
        
        popped = stack.pop()
        if visited.get(popped) != None:
            continue

        print(popped)

         

        # if(validSubstring(popped)):
        # found=True
        # print(popped)
        # break
        all.add(popped)
        visited[popped]="seen"


        if(len(popped)) > 1:
            for i in range(len(popped)):
                stack = [popped[:i]+popped[i+1:]] + stack

    print(len(all))

def allTiles2(str):
    stack = []
    for i in str:
        stack.append(i)
    all = set()
    visited = {}
   
    curr = str
    found = False
    stack.append(curr)

    while(len(stack) > 0):
        
        popped = stack.pop()
        if visited.get(popped) != None:
            continue

        print(popped)

         

        # if(validSubstring(popped)):
        # found=True
        # print(popped)
        # break
        all.add(popped)
        visited[popped]="seen"


        if(len(popped)) >= len(str):
            for i in range(len(popped)):
                stack = [popped[:i]+popped[i+1:]] + stack

    print(len(all))

allTiles("ABC")
