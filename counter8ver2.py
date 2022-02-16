import math

counter = 0
def counter8(n):
    global counter
    n = math.floor(n)
    if n <= 0:
        return 1
    else:
        if n % 100 == 88:
            counter = counter + 2
        elif n % 10 == 8:
            counter = counter + 1
        return counter8(n/10)

    
if __name__ == "__main__":
    counter8(1818188)
    print(counter)
    #print(8%10)