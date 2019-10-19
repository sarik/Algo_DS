class Coord:
    
    def __init__(self,x,y):
        self.x = x
        self.y=y
        

#first = Coord(2,3)
#second = Coord(4,3)
#third = Coord(6,3)
#fourth = Coord(2,6)
#fifth = Coord(4,6)
#sixth = Coord(6,6)
        
first = Coord(0,0)
second = Coord(0,1)
third = Coord(1,1)
fourth = Coord(1,0)
fifth = Coord(2,1)
sixth = Coord(2,0)
seventh = Coord(3,1)
eighth = Coord(3,0)

#time complexity n**2
#space complexity n**2 to store y coordinate * y coordinate combinations
def countRectangles(allPoints):
    set = {}
    answer = 0
    for point in allPoints:
        for point_above in allPoints:
            set[str(point_above.y)+"::"+str(point.y)] = 0
    print(set)
            
    for point in allPoints:
        for point_above in allPoints:            
            if (point_above.y > point.y and point.x == point_above.x):               
                
                answer += int(set[str(point_above.y)+"::"+str(point.y)])                   
                set[str(point_above.y)+"::"+str(point.y)] += 1               
                    
    print(set)
    return answer
                
                
        

print(countRectangles([first,second,third,fourth,fifth,sixth,seventh,eighth]))