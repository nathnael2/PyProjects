# DNA exercises Oct 15
import random

def randomDNA(sl):
    myseq = ''
    for k in range(sl):
        # get next letter
        nextLetter = random.choice(['A', 'C', 'G', 'T'])
        # append it
        myseq = myseq + nextLetter
    return myseq

def randomDNAList(sl, m):
    myList = []
    for k in range(m):
        myList.append(randomDNA(sl))
    return myList

def complementWC(dnaStr):
    answer = ''
    dnaDict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    for ch in dnaStr:
        answer = answer + dnaDict[ch]
    return answer

def reverse(astr):
    answer = ''
    for ch in astr:
       answer = ch + answer
    return answer
       

def palindromeWC(d):
    return  reverse(d) == complementWC(d)
   
def main():
##    n = 15
##    for k in range(n):
##        print(randomDNA(k))

    dnaList = randomDNAList(4, 20)
##    for d in dnaList:
##        print(d, complementWC(d))

    for d in dnaList:
        print(d, palindromeWC(d))
        


        

main()
