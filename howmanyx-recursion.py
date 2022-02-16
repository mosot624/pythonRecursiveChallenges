
counterar = 0
def howmanyx(n):
    global counterar
    lenthofn = len(n) - 1
    if n == '':
        return
    if n[lenthofn]  == 'x':
        counterar = counterar + 1
    return howmanyx(n[:len(n) - 1])

      
if __name__ == "__main__":
    stringval =  "xhixhix"
    print(howmanyx(stringval))
    print("There are {} x on {}".format(counterar,stringval))