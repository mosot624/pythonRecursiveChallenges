from math import floor as rounder
def counter8(n):
    counter = 0
    n = rounder(n)
    if n % 100 == 88:
        counter = counter + 2
    elif n %  10 ==  8:
        counter = counter + 1
    if n <= 0:
        return 0
    return counter + counter8(n/10)

if __name__ == "__main__":
    print(counter8(8818181))
