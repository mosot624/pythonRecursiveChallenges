def reversestring(n):
    if n  ==  "":
        return ""
    name = n[:-1]
    y = n[len(n)-1]
    return y + reversestring(name)

if __name__ == "__main__":
    stringval = "Michael"
    print(reversestring(stringval))