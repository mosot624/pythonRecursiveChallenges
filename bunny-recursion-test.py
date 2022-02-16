def bunnymult(n):
    if n <= 0:
        return 0
    if n == 1:
        return 2
    else:
        return 2 + bunnymult(n-1)


if __name__ == "__main__":
    print(bunnymult(0))