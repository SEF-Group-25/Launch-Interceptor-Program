def decide():
    functions = [func1, func2, func3] * 5

    CMV = [False] * 15
    print(CMV)

    for i in range(len(CMV)):
        if functions[i]():
            CMV[i] = True

    print(CMV)




def func1():
    return True


def func2():
    return False


def func3():
    return True

def func7():
    "input: int NUMPOINTS, N_PTS, points[(x,y)] int DIST"
    #create temporary variables
    NUMPOINTS = 5
    N_PTS = 3
    DIST = 1
    points = [(0,0), (1,1), (2,2), (3,3), (4,4)]
    #IF DIST = 0 return True
    #if NUMPOINTS < 3:
        #return False
    for i in range(NUMPOINTS - N_PTS + 1):
        
        #If the first and last point are the same, compare all points between to that point
        if points[i] == points[i + N_PTS - 1]:
            subset = points[i:i + N_PTS]
            for j in range(1, N_PTS - 1):
                a = subset[j][0] - subset[0][0]
                b = subset[j][1] - subset[0][1]
                #Check distance between all points in subset: c = sqrt(a^2 + b^2)
                #if (a ** 2 + b ** 2)**0.5 > DIST:
                #    return True
        else:
            #Calculate line between first and last point acording to ax+by+c=0
            x1, y1 = points[i]
            x2, y2 = points[i + N_PTS - 1]
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            # Formula for calculating closest distance between a point and a line is abs(ax0 + by0 + c) / sqrt(a^2 + b^2)
            #https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
            for j in range(1, N_PTS - 1):
                px, py = points[i + j]
                distance = abs(a * px - b * py +c) / (a ** 2 + b ** 2)**0.5

                #if distance > DIST:
                #    return True


    return False

if __name__ == '__main__':
    decide()
