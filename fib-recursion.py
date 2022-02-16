fibmemo = {}

def fib(n):
    if n in fibmemo:
        return fibmemo[n]
    if n <= 0:
        value = 0
    elif n == 1:
        value= 1
    else:
        value  = fib(n - 1) + fib(n-2)
    fibmemo[n] = value
    return value
    

if __name__ == "__main__":
    print(fib(10))