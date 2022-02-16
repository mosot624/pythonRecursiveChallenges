
varIntNoaxis = {}

def boxSolver(n,m):
    if (n,m) in varIntNoaxis:
        return varIntNoaxis[n,m]
    if n == 1 or m == 1:
        value = 1
    else:
        value = boxSolver(n-1,m) + boxSolver(n,m-1)
    varIntNoaxis[n,m] = value
    return value
if __name__ == "__main__":
    print(boxSolver(100,100))
    print()