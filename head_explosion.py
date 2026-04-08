fasta_dict = {}
current_id = ""
with open('rosalind_gc.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'): 
            current_id = line[1:] 
            fasta_dict[current_id] = "" 
        else:
            fasta_dict[current_id] += line
highest_id = ""
highest_gc = 0.0
for seq_id, dna in fasta_dict.items():
    gc_percent = (dna.count('C') + dna.count('G')) / len(dna) * 100
    if gc_percent > highest_gc:
        highest_gc = gc_percent
        highest_id = seq_id
with open('fasta_dictionary.txt', 'w') as F:
    F.write(f"{highest_id}\n{highest_gc}")