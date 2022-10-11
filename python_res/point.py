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



def visualisation(guard, corners):

    global pointsSeen
    global pointsNotSeen
    
    pointsSeen = []
    pointsNotSeen = []
    
    corners[-1] = corners[0]
    
    for seg in range(len(corners) - 1):
        for point in range(len(corners)):
            i = barycenter(corners[seg], corners[seg+1], corners[point], guard)
            
            if i == 0:
                pass
            
            elif i.notVisible(corners[seg], corners[seg+1], corners[point], guard) == True and imprecision(i, corners[point]) == False:
                pointsNotSeen.append(corners[point])
                
    pointsNotSeen = [p for p in corners if p in pointsNotSeen]
    pointsSeen = [p for p in corners if p not in pointsNotSeen]
    
    vision = []
    for n in range(len(pointsSeen)):
        vision.append((pointsSeen[n].x, pointsSeen[n].y))

    for point in range(len(pointsSeen)):
        alignedPoints = []
        for seg in range(len(corners)-1):
            
            i = barycenter(corners[seg], corners[seg+1], pointsSeen[point], guard)
            if i.ableToSeeFurther(corners[seg], corners[seg+1], pointsSeen[point], guard) == True and imprecision(i, pointsSeen[point]) == False:
                for n, pt in enumerate(corners):
                    if pointsSeen[point] == pt:
                        if orientation(guard, corners[n-1], pointsSeen[point], corners[n+1]) == True:
                            alignedPoints.append(i)
                                
        alignedPoints.sort(key=lambda P:dist(P, guard))

        if len(alignedPoints) != 0:
            for p in range(len(corners)-1):
                if pointsSeen[point] == corners[p]:
                    for p2 in range(len(corners)-1):
                        
                        if alignedPoints[0].onSeg(corners[p2], corners[p2 + 1]) == True and p < p2:
                            pointsSeen.insert(point+1, alignedPoints[0])
                            point += 1
                            
                        elif alignedPoints[0].onSeg(corners[p2], corners[p2 + 1]) == True and p > p2:
                            pointsSeen.insert(point, alignedPoints[0])
                            point += 1
                            
    draw(pointsSeen, guard)


def draw(pointsSeen, guard):
    global vision
    list_points = []
    for point in pointsSeen:
        list_points.append((point.x, point.y))
        

    vision = cnv.create_polygon(list_points, fill='#FFEA00', tag='vision')
    cnv.tag_raise('guard')
    cnv.create_oval(guard.x - 10, guard.y - 10, guard.x + 10, guard.y  + 10, fill='#FF3D00')


    return