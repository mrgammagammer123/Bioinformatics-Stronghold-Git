with open('rosalind_iev.txt', 'r') as f:
    g1, g2, g3, g4, g5, g6 = map(int, f.read().strip().split())
expected_total = (g1 * 2) + (g2 * 2) + (g3 * 2) + (g4 * 1.5) + (g5 * 1) + (g6 * 0)
with open('expected_pops.txt', 'w') as F:
    F.write(f"{expected_total}")