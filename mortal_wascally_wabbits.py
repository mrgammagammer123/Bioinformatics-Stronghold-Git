with open('rosalind_fibd.txt', 'r') as f:
    n, m = map(int, f.read().strip().split())
ages = [0] * m
ages[0] = 1
for _ in range(n-1):
    survivors = ages[:-1]
    new_babies = sum(ages[1:])
    ages = [new_babies] + survivors
with open('mortal_rabbits.txt', 'w') as F:
    F.write(f"{sum(ages)}")