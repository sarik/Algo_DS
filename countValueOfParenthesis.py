def CalPar(str):
    
    print(str)
    answer =0;
    
    if len(str) == 0:
        return answer
    
    if str[0] == "(":
        if str[1] == ")":
            answer = answer + 1 +CalPar(str[2:]) 
        else:
            count = 1
            
            i=2
            
            b="("
            while True:
                if count == 0 and str[i] == ")":
                    break
                else:
                    print("here")
                    if str[i] == "(":
                        count += 1
                        b = b+ "("
                    else:
                        print("there")
                        count -= 1
                        b = b+ ")"
                i +=1
                        
            
            answer =  2 * CalPar(b)
        
    return answer

print(CalPar("(()()(()))"))
    