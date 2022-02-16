lefuncArr = {}
def partionRec(n,m):
    if (n,m) in lefuncArr:
        return lefuncArr[n,m]
    if n == 0:
        val = 1
    elif m == 0 or n < 0:
        val  =  0
    else:
        val = partionRec(n-m,m)  +  partionRec(n,m-1)
    lefuncArr[n,m] = val
    return val

if __name__ == "__main__":
    print(partionRec(9,5))