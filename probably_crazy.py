with open('rosalind_iprb.txt', 'r') as f:
    k_str, m_str, n_str = f.read().strip().split()
    k = int(k_str)
    m = int(m_str)
    n = int(n_str)
total = k + m + n
mm_prob = (m/total) * ((m-1)/(total-1)) * 0.25
nn_prob = (n/total) * ((n-1)/(total-1)) * 1.0
mn_prob = (((m/total) * (n/(total-1))) + ((n/total) * (m/(total-1)))) * 0.5
total_prob = 1.0 - mm_prob - nn_prob - mn_prob
with open('total_probability_answer.txt', 'w') as F:
          F.write(str(total_prob))