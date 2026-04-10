with open('rosalind_hamm.txt', 'r') as f:
    dna1, dna2 = f.read().strip().split('\n')
mutations = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        mutations += 1
with open('hammingdistance.txt', 'w') as F:
    F.write(str(mutations))