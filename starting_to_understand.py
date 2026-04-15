with open('rosalind_subs.txt', 'r') as f:
    s, t = f.read().strip().split('\n')
positions = ""
for i in range(len(s)):
    window = s[i : i+len(t)]
    if window == t:
        positions += f"{i + 1} "
with open('motif_solutions.txt', 'w') as F:
    F.write(positions)