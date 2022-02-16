def multiCounter(n):
    counter = 0
    j = len(n)
    for i in range(len(n)):
        if type(n[i]) ==  int:
            counter = counter + 1
        if type(n[i]) == list:
            counter = counter + multiCounter(n[i])
    return counter

if __name__ == "__main__":
    arryArry =[[1,2,3,4],[5,[6],[7],[[8,9],10]],11,[12,[13,14]]]

    print(multiCounter(arryArry))