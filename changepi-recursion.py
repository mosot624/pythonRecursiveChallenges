def pichanger(n):
    if n  ==  "":
        return ""
    elif n[len(n) -  1]  ==  "i" and n[len(n) -  2]  ==  "p":
        n = list(n)
        n[len(n) - 1] = ""
        n[len(n) - 2] = ""
        n = "".join(n)
        n = n + "3.14"
    name = n[:-1]
    return pichanger(name) + n[len(n)-1]
if __name__ == "__main__":
    stringval = "pip"
    print("{} is now {}".format(stringval,pichanger(stringval)))