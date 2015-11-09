import math
def dnaUnitVector(filename):
    alphabets = ['A','C','T','G']
    length_three_string = []
    for i in alphabets:
        for j in alphabets:
            for k in alphabets:
                string = i + j + k
                length_three_string.append(string)
    frequency_of_strings = [0 for k in range(64)]
    with open(filename) as myfile:
        astr = myfile.read()
        astr = astr.upper()
        for c in range(len(astr)-3):
            for k in range(len(length_three_string)):
                if astr[c:c+3] == length_three_string[k]:
                    frequency_of_strings[k] += 1
        sum_of_squares = 0
        for i in range(len(frequency_of_strings)):
            sum_of_squares += frequency_of_strings[i]**2
        square_root = math.sqrt(sum_of_squares)
        unitVector = frequency_of_strings[:]
        for i in range(len(unitVector)):
            unitVector[i] = unitVector[i]/square_root
        return unitVector
def dotProduct(u1,u2):
    if len(u1) != len(u2):
        return
    dot_product = 0
    for i in range(len(u1)):
        dot_product += u1[i]*u2[i]
    return dot_product 
def dataMining():
    file1 = 'dna3.txt'
    file2 = 'rdna1.txt'
    vector1 = dnaUnitVector(file1)
    vector2 = dnaUnitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    # a correlation of 1 or 100% means the two files are very simillar while a correlation of
    # 0 means they have no simillarity
    print("-------------------------------------------------------------------------")


    file1 = 'rdna.txt'
    file2 = 'dna3.txt'
    vector1 = dnaUnitVector(file1)
    vector2 = dnaUnitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")

    file1 = 'dna3.txt'
    file2 = 'ecoli.txt'
    vector1 = dnaUnitVector(file1)
    vector2 = dnaUnitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")


    file1 = 'ecoli.txt'
    file2 = 'dna4.txt'
    vector1 = dnaUnitVector(file1)
    vector2 = dnaUnitVector(file2)
    dot_product = dotProduct(vector1,vector2)
    print("There is a %f%% correlation between %s and %s"%(dot_product*100/1,file1,file2))
    print("-------------------------------------------------------------------------")


    

    
def main():
    dataMining()

main()    
