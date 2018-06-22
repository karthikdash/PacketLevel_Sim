import numpy as np
# 0.02 + 0.005*10
# 0.009 + 0.001*10
# 0.02 + 0.005*7
# 0.02 + 0.001*8
# 0.02 + 0.005*9
# 0.001 + 0.001*10
lamb = np.arange(0.001, 0.01, 0.001)

print lamb
final_csv = np.zeros((len(lamb),8))
i = 0
for lam in lamb:
    res1 = np.genfromtxt('./resultsHetero' + str(round(lam, 3)) + '.csv', delimiter=',')
    final_csv[i,:] = res1
    i += 1
np.savetxt("packet_new.csv", final_csv, delimiter=",", fmt="%.5f")

