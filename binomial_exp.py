# binomial_exp.py ---
#
# Filename: binomial_exp.py
# Description:
# Author: Subhasis Ray
# Created: Tue Jul 21 10:36:54 2026 (+0530)
#

# Code:
#%%
import numpy as np
#%%
N = 30
H = [19, 11, 13, 17, 14, 14, 14, 12, 16, 16, 15, 20, 23,15, 16, 17, 16, 12, 14, 17]

n = len(H)
print('Number of trials/sample size n=', n)

#%%
mean = sum(H) / n
print('Sample mean =', mean)
#%%
deviations = [(h - mean) for h in H]
print('deviations', deviations)
print('Sum of deviation', sum(deviations))
#%%
abs_dev = [abs(dev) for dev in deviations]

print('Sum of absolute deviation', sum(abs_dev))

#%%
squared_dev = [dev*dev for dev in deviations]
print('Sum of squared deviations (sample variance)', sum(squared_dev))
#%%
s2 = sum(squared_dev)/n
print('Average of squared deviations', s2)
print('Root mean squared deviation, standard deviation', np.sqrt(s2))
#%%
s2 = sum(squared_dev)/(n-1)
print('Average of squared deviations', s2)
print('Root mean squared deviation, standard deviation', np.sqrt(s2))

#%%
import matplotlib.pyplot as plt
plt.hist(H, bins=np.arange(31))
plt.show()
#%%

print('Theoretical variance:', 20 * 0.5 * 0.5)
print('SD', np.sqrt(20 * 0.5 * 0.5))
#%%

#
# binomial_exp.py ends here
