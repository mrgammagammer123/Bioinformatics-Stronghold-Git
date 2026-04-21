fasta_dict = {}
current_id = ""
with open('rosalind_cons.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]
            fasta_dict[current_id] = ""
        else:
            fasta_dict[current_id] += line
dna_list = list(fasta_dict.values())
n = len(dna_list[0])
profile = {
    'A': [0] * n,
    'C': [0] * n,
    'G': [0] * n,
    'T': [0] * n
}
for i in range(n):
    for dna in dna_list:
        letter = dna[i]
        profile[letter][i] += 1
consensus = ""
for i in range(n):
    max_score = 0
    winning_letter = ""
    for nucleotide in ['A', 'C', 'G', 'T']:
        current_score = profile[nucleotide][i]      
        if current_score > max_score:
            max_score = current_score
            winning_letter = nucleotide
    consensus += winning_letter
with open('consensus_output.txt', 'w') as F:
    F.write(f"{consensus}\n")
    for nucleotide in ['A', 'C', 'G', 'T']:
        scores_string = " ".join(map(str, profile[nucleotide]))
        F.write(f"{nucleotide}: {scores_string}\n")