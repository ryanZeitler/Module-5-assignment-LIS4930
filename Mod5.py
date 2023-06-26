class Rectangle:
    
    def __init__(self,posn,w,h):
        self.corner = posn
        self.width = w
        self.height = h
        
    def __str__(self):
        return "({0},{1},{2})".format(self.corner,self.width,self.height)
        

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    
def create_rectangle(x,y,width,height):
    return Rectangle(Point(x, y), width, height)  # creats new rectangle

def str_rectangle(rect):
    return str(rect)            #returns rectangle as a string

def shift_rectangle(rect,dx,dy):            
    rect.corner.x += dx                 #shifts the corner/point values by dx, and dy
    rect.corner.y += dy

def offset_rectangle(rect,dx,dy):
    newRect = Rectangle(Point(rect.corner.x,rect.corner.y),rect.width, rect.height)    #creats new rectangle by taking rect.corner as x and using that to get point
    shift_rectangle(newRect,dx,dy)                          #shifts new rectangle 
    return newRect
    

r1 = create_rectangle(10, 20, 30, 40)
print (str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print (str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print (str_rectangle(r1))# should be same as previous
print (str_rectangle(r2))

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) 
print("box: ", box)
print("bomb: ", bomb)
