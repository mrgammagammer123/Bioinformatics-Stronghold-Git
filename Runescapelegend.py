with open('rosalind_dna.txt', 'r') as f:
    nucleotide_string = f.read().strip()
A = nucleotide_string.count('A')
C = nucleotide_string.count('C')
G = nucleotide_string.count('G')
T = nucleotide_string.count('T')
with open('nucleotidestring.txt', 'w') as F:
    F.write(f"{A} {C} {G} {T}")