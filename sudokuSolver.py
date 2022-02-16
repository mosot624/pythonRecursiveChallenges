global arrayOfImmoveAbleChar
sudokumapval =  []
def checkSubSquare(valCheck,mapArr, valy,valx):
    checkery = -3
    checkerx = -3
    checkVal = 0
    for i in range(3):
        if valy >= checkVal:
            checkery +=3
        if valx >= checkVal:
            checkerx +=3
        checkVal +=3
    for i in range(3):
        for z in range(3):
            dupVal = mapArr[checkery+i][checkerx+z]
            if dupVal == valCheck:
                return 0
    return 1

def checkIfValAllowed(valCheck,mapArr,y,x):
    # valx = 0
    # valy = 0 
    # for y in range(index):
    #     valx += 1
    #     if valx == 9:
    #         valx =0
    #         valy +=1
    for i in range(9):
        valueofX = mapArr[y][i]
        ValueOfY = mapArr[i][x]
        if ValueOfY == valCheck:
            return 0
        if valueofX == valCheck:
            return 0
    if checkSubSquare(valCheck,mapArr, y,x) == 0:
        return 0
    return 1

def solverpart2(y,x):
    if x >= 9:
        x = 0
        y += 1
    if y >=9:
        return
    if arrayOfImmoveAbleChar[y][x] >= 2:
        x += 1
    for z in range(1,10):
        booleanchecker = checkIfValAllowed(z,sudokumapval,y,x)
        if booleanchecker == 1:
            sudokumapval[y][x] = z
            solverpart2(y,x)
            sudokumapval[y][x] = 0
    return

def sudokuRecursionversion2():
    for y in range(9):
        for x in range(9):
            if sudokumapval[y][x] == 0:
                for z in range(1,10):
                    booleanchecker = checkIfValAllowed(z,sudokumapval,y,x)
                    if booleanchecker == 1:
                        sudokumapval[y][x] = z
                        if x == 8 and y == 8:
                            sudokumap(sudokumapval)
                        sudokuRecursionversion2()
                        sudokumapval[y][x] = 0
                return


#checkIfValAllowed(i,sudokumapval,valy,valx)
#Depricated
# def sudokuRecursion(n,index,arrayOfImmoveAbleChar,valtoadd):
#     if valtoadd == 10:
#         counterofcounter = 1
#         while(True):
#             if arrayOfImmoveAbleChar[index-counterofcounter] >=2:
#                 counterofcounter +=1
#             else:
#                 return sudokuRecursion(n,index-counterofcounter,arrayOfImmoveAbleChar,n[index-counterofcounter]+1)
        
#     if arrayOfImmoveAbleChar[index] == 2:
#         sudokuRecursion(n,index + 1,arrayOfImmoveAbleChar,valtoadd)
#     else:
#         n[index] = 0
#         varTocheck = checkIfValAllowed(valtoadd,sudokumapval,index)
#         if varTocheck == 1:
#             n[index] = valtoadd
#             return sudokuRecursion(n,index+1,arrayOfImmoveAbleChar,1)
#         else:
#             return sudokuRecursion(n,index,arrayOfImmoveAbleChar,valtoadd+1)
        


# #Depricated
# def putValOnMap(sudokuMapVar, immoveableArrOfNum):
#     counter = 0 
#     for y in  range(9):
#         for x in range(9):
#             if immoveableArrOfNum[counter] == 2:
#                 pass
#             if immoveableArrOfNum[counter] < 2:
#                 for i in range(1,11):
#                     checkerVar = checkIfValAllowed(i,sudokuMapVar,y,x)
#                     if checkerVar == 1:
#                         sudokuMapVar[y][x] = i
#                         break
#             counter += 1
#     return sudokuMapVar

def makeImmoveAbleArr(valArr):
    immoveableArr = []
    for y in valArr:
        for x in y:
            if x == 0:
                immoveableArr.append(0)
            else:
                immoveableArr.append(2)
    return immoveableArr


def sudokumap(sudokuValn):
    for i in range(9):
        print("----",end='')
    print()
    for y in range(9):
        for x in range(9):
            print("| {} ".format(sudokuValn[y][x]),end='')
            if (x)  ==  8:
                print("|")
        for z in range(9):
            print("----",end='')
        print()


def sudokomaker(sudokuNums):
    sudokuVal = []
    numcounter = 0
    for y in range(9):
        sudokuVal.append([])
        for x in range(9):
            sudokuVal[y].append(sudokuNums[numcounter])
            numcounter = numcounter + 1
    return sudokuVal
    #print(sudokuVal)
def multiDimmensionalArry():
    arrayofArry = []
    counter = 0
    for y in range(9):
        arrayofArry.append([])
        for x in range(9):
            arrayofArry[y].append(arrayOfImmoveAbleChar[counter])
            counter += 1
    return arrayofArry

if __name__ == "__main__":
    oneBigSudoku = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0]
    index = 0
    sudokumapval  = sudokomaker(oneBigSudoku)
    sudokumap(sudokumapval)
    arrayOfImmoveAbleChar = makeImmoveAbleArr(sudokumapval)
    valy = 0
    valx = 0
    global truecounter 
    truecounter = 0 
    valtoadd = 1
    gornArr = multiDimmensionalArry()
    arrayOfImmoveAbleChar = gornArr
    print(arrayOfImmoveAbleChar)
    sudokuRecursionversion2()
    print(sudokumapval)
    #print(sudokuRecursion(oneBigSudoku,index,arrayOfImmoveAbleChar,valtoadd))
    #sudokumap(putValOnMap(sudokumapval,arrayOfImmoveAbleChar))