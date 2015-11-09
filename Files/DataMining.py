import math
def unitVector(filename):
    with open(filename) as myfile:
        astr = myfile.read()
        astr = astr.lower()
        listA = [0 for k in range(26)]
        for c in astr:
            if c >= 'a' and c <= 'z':
                index = ord(c) - ord('a')
                listA[index] += 1
        sum_of_squares = 0
        for i in range(len(listA)):
            sum_of_squares += listA[i]**2
        square_root = math.sqrt(sum_of_squares)
        unit_vector = listA[:]
        for i in range(len(unit_vector)):
            unit_vector[i] = unit_vector[i]/square_root
        return unit_vector
def dotProduct(u1,u2):
    if len(u1) != len(u2):
        return
    dot_product = 0
    for i in range(len(u1)):
        dot_product += u1[i]*u2[i]
    return dot_product
def dataMining():
    file1 = 'moby.txt'
    file2 = 'PrideAndPredjudiceChap1-3.txt'
    vector1 = unitVector(file1)
    vector2 = unitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    # a correlation of 1 or 100% means the two files are very simillar while a correlation of
    # 0 means they have no simillarity
    print("-------------------------------------------------------------------------")


    file1 = 'JohnOliver.txt'
    file2 = 'Ethiopia.txt'
    vector1 = unitVector(file1)
    vector2 = unitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")

    file1 = 'dna4.txt'
    file2 = 'ecoli.txt'
    vector1 = unitVector(file1)
    vector2 = unitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")


    file1 = 'MrRobot.py'
    file2 = 'PokerHands.py'
    vector1 = unitVector(file1)
    vector2 = unitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")


    

    
def main():
    dataMining()

main()
