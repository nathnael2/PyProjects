import random

def randomDNA(filename, length):
    with open(filename, 'w') as f:
        for k in range(length):
            f.write(random.choice(['A', 'T', 'G', 'C']))
    print("Done creating", filename, "with", length, "characters.")

randomDNA("dna4.txt", 3000)
