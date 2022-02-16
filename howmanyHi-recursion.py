
counter = 0
def hicounter(n,k):
    global counter
    lengthofn = len(n) - 1
    if n == '':
        return
    minusminus = 0
    correctcounter = 0
    for i in range(len(k)-1,-1,-1):
        if n[lengthofn - minusminus] == k[i]:
            correctcounter = correctcounter +1
            minusminus = minusminus + 1
        else: 
            break
    if correctcounter == len(k):
            counter = counter +1 
    return hicounter(n[:len(n) - 1],k)

    
if __name__ == "__main__":
    stringset= "xhixhxihihhhih"
    stringcheck = "hi"
    hicounter(stringset,stringcheck)
    print(counter)