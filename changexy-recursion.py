def changerxtoy(n):
    if n  ==  "":
        return ""
    elif n[len(n) -  1]  ==  "x":
        n = list(n)
        n[len(n) - 1] = "y"
        n = "".join(n)
    name = n[:-1]
    return changerxtoy(name) + n[len(n)-1]

if __name__ == "__main__":
    stringval = "yyhxyi"
    print(changerxtoy(stringval))