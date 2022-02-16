import math
def counter7(n):
    counter = 0
    n = math.floor(n)
    if n %  10 ==  7:
        counter = counter + 1
    if n <= 0:
        return 0
    return counter +  counter7(n/10)

    
if __name__ == "__main__":
    print(counter7(777576197))