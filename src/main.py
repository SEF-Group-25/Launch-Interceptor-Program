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

def func4():
    "input: AREA1, POINTS, NUMPOINTS"
    AREA1 = 1
    NUMPOINTS = 4
    POINTS = [(0, 0), (1, 1), (2, 2), (3, 3)]

    for i in range(NUMPOINTS-2):
        if abs((POINTS[i][0]*(POINTS[i+1][1]-POINTS[i+3][1]) + POINTS[i+1][0]*(POINTS[i+3][1]-POINTS[i][1]) + POINTS[i+3][0]*(POINTS[i][1]-POINTS[i+1][1]))/2) > AREA1:
            pass
    "return True if the condition is met, False otherwise"
    return False


if __name__ == '__main__':
    decide()