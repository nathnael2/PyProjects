def isPotentialGene(dna):
    # number of bases is a multiple of 3
    if (len(dna) % 3) != 0:
        return False
    # starts with start codon
    if not dna.startswith('ATG'):
        return False
        # no intervening stop codons
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i:i+3] == 'TAA':
                return False
            if dna[i:i+3] == 'TAG':
                return False
            if dna[i:i+3] == 'TGA':
                return False
        # ends with a stop codon
    if dna.endswith('TAA'):
        return True
    if dna.endswith('TAG'):
        return True
    if dna.endswith('TGA'):
        return True
    return False

def isDNA(astr):
    ''' returns True when astr consists of only the letters A, T, C, and G, otherwise returns False '''
    bases = ['A','T','C','G']
    for i in astr:
        if i not in bases:
            return False
    return True

def longestEqual(dnaStr):
    '''return the pair (start, stop) such that dnaStr[start:stop] is the longest contiguous sequence of equal values in  dnaStr'''
    track_of_index = {}
    count_freq = 1
    for i in range(1,len(dnaStr)):
        if dnaStr[i] == dnaStr[i-1]:
            count_freq +=1
        elif(count_freq > 1):
            track_of_index[i] = count_freq
            count_freq = 1
    values_of_index = []
    for value in track_of_index.values():
        values_of_index.append(value)
    max_freq = max(values_of_index)
    max_key = 0
    for key in track_of_index.keys():
        if track_of_index[key] == max_freq:
            max_key = key
    return (max_key-max_freq,max_key)

def potentialGenes(dnaStr, m):
    '''Returns a list of pairs (start, stop) of all substrings of dnaStr  where dnaStr[start:stop] are
    all potential genes contained in dnsString of length greater than or equal to m. '''
    list_of_potential_genes = []
    for i in range (m,len(dnaStr)):
        for j in range(i+3,len(dnaStr)):
            if isPotentialGene(dnaStr[i:j]):
                list_of_potential_genes.append((i,j))
    return list_of_potential_genes
def highestConcentration(dnaStr, symbol):
    '''return the pair (start, stop) such that dnaStr[start:stop] has the highest symbol concentration
    of any substring of dnaStr'''
    track_of_index = {}
    count_freq_symbol = 1
    for i in range(1,len(dnaStr)):
        if dnaStr[i] == dnaStr[i-1] and dnaStr[i-1] == symbol:
            count_freq_symbol +=1
        elif(count_freq_symbol > 1):
            track_of_index[i] = count_freq_symbol
            count_freq_symbol = 1
    values_of_index = []
    for value in track_of_index.values():
        values_of_index.append(value)
    max_freq = max(values_of_index)
    max_key = 0
    for key in track_of_index.keys():
        if track_of_index[key] == max_freq:
            max_key = key
    return (max_key-max_freq,max_key)
def main():
    dna5 = '''ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC
CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC
CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG
TTTAATTACAGACCTGAA'''
    dna = {'string1':'ATGGTAATGAATTAA','string2':'ATGGTAATGAATAGATAG','string3':'ATGGTAATGAATAGATAG','string4':'TAAATGGTAATGTAAATG',
           'string5':dna5}
    m = 0
    symbol = 'A'
    for key,value in dna.items():
        if isPotentialGene(value):
            print("%s is a potential gene"%key)
        else:
            print("%s is not a potential gene"%key)
        if isDNA(value):
            print("%s is a DNA"%key)
        else:
            print("%s is not DNA"%key)
        longest = longestEqual(value)
        print("%s: longest equal in format(start,stop)-->"%key,longest)
        potential_gene = potentialGenes(value,m)
        print("%s: potential genes in format (start,stop)-->"%key,potential_gene)
        highest_concentration = highestConcentration(value,symbol)
        print("%s: highest concentratio of base %s in format(start,stop)-->"%(key,symbol),highest_concentration)
        print()
main()
