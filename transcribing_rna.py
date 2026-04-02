with open('rosalind_rna.txt', 'r') as f:
    original_dna = f.read().strip()
transcribed_rna = original_dna.replace('T', 'U')
with open('RNAfromdna.txt', 'w') as F:
    F.write(transcribed_rna)    