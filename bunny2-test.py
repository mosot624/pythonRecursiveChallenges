def bunny2(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n % 2 == 0:
        return 3 + bunny2(n-1)
    else:
        return 2 + bunny2(n-1)

    
if __name__ == "__main__":
    print(bunny2(5))