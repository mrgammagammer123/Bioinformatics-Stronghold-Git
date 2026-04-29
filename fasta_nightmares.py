fasta_dict = {}
current_id = ""
with open('rosalind_grph.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'): 
            current_id = line[1:] 
            fasta_dict[current_id] = "" 
        else:
            fasta_dict[current_id] += line
edges = []
for id1, dna1 in fasta_dict.items():
    for id2, dna2 in fasta_dict.items():
        if id1 != id2:
            if dna1[-3:] == dna2[:3]:
                edges.append(f"{id1} {id2}")
with open('overlapping_graphs.txt', 'w') as F:
    for edge in edges:
        F.write(f"{edge}\n")