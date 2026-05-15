import math
with open('rosalind_lia.txt', 'r') as f:
    k , N = map(int, f.read().strip().split())
total = 2**k
total_probability = 0
for x in range(N, total + 1):
    combinations = math.comb(total, x)
    prob_x = combinations * (0.25**x) * (0.75**(total-x))
    total_probability += prob_x
with open('allele_answer.txt', 'w') as F:
    F.write(f"{total_probability}")