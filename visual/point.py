# Considering A, X, B, C, D and every points in inputs as objects defined bellow
def dist(A, X):
    dist = abs(A.x-X.x) + abs(A.y-X.y)
    return dist


def imprecision(A, B):
    if abs(A.x-B.x) <= 5 and abs(A.y-B.y) <= 5:
        return True
    else:
        return False

def determinantOf3points(A, B, C):
    det = A.x*B.y + B.x*C.y + C.x*A.y - B.x*A.y - C.x*B.y - A.x*C.y
    return det


def signDeterminant(A, B, C):
    if determinantOf3points(A, B, C) > 0:
        return("+")
    else:
        return("-")
    
def orientation(G, A, B, C):
    if signDeterminant(G, B, A) == signDeterminant(G, B, C):
        return True
    else:
        return False

    
def barycenter(A, B, C, D):
    if determinantOf3points(A, B, C) + determinantOf3points(B, A, D) != 0:  
        i_x = (determinantOf3points(A, B, C)*D.x + determinantOf3points(B, A, D)*C.x) / (determinantOf3points(A, B, C) + determinantOf3points(B, A, D))
        i_y = (determinantOf3points(A, B, C)*D.y + determinantOf3points(B, A, D)*C.y) / (determinantOf3points(A, B, C) + determinantOf3points(B, A, D))
        i = Point(i_x, i_y, None)
    else:
        # if we have 2 parallel lines
        i = 0
    return i

class Point():
    
    def __init__(self, x, y, draw):
        self.x = x
        self.y = y
        self.draw = draw
        
    # is the point on the segment [AB]
    def onSeg(self, A, B):
        if min(A.x, B.x) - 2 <= self.x <= max(B.x, A.x) + 2 and min(A.y, B.y) - 2 <= self.y <= max(B.y, A.y) + 2:
            return True
        else :
            return False
    
    # is the point the intersection between the segment [AB] and the segment [XY]
    def is_IntersectionOfSegs(self, A, B, X, Y):
        if self.onSeg(A, B) == True and self.onSeg(X, Y) == True:
            return True
        else:
            return False
        
    # is the point an intersection between the segment [AB] and the line defined by the segment [XY]
    def is_IntersectionOfSeg_Line(self, A, B, X, Y):
        if self.onSeg(A, B) == True and self.onSeg(B, X) == False:
            return True
        else:
            return False

    
    # is the point an intersection between the segment [AB] and the ray [XY[ staring from the point X
    def is_IntersectionSeg_Ray(self, A, B, X, Y):
        if self.onSeg(A, B) == True and self.onSeg(X, Y) == False:
            if dist(X, self) > dist(Y, self):
                return True
            else :
                return False
    
    # is this point visible or is there any segment == wall hiding the vision of the point
    def notVisible(self, A, B, c, g):
        if self.onSeg(A, B) == True and self.onSeg(c, g) == True:
            return True
        else:
            return False
     
    # we can see this point, but can we see further ==> this case bellow :
    #  \--•B
    #   \
    #    •A        We can see the point A, but we can also see the point B behind from G   
    #   /
    #  /
    #   •G
    def ableToSeeFurther(self, A, B, c, g):
        if self.onSeg(A, B) == True and c.onSeg(self, g) == True:
            return True
        else:
            return False