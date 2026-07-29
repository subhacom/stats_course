# binomial_to_gaussian.py ---
#
# Filename: binomial_to_gaussian.py
# Description:
# Author: Subhasis Ray
# Created: Sun Jul 26 09:08:43 2026 (+0530)
#

# Code:
"""Simulation of binomial distribution to obtain approximate Gaussian"""
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
def bean_draw_0(N, n_red, total=1000):
    """Draw `N` beans from a mix of red and white where the number of
    red beans is `n_red`, and the total number of beans is `total`.


    This is the naive version of the bean_draw - we layout everything
    we did experimentally.

    """
    n_white = total - n_red  # number of white beans

    # Make a list of `n_red` "red" and a list of `n_white` "white"
    # beans, and concatenate them
    beans = ['red'] * n_red + ['white'] * n_white

    picked = []  # List of 1s and 0s indicating if a picked bean is red or white

    for ii in range(N):
        np.random.shuffle(beans)
        # Pick the first bean after shuffling. This is a single
        # Bernoulli trial. We could as well picked the second, third,
        # ..., last bean - it should not matter.
        success = 1 if beans[0] == 'red' else 0
        picked.append(success)
    return picked


N = 10   # no. of draws
n_red = 50  # number of red beans in the population
tot_beans = 2 * n_red    # total number of beans in the bowl - twice that of red beans to make p = 0.5

n_experiments = 20  # number of binomial experiments - how many times we collect an N-sample

counts = []   # collect the number of red beans in each experiment
for ii in range(n_experiments):
    picked = bean_draw_0(N, n_red, tot_beans)
    counts.append(sum(picked))

#%%
fracs = [count/N for count in counts]
print(f'Count of red beans out of {N} draws in {n_experiments} experiments : {counts}')
print('Sample means:', [count/N for count in counts])
print('Mean of the sample means:', np.mean(fracs))
print('Theoretical mean of the sample means:', p)
print('Variance of the sample means:', np.var(fracs))
print('Variance of the sample means with Bessel\'s correction:', np.var(fracs, ddof=1))
print('Theoretical variance:', p * (1-p) / N)
#%%
fig, ax = plt.subplots()
ax.hist(fracs)
plt.show()
#%%


#
# binomial_to_gaussian.py ends here
