with open('rosalind_revc.txt', 'r') as f:
    original_dna = f.read().strip()
reversed_dna = original_dna[::-1]
decoding_dictionary = str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})
reverse_complement = reversed_dna.translate(decoding_dictionary)
with open('reverse_complement.txt', 'w') as F:
    F.write(reverse_complement)