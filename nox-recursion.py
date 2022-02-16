def noxstr(n):
    temp =  ""
    if n == "":
        return ""
    elif n[0] == "x":
        temp = ""
    else:
        temp = n[0]
    n = n[1:]
    return temp + noxstr(n)

if __name__ == "__main__":
    stringval = "axxbxx"
    print(noxstr(stringval))