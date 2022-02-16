import math
def sumdigi(n):
    if n <= 0:
        return 0
    if n < 10 and n > 0:
        return math.floor(n)
    return sumdigi(n/10) + sumdigi(n%10)
if __name__ == "__main__":
    print(sumdigi(235))