# bernoulli_to_gaussian.py ---
#
# Filename: bernoulli_to_gaussian.py
# Description:
# Author: Subhasis Ray
# Created: Tue Jul 28 10:22:58 2026 (+0530)
#

# Code:

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
results = {'risani': [4, 5, 5, 5, 4, 5, 1, 7, 3],
           'arshama': [5, 4, 3, 5, 5, 6, 5, 7],
           'sudipta': [5, 4, 6, 1, 4, 5],
           'swarnima': [3, 2, 5, 4],
           'jyotirmay': [5, 7, 7],
           'mayuri': [5, 5, 5, 2],
           'anshuman': [6, 7]}

#%%

counts = []
for name, res in results.items():
    counts += res

print(counts, 'number of samples', len(counts))

print('Mean', np.mean(counts))
print('Variance', np.var(counts))

N = 10
sample_means = [count / N for count in counts]
print('Sample means', sample_means)
#%%
print('Mean of means', np.mean(sample_means))
print('Variance in sample mean', np.var(sample_means))

#%% taking 4 draws as a single 40-draw
counts_40 = [sum(counts[ii:ii+4])
             for ii in range(0, len(counts), 4)]
print('COunts for 40 draws', counts_40)
sample_means_40 = [count / 40.0 for count in counts_40]

print('Variance for 40 draws', np.var(sample_means_40))

#%%
fig, axes = plt.subplots(nrows=2, sharex='all', sharey='all')
axes[0].hist(sample_means, bins=np.linspace(0, 1, 10))
axes[1].hist(sample_means_40, bins=np.linspace(0, 1, 10))
plt.show()


#
# bernoulli_to_gaussian.py ends here
