from typing import Counter


def sumitup(n):
    counter = 0
    if not n:
        return 0
    elif n[0] == 6:
        counter = counter + 1
    return counter + sumitup(n[1:])

if __name__ == "__main__":
    arr6 = [11, 11]

    print(sumitup(arr6))