with open('rosalind_fib.txt', 'r') as f:
    n_string, k_string = f.read().strip().split()
    n = int(n_string)
    k = int(k_string)
adults = 0
babies = 1
for i in range(n-1):
    adults, babies = (adults + babies), (adults * k)
with open('wabbits.txt', 'w') as F:
    F.write(str(adults + babies))