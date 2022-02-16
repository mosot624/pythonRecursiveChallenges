def funcRe(n):
    if n <= 1:
        return 1
    else: 
        return n * funcRe(n-1)
if __name__ == "__main__":
    print(funcRe(5))