from point import Point

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