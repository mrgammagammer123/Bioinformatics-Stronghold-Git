fasta_dict = {}
current_id = ""
with open('rosalind_lcsm.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]
            fasta_dict[current_id] = ""
        else:
            fasta_dict[current_id] += line
dna_list = list(fasta_dict.values())
short_king = min(dna_list, key=len)
shared_motif = ""
for window_size in range(len(short_king), 0, -1):
        for i in range(len(short_king) - window_size + 1):
            chunk = short_king[i : i + window_size]
            if all(chunk in dna for dna in dna_list):
                shared_motif = chunk
                break
        if shared_motif != "":
            break
with open('rosalind13.txt', 'w') as F:
    F.write(shared_motif)