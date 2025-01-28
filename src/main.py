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

if __name__ == '__main__':
    decide()
