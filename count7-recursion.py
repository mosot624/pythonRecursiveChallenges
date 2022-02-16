import math
def counter7(n):
    counter = 0
    n = math.floor(n)
    if n < 10 and n == 7:
        return counter + 1
    if n < 10 and n != 7:
        return  counter
    counter = counter7(n/10) + counter7(n%10)
    return counter
if __name__ == "__main__":
    print(counter7(7717))