# Part 1

# checksum without collections
def checksum(file):
    n2 = 0
    n3 = 0
    dFile = open(file, "r")
    for line in dFile:
        flag2 = False
        flag3 = False
        iter = 0
        n = 1
        line = sorted(line)
        if line[0] == '\n':
            line.remove('\n')
        while (iter < len(line)-1) and (flag2 == False or flag3 == False):
            if line[iter] == line[iter + 1]:
                n += 1
            else:
                if n == 2:
                    flag2 = True
                elif n == 3:
                    flag3 = True
                n = 1
            iter += 1
        if(n == 2):
            flag2 = True
        elif(n == 3):
            flag3 = True
        if flag2 == True:
            n2 += 1
        if flag3 == True:
            n3 += 1
    dFile.close()
    return n2 * n3

# Part 2

def similarite(file):
    iter = 0
    max = 0
    mot1 = []
    mot2 = []
    flag = False
    res = ""
    dFile = open(file, "r")
    lFile = dFile.readlines()
    while (flag == False) and (iter < len(lFile)):
        w1 = lFile[iter]
        for j in range(iter+1, len(lFile)):
            i = 0
            w2 = lFile[j]
            for k in range(len(w2)):
                if w1[k] == w2[k]:
                    i += 1
            if i > max:
                max = i
                mot1 = w1
                mot2 = w2
        if max == len(w1):
            flag = True
        iter += 1
    dFile.close()
    for i in range(len(mot1)):
        if mot1[i] == mot2[i]:
            res += mot1[i]
    return res

print(checksum("input.txt"))
print(similarite("input.txt"))