def countNoOfOnesInBinaryRepresentatin(num):
    
    return helper(num)

def helper(num):
    if num == 0:
        return 1;
    if num == 1:
        return 1
    
    if num % 2 == 0:
        return helper(num /2)
    
    return 1 + helper((num-1)/2)
    

print(countNoOfOnesInBinaryRepresentatin(127))