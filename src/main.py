LCM = [["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED"],
       ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED"],
       ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED"],
       ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED"],
       ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED"]]


def decide():
    # Setup
    functions = [func1, func2, func3] * 5
    CMV = [False, True, True, True, False] #[False] * 15
    PUM = [[False] * 5 for _ in range(5)]

    # Gather CMV
    #for i in range(len(CMV)):
     #   if functions[i]():
      #      CMV[i] = True

    print(CMV)

    # Calculate PUM
    for i in range(len(PUM)):
        for j in range(len(PUM[0])):
            if LCM[i][j] == "NOTUSED":
                PUM[i][j] = True

            if LCM[i][j] == "ANDD" and (CMV[i] and CMV[j]):
                PUM[i][j] = True

            if LCM[i][j] == "ORR" and (CMV[i] or CMV[j]):
                PUM[i][j] = True

            if i == j:
                PUM[i][j] = "*"
    print(PUM)


def func1():
    return True


def func2():
    return False


def func3():
    return True


if __name__ == '__main__':
    decide()
