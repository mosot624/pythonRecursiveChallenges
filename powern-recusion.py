def powern(n,mult):
    if mult == 0:
        return 0
    if mult == 1:
        return n
    return n * powern(n,mult-1)
if __name__ == "__main__":
    print(powern(2,5))